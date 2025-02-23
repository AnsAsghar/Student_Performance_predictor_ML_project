import sys
from src.ml_project_1.logger import logging

# error message detail function will show us where the error occured
def error_message_detail(error_message, error_details:sys):
    if hasattr(error_details, 'exc_info'):
        _, _, exc_tb = error_details.exc_info()
        if exc_tb is not None:
            file_name = exc_tb.tb_frame.f_code.co_filename
            error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
                file_name, exc_tb.tb_lineno, str(error_message))
            return error_message
    return str(error_message)

class CustomException(Exception):
    def __init__(self, error_message, error_details:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_details)
        logging.error(self.error_message)

    def __str__(self):
        return self.error_message
