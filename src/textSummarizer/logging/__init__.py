import os
import logging
import sys

logging_str="[%(asctime)s:%(levelname)s:%(module)s:%(message)s"
log_dir="logs"
log_filepath=os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir,exist_ok=True)


# Configure the logging settings
logging.basicConfig(
    level=logging.INFO,  # Set the logging level to INFO. This will capture INFO, WARNING, ERROR, and CRITICAL logs.
    format=logging_str,  # Specify the format of the log messages using the logging_str variable.
    handlers=[
        logging.FileHandler(log_filepath),  # Log messages to a file specified by log_filepath.
        logging.StreamHandler(sys.stdout)   # Also output log messages to the console (standard output).
    ]
)

# Create or retrieve a logger named "textSummarizerLogger"
logger = logging.getLogger("textSummarizerLogger")
