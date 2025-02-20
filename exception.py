# creating custom exception
import sys 
from src.ml_project_1.logger import logger
# error message detail function will show us where the error occured
def error_message_detail(error_message,error_details:sys): # error message detail function
    _,_,exc_tb = error_details.exc_info() # getting the error details
    file_name = exc_tb.tb_frame.f_code.co_filename # getting the file name
    error_message = "Error occured in python script name [{}] and error message is [{0}] line number [{1}] error message [{2}]".format(file_name,exc_tb.tb_lineno,error_message) # error message
    file_name,exc_tb.tb_lineno,str(error_details) # returning the error message

class CustomException(Exception): # inheriting from Exception class
    def __init__(self, error_message,error_details:sys): #  constructor
        super().__init__(error_message)  #  calling the constructor of the parent class
        self.error_message = error_message_detail(error_message,error_details) #  error message
        logger.error(self.error_message)
        sys.exit(1)
        
    def __str__(self): # this is used to print the error message
        return self.error_message