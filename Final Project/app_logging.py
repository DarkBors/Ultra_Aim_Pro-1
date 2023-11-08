# logging.py

import logging
from datetime import datetime

# Configure the logger
logger = logging.getLogger('application_logger')
logger.setLevel(logging.DEBUG)  # Set the logging level

# Create a file handler with a timestamped log file name
current_time = datetime.now().strftime("App_log_%d%m%Y_%H%M.log")  # Adjust the format here
fh = logging.FileHandler(current_time, encoding='utf-8')  # Specify UTF-8 encoding here
fh.setLevel(logging.DEBUG)

# Create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

# Create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

# Define custom log levels without emojis to avoid encoding issues
logging.addLevelName(logging.INFO, "INFO")
logging.addLevelName(logging.WARNING, "WARNING")
logging.addLevelName(logging.DEBUG, "DEBUG")
logging.addLevelName(logging.CRITICAL, "CRITICAL")
