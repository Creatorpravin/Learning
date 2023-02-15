import os
import stat
import shutil
from zipfile import ZipFile

import Definitions.system_definitions as SystemDefinitions

# providing file permission to the qos_configuration.sh file equivalent to "chmod 755"
EXECUTABLE_PERMISSION = stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH

FILENAME_EXTENSION_SEPARATOR = "."
OLD_FILENAME_SUFFIX = "-old"
FILENAME_INDEX = 0
FILE_EXTENSION_INDEX = 1


def rotate_files(file_to_be_rotated_filepath, data_to_be_written_in_newfile, logger_object):
    """
    This function gets the filename of the file to be rotated and renames it with "-old" suffix.
    It then writes the data provided by the user into a new file which has the same filename as the file that was rotated.
    Args:
        file_to_be_rotated_filepath - the absolute path to the file that the user wants to rotate
        data_to_be_written_in_newfile - the bytes data that the user wants to write into the new file after the existing one is rotated
        logger_object - an object of type Logger which is used by this function to log messages
    """
    file_to_be_rotated_directory, _ = os.path.split(file_to_be_rotated_filepath)

    if os.path.exists(file_to_be_rotated_directory) == False:
        os.makedirs(file_to_be_rotated_directory)

    # check if file_to_be_rotated_filepath exists
    if os.path.isfile(file_to_be_rotated_filepath) == True:
        # rename the file_to_be_rotated_filepath with '-old' suffix
        filename_list = file_to_be_rotated_filepath.split(FILENAME_EXTENSION_SEPARATOR)
        old_suffixed_filepath = str(filename_list[FILENAME_INDEX]) + OLD_FILENAME_SUFFIX + FILENAME_EXTENSION_SEPARATOR + str(filename_list[FILE_EXTENSION_INDEX])

        try:
            os.replace(file_to_be_rotated_filepath, old_suffixed_filepath)
        except OSError as os_error:
            logger_object.error(os_error)
            return False
        except Exception as exception:
            logger_object.error(exception)
            return False

        logger_object.info("{} rotated as {} successfully".format(file_to_be_rotated_filepath, old_suffixed_filepath))

    # open a new file with the filename same as file_to_be_rotated_filepath
    # write data_to_be_written_in_newfile into the new file
    try:
        with open(file_to_be_rotated_filepath, SystemDefinitions.FILE_WRITE_BINARY_MODE) as new_file:
            new_file.write(data_to_be_written_in_newfile)
    except Exception as exception:
        logger_object.error(exception)
        return False

    logger_object.info("User provided data written successfully to {}".format(file_to_be_rotated_filepath))
    return True


def extract_files_to_directory(zip_compressed_filepath, extract_destination_directory_path, logger_object):
    """
    This function unzips the files to a destination directory
    Args:
        zip_compressed_filepath - the absolute path to the zipped file which the user wants to unzip
        extract_destination_directory_path - the destination directory to which the contents of the zipped file must be unzipped
        logger_object - an object of type Logger which is used by this function to log messages
    """
    # check if zip_compressed_filepath exists
    if os.path.isfile(zip_compressed_filepath) != True:
        logger_object.error("{} is not a valid file".format(zip_compressed_filepath))
        return False

    try:
        with ZipFile(zip_compressed_filepath, SystemDefinitions.FILE_READ_MODE) as zipped_file:
            # unzip the contents of zipped_filepath into extract_destination_filepath
            zipped_file.extractall(extract_destination_directory_path)
    except Exception as exception:
        logger_object.error(exception)
        return False

    logger_object.info("Successfully unzipped files from {} to {}".format(zip_compressed_filepath, extract_destination_directory_path))
    return True


