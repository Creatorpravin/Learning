import requests

import CoreCode.logger as Logger
import Definitions.system_definitions as SystemDefinitions
import CoreCode.chiefnet_exception as ChiefnetException


class HttpCommunicationManager():
    """
    HttpCommunicationManager is used to manage the http based communication to get the data from the endpoint 
    and post the data to the endpoint

    Arguments:
    system_configuration_manager:
            Instance of SystemConfigurationManager
    authorization_request_header:
            Argument of type string, which consists of an authorization header
    """

    def __init__(self, system_configuration_manager, authorization_request_header):
        self.__logger = Logger.get_logger(__name__)
        self.__logger.info("HttpCommunicationManager initializer starts")

        self.__system_configuration_manager = system_configuration_manager

        try:
            self.__authorization_request_header_dict = {}
            self.__authorization_request_header_dict[SystemDefinitions.AUTHORIZATION_HTTP_HEADER_KEY] = authorization_request_header
        except ValueError as value__error:
            raise ValueError(value__error)

        self.__logger.info("HttpCommunicationManager initializer ends")
    

    def get_data(self, endpoint):
        """
        Function used to fetch data from the provided endpoint
        Args   - endpoint : str type - URL to perform GET request
        Return - byte type - On success, content of the response is returned as byte stream.
                             On failure, returns empty byte stream
        Raises - HttpRequestException - when http request exception get raised
        """
        response_data = b""

        try:
            # Without a timeout, code may hang for minutes or more till the connection and reading the content from the URL.
            # A good practice to set connect timeouts to slightly larger than a multiple of 3. 
            # Ref: https://requests.readthedocs.io/en/latest/user/advanced/#timeouts
            response = requests.get(url=endpoint, headers=self.__authorization_request_header_dict, timeout=SystemDefinitions.HTTP_TIMEOUT)
            response.raise_for_status()

        except requests.exceptions.RequestException as request_exception:
            self.__logger.error(request_exception)
            raise ChiefnetException.HttpRequestException(request_exception)
        except Exception as exception:
            self.__logger.error(exception)
            return response_data

        if response.status_code == requests.codes.ok:
            response_data = response.content
        else:
            self.__logger.error("Invalid response code - ", response.status_code)
        
        return response_data

    
    def post_data(self, data, endpoint):
        """
        Function used to post the data to the provided endpoint
        Args   - data : dict type - Content which is going to get posted to the URL 
                 endpoint : str type - URL to perform POST request
        Return - True - On success
                 False - On failure
        Raises - HttpRequestException - when http request exception get raised
        """
        try:
            response = requests.post(url=endpoint, headers=self.__authorization_request_header_dict, json=data)
            response.raise_for_status()

        except requests.exceptions.RequestException as request_exception:
            self.__logger.error(request_exception)
            raise ChiefnetException.HttpRequestException(request_exception)
        except Exception as exception:
            self.__logger.error(exception)
            return False

        if response.status_code == requests.codes.ok:
            return True
        else:
            self.__logger.error("Invalid response code - ", response.status_code)
            return False


    def post_data_with_response(self, data, endpoint):
        """
        Function used to post the data to the provided endpoint
        Args   - data : dict type - Content which is going to get posted to the URL 
                 endpoint : str type - URL to perform POST request
        Return - byte type, bool - On success, content of the response is returned as byte stream - True
                                   On failure, content of the error response is returned as byte stream - False
        """
        response_data = b""

        try:
            response = requests.post(url=endpoint, headers=self.__authorization_request_header_dict, json=data)
            response_data = response.content
            response.raise_for_status()
        except requests.exceptions.RequestException as request_exception:
            self.__logger.error(request_exception)
            return response_data, False
        except Exception as exception:
            self.__logger.error(exception)
            return response_data, False

        if response.status_code == requests.codes.ok:
            return response_data, True
        else:
            self.__logger.error("Invalid response code - ", response.status_code)
            return response_data, False