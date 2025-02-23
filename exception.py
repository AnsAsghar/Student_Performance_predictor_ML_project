# creating custom exception
import sys 
from src.ml_project_1.logger import logger
# error message detail function will show us where the error occured
def error_message_detail(error_message, error_details:sys):
    _,_,exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error_message))
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_details:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_details)
        logger.error(self.error_message)

    def __str__(self):
        return self.error_message