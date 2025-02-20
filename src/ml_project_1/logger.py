import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d')}.log" # log file name
log_dir = os.path.join(os.getcwd(), "logs") # log directory path
os.makedirs(log_dir, exist_ok=True) # create the directory if it does not exist

LOG_FILE_PATH = os.path.join(log_dir, LOG_FILE) # log file path

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Create a custom logger
logger = logging.getLogger(__name__)

# Create handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler(LOG_FILE_PATH)
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)

# Create formatters and add it to handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

# Example usage
logger.warning('This is a warning')
logger.error('This is an error')