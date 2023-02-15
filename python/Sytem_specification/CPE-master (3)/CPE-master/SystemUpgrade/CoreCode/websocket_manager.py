import threading
import asyncio
import websockets

import CoreCode.logger as Logger
import Definitions.system_definitions as SystemDefinitions


class WebSocketManager:
    """
    This module is used to communicate with the WebsocketServer set up by the ChiefNet Webapplication

    Arguments:
    uri_manager:
        Instance of URIManager
    receive_data_callback:
        users of this module should register a callback to handle the data received by the
        websocket client. The receive_data_callback take a single argument. The received data
        will be of the format 'str' in case a text frame is received or 'bytes' in case of binary frame
    """

    def __init__(self, uri_manager):
        self.__logger = Logger.get_logger(__name__)
        self.__logger.info("WebSocketManager initialization start")

        self.__uri_manager = uri_manager
        self.__websocket_server_uri = uri_manager.get_server_connection_uri()

        # event loop object must be created before the thread starts so that other entities using it (e.g.send_data()) don't raise exception
        self.__websocket_event_loop = asyncio.new_event_loop()

        self.__websocket_event_thread = threading.Thread(target=self.__websocket_thread_function, daemon=True)
        self.__websocket_event_thread.start()

        self.__logger.info("WebSocketManager initialization end")


    def register_receive_data_callback(self, receive_data_callback):
        """
        To register the data callback function which is used to handle the data received from the websocket server
        Args   - receive_data_callback : callable function which takes string as a argument
        Return - None
        Raises - None
        """
        self.__receive_data_callback = receive_data_callback


    def send_data(self, data):
        """
        Used to send data to the websocket server. The arguments passed must be of type 'str'
        Args    - data : Takes a 'str' or 'byte' type as the argument
        Returns - None
        Raises  - TypeError : when invalid input is given     
        """
        push_to_data_queue_coroutine_object = self.__push_to_data_queue(data)
        asyncio.run_coroutine_threadsafe(push_to_data_queue_coroutine_object, loop=self.__websocket_event_loop)


    def __websocket_thread_function(self):   
        # set a new event loop as the default loop for this thread
        asyncio.set_event_loop(self.__websocket_event_loop)
        
        # asyncio queue must be created inside the event loop in which it is used to avoid 'future belongs to different loop' error
        self.__data_queue = asyncio.Queue(SystemDefinitions.MAX_DATA_QUEUE_SIZE) 

        self.__websocket_event_loop.create_task(self.__connection_handler_async())
        self.__websocket_event_loop.run_forever() 


    async def __connection_handler_async(self):
        while True:
            try:
                async with websockets.client.connect(self.__websocket_server_uri,
                                                    ping_interval=SystemDefinitions.PING_INTERVAL,
                                                    ping_timeout=SystemDefinitions.PING_TIMEOUT,
                                                    close_timeout=SystemDefinitions.CLOSE_TIMEOUT) as websockets_client: 
                    
                    self.__logger.info("Connected with {}".format(self.__websocket_server_uri))

                    receiver_task = asyncio.ensure_future(self.__receive_data_async(websockets_client))
                    sender_task = asyncio.ensure_future(self.__send_data_async(websockets_client))

                    # since the exceptions are caught in the sender and receiver tasks, the asyncio.wait must return
                    # on FIRST_COMPLETED task to detect disconnection, instead of FIRST_EXCEPTION
                    await asyncio.wait([receiver_task, sender_task], return_when=asyncio.FIRST_COMPLETED,)

                    self.__logger.info("Disconnected from {}".format(self.__websocket_server_uri))

                    self.__websocket_server_uri = self.__uri_manager.get_server_connection_uri()
                    
            except Exception as exception:
                self.__logger.error(exception)
                await asyncio.sleep(1)
                continue


    async def __receive_data_async(self, websockets_client):
        try:
            async for data in websockets_client:   # Asynchronours Comprehension. Generator of data
                self.__receive_data_callback(data) 

        except websockets.exceptions.ConnectionClosedError as connection_closed_error:
            self.__logger.error(connection_closed_error)
            
        except websockets.exceptions.ConnectionClosedOK as connection_closed_ok:
            self.__logger.info(connection_closed_ok)
            
        except Exception as exception:
            self.__logger.exception(exception)


    async def __send_data_async(self, websockets_client):         
        try:
            while True:
                data = await self.__data_queue.get()
                await websockets_client.send(data)

        except websockets.exceptions.ConnectionClosedError as connection_closed_error:
            self.__logger.error(connection_closed_error)

        except websockets.exceptions.ConnectionClosedOK as connection_closed_ok:
            self.__logger.info(connection_closed_ok)

        except Exception as exception:
            self.__logger.exception(exception)


    async def __push_to_data_queue(self, data):
        await self.__data_queue.put(data)
        await asyncio.sleep(0)