def clear_directory(directory_to_be_cleared, logger_object):
    """
    This function is used to clear the contents of a directory
    Args:
        directory_to_be_cleared - the absolute path of the directory whose contents must be cleared
        logger_object - an object of type Logger which is used by this function to log messages
    """
    if os.path.isdir(directory_to_be_cleared) != True:
        logger_object.error("{} is not a valid directory".format(directory_to_be_cleared))
        return False

    try:
        list_of_files_in_directory = os.listdir(directory_to_be_cleared)
        for filename in list_of_files_in_directory:
            file_path = directory_to_be_cleared + os.path.sep + filename
            # clear the contents of directory_to_be_cleared

            if os.path.isdir(file_path):
                shutil.rmtree(file_path)
            else:
                os.remove(file_path)
    except Exception as exception:
        logger_object.error(exception)
        return False

    logger_object.info("{} directory successfully cleared".format(directory_to_be_cleared))
    return True

def remove_directory(directory_to_be_removed, logger_object):
    """
    This function is used to remove directory
    Args:
        directory_to_be_removed - the absolute path of the directory whose contents must be cleared
        logger_object - an object of type Logger which is used by this function to log messages
    """
    if os.path.isdir(directory_to_be_removed) != True:
        logger_object.error("{} is not a valid directory".format(directory_to_be_removed))
        return False
     
    try:
        shutil.rmtree(directory_to_be_removed)
    
    except Exception as exception:
        logger_object.error(exception)
        return False
    
    logger_object.info("{} directory successfully removed".format(directory_to_be_removed))
    return True


def move_files_in_directory(source_directory_path, destination_directory_path, logger_object):
    """
    This function is used to move all the files present in the source directory to destination directory.
    Args:
        source_directory_path - the absolute path of the directory whose contents are to be moved
        destination_directory_path - the absolute path of the directory to which the contents will be moved
        logger_object - an object of type Logger which is used by this function to log messages
    """
    if os.path.isdir(source_directory_path) != True:
        logger_object.error("{} is not a valid directory".format(source_directory_path))
        return False

    if os.path.isdir(destination_directory_path) != True:
        logger_object.error("{} is not a valid directory".format(destination_directory_path))
        return False

    try:
        list_of_files_in_directory = os.listdir(source_directory_path)
        for filename in list_of_files_in_directory:
            source_filepath = source_directory_path + os.path.sep + filename
            # move from source_directory_path to destination_directory_path
            shutil.move(source_filepath, destination_directory_path)
    except Exception as exception:
        logger_object.error(exception)
        return False

    logger_object.info("Succesfully moved files from {} to {}".format(source_directory_path, destination_directory_path))
    return True


def set_executable_permission_to_file(path_to_file, logger_object):
    # check if the file exists
    if os.path.isfile(path_to_file) != True:
        logger_object.error("{} is not a valid file".format(path_to_file))
        return False

    try:
        # provide executable permission to the file
        os.chmod(path_to_file, EXECUTABLE_PERMISSION)
    except Exception as exception:
        logger_object.error(exception)
        return False

    logger_object.info("Successfully set executable permission to {}".format(path_to_file))
    return True


def move_file(source_filepath, destination_filepath, logger_object):
    # check if the file exists
    if os.path.isfile(source_filepath) != True:
        logger_object.error("{} is not a valid file".format(source_filepath))
        return False

    try:
        shutil.move(source_filepath, destination_filepath)
    except Exception as exception:
        logger_object.error(exception)
        return False

    logger_object.info("Succesfully moved file from {} to {}".format(source_filepath, destination_filepath))
    return True

def copy_file(source_filepath, destination_filepath, logger_object):
    # check if the file exists
    if os.path.isfile(source_filepath) != True:
        logger_object.error("{} is not a valid file".format(source_filepath))
        return False

    try:
        shutil.copy(source_filepath, destination_filepath)
    except Exception as exception:
        logger_object.error(exception)
        return False

    logger_object.info("Succesfully copied file from {} to {}".format(source_filepath, destination_filepath))
    return True

def remove_file_if_exists(filepath, logger_object):
    if os.path.exists(filepath) == True:
        try:
            os.remove(filepath)
        except Exception as exception:
            logger_object.error(exception)
            return False
    else:
        logger_object.info("{} file does not exist".format(filepath))

    return True
