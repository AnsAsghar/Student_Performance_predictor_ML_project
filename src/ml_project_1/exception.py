import sys

class CustomException(Exception):
    def __init__(self, message, error_detail: sys):
        super().__init__(message)
        self.error_message = message  # Store the message in error_message attribute
        self.error_detail = error_detail

    def __str__(self):
        return f"{self.error_message} - {self.error_detail}"
