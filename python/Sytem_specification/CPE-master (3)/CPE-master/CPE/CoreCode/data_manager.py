import hashlib

import CoreCode.logger as Logger
import CoreCode.chiefnet_exception as ChiefnetException


class DataManager():
    """
    DataManager is used to fetch/post the data from/to the desired endpoint using the CommunicationManager
    
    Arguments:
    communication_manager:
            Instance of the CommunicationManager    
    """

    def __init__(self, communication_manager):
        self.__logger = Logger.get_logger(__name__)
        self.__logger.info("DataFetcher initializer starts")

        self.__communication_manager = communication_manager

        self.__logger.info("DataFetcher initializer ends")
    

    def get_data(self, endpoint, checksum):
        """
        get_data gets the data from the endpoint and returns the data by validating it
        Args   - checksum : str type - recived data will be validated against this checksum
                 endpoint : str type - URL from where the data is fetched
        Return - bytestream type - If the fetching and validation of user provided data is done 
                 successfully it returns response content data as raw bytestream
        Raises - if data fetch fails DataFetchFailedException is raised
                 if validation fails ChecksumMismatchException is raised
        """
        try:
            byte_stream = self.__communication_manager.get_data(endpoint=endpoint)
        except ChiefnetException.CommunicationManagerException as communication_exception:
            self.__logger.error(communication_exception)
            raise ChiefnetException.DataFetchFailedException(communication_exception)

        if byte_stream != b"":

            try:
                data_integrity_check_status = self.__validate_data_integrity(byte_stream=byte_stream, checksum=checksum)
            except ChiefnetException.ChecksumMismatchException:
                raise ChiefnetException.ChecksumMismatchException

            if  data_integrity_check_status == True:
                self.__logger.info("Data validation success")
            else:
                self.__logger.error("Data validation failed")
        else:
            self.__logger.error("Empty data")
        
        return byte_stream
        

    def put_data(self, data, endpoint):
        """
        put_data puts the data to the endpoint and returns the checksum of the data
        Args   - data: dict type - Content which is going to get posted to the URL
                 endpoint : str type - URL to post the data
        Return - True - On successfully posted the data
                 False- On fails while posting the data
        Raises - DataPostFailedException - when post data fails, DataPostFailedException get raised
        """ 
        # Currently this function is used to POST only json data to the endpoint.
        try:
            is_data_posted_successfully = self.__communication_manager.post_data(data=data, endpoint=endpoint)
        except ChiefnetException.CommunicationManagerException as communication_exception:
            self.__logger.error(communication_exception)
            raise ChiefnetException.DataPostFailedException(communication_exception)

        if is_data_posted_successfully == True:
            self.__logger.info("Data posted successfully")
            return True
        else:
            self.__logger.error("Data post fails")
            return False


    def __validate_data_integrity(self, byte_stream, checksum):
        return_value = False
        calculated_checksum = ""

        calculated_checksum = self.__calculate_checksum(byte_stream=byte_stream)
 
        if calculated_checksum == checksum:
            return_value = True
        else:
            raise ChiefnetException.ChecksumMismatchException

        return return_value
    

    def __calculate_checksum(self, byte_stream):
        calculated_checksum = ""

        hash_md5 = hashlib.md5()

        try:
            # update() works only with byte stream
            hash_md5.update(byte_stream)
            calculated_checksum = hash_md5.hexdigest()

        except TypeError as type_error:
            self.__logger.error(type_error)
        except Exception as exception:
            self.__logger.error(exception)
        
        return calculated_checksum
