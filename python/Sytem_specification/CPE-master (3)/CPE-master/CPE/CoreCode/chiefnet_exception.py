""" ChiefNetException defines the following exception hierarchy:

* ChiefNetException
    * CommunicationManagerException
        * HttpCommunicationManagerException
            * HttpRequestException
    * DataManagerException
        * DataFetchFailedException
        * DataPostFailedException
        * ChecksumMismatchException
"""


class ChiefNetException(Exception):
    """
    Base class for all custom exceptions used in ChiefNet application 

    Arguments:
    chiefnet_exception_status:
        Default value is DEFAULT_CHIEFNET_EXCEPTION_STATUS
        When we pass string to this argument, ChiefNetException returns the provided string
    """
    DEFAULT_CHIEFNET_EXCEPTION_STATUS = "ChiefnetException raised"

    def __init__(self, chiefnet_exception_status=DEFAULT_CHIEFNET_EXCEPTION_STATUS):
        self._exception_status = chiefnet_exception_status


    def __str__(self):
        return(repr(self._exception_status))


class CommunicationManagerException(ChiefNetException):
    """
    Exception base class of all CommunicationManagers

    Arguments:
    communication_exception_status:
        Default value is DEFAULT_COMMUNICATION_MANAGER_EXCEPTION_STATUS
        When we pass string to this argument, CommunicationManagerException returns the provided string
    """
    DEFAULT_COMMUNICATION_MANAGER_EXCEPTION_STATUS = "CommunicationManagerException raised"

    def __init__(self, communication_exception_status=DEFAULT_COMMUNICATION_MANAGER_EXCEPTION_STATUS):
        ChiefNetException.__init__(self, chiefnet_exception_status=communication_exception_status)


    def __str__(self):
        return(repr(self._exception_status))


class HttpCommunicationManagerException(CommunicationManagerException):
    """
    Exception base class of HttpCommunicationManager

    Arguments:
    http_exception_status:
        Default value is DEFAULT_HTTP_COMMUNICATION_MANAGER_EXCEPTION_STATUS
        When we pass string to this argument, HttpCommunicationManagerException returns the provided string
    """
    DEFAULT_HTTP_COMMUNICATION_MANAGER_EXCEPTION_STATUS = "HttpCommunicationManagerException raised"

    def __init__(self, http_exception_status=DEFAULT_HTTP_COMMUNICATION_MANAGER_EXCEPTION_STATUS):
        CommunicationManagerException.__init__(self, communication_exception_status=http_exception_status)


    def __str__(self):
        return(repr(self._exception_status))


class HttpRequestException(HttpCommunicationManagerException):
    """
    Exception class of HttpRequestException
    It returns the Status of http Error

    Arguments:
    request_exception_status:
        Default value is DEFAULT_HTTP_REQUEST_EXCEPTION_STATUS
        When we pass string to this argument, HttpRequestException returns the provided string
    """
    DEFAULT_HTTP_REQUEST_EXCEPTION_STATUS = "HttpRequestException raised"

    def __init__(self, request_exception_status=DEFAULT_HTTP_REQUEST_EXCEPTION_STATUS):
        HttpCommunicationManagerException.__init__(self, http_exception_status=request_exception_status)

    def __str__(self):
        return(repr(self._exception_status))


class DataManagerException(ChiefNetException):
    """
    Exception base class of Data Fetcher

    Arguments:
    data_manager_exception_status:
        Default value is DEFAULT_DATA_MANAGER_EXCEPTION_STATUS
        When we pass string to this argument, DataManagerException returns the provided string
    """
    DEFAULT_DATA_MANAGER_EXCEPTION_STATUS = "DataManagerException raised"

    def __init__(self, data_manager_exception_status=DEFAULT_DATA_MANAGER_EXCEPTION_STATUS):
        ChiefNetException.__init__(self, chiefnet_exception_status=data_manager_exception_status)


    def __str__(self):
        return(repr(self._exception_status))


class DataFetchFailedException(DataManagerException):
    """
    Raises when data fetch get failed

    Arguments:
    data_fetch_exception_status:
        Default value is DEFAULT_DATA_FETCH_FAILED_EXCEPTION_STATUS
        When we pass string to this argument, ChecksumMismatchException returns the provided string
    """
    DEFAULT_DATA_FETCH_FAILED_EXCEPTION_STATUS = "DataFetchFailedException raised"

    def __init__(self, data_fetch_exception_status=DEFAULT_DATA_FETCH_FAILED_EXCEPTION_STATUS):
        DataManagerException.__init__(self, data_manager_exception_status=data_fetch_exception_status)


    def __str__(self):
        return(repr(self._exception_status))


class DataPostFailedException(DataManagerException):
    """
    Raises when data post get failed

    Arguments:
    data_post_exception_status:
        Default value is DEFAULT_DATA_POST_FAILED_EXCEPTION_STATUS
         When we pass string to this argument, DataPostFailedException returns the provided string
    """
    DEFAULT_DATA_POST_FAILED_EXCEPTION_STATUS = "DataPostFailedException raised"

    def __init__(self, data_post_exception_status=DEFAULT_DATA_POST_FAILED_EXCEPTION_STATUS):
        DataManagerException.__init__(self, data_manager_exception_status=data_post_exception_status)


    def __str__(self):
        return(repr(self._exception_status))


class ChecksumMismatchException(DataManagerException):
    """
    Raises when checksum mismatches

    Arguments:
    checksum_mismatch_exception_status:
        Default value is DEFAULT_CHECKSUM_MISMATCH_EXCEPTION_STATUS
        When we pass string to this argument, ChecksumMismatchException returns the provided string
    """
    DEFAULT_CHECKSUM_MISMATCH_EXCEPTION_STATUS = "ChecksumMismatchException raised"

    def __init__(self, checksum_mismatch_exception_status=DEFAULT_CHECKSUM_MISMATCH_EXCEPTION_STATUS):
        DataManagerException.__init__(self, data_manager_exception_status=checksum_mismatch_exception_status)


    def __str__(self):
        return(repr(self._exception_status))
