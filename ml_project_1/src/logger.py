from logging import getLogger, StreamHandler, Formatter, INFO, DEBUG, FileHandler
import os

class Logger:
    def __init__(self, name: str, log_file: str = None):
        self.logger = getLogger(name)
        self.logger.setLevel(INFO)

        # Create console handler and set level to debug
        ch = StreamHandler()
        ch.setLevel(DEBUG)

        # Create formatter
        formatter = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)

        # Add console handler to logger
        self.logger.addHandler(ch)

        # If a log file is specified, create a file handler
        if log_file:
            if not os.path.exists(os.path.dirname(log_file)):
                os.makedirs(os.path.dirname(log_file))
            fh = FileHandler(log_file)
            fh.setLevel(INFO)
            fh.setFormatter(formatter)
            self.logger.addHandler(fh)

    def debug(self, message: str):
        self.logger.debug(message)

    def info(self, message: str):
        self.logger.info(message)

    def warning(self, message: str):
        self.logger.warning(message)

    def error(self, message: str):
        self.logger.error(message)

    def critical(self, message: str):
        self.logger.critical(message)

# Example usage
# logger = Logger(__name__, log_file='logs/project.log')
# logger.info('This is an info message')