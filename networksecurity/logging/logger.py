import logging # Python’s built-in logging library, used to record messages (info, warnings, errors) to files or console. It’s more flexible than print()
import os # Provides functions for interacting with the operating system (like creating folders, joining paths).
from datetime import datetime # To get the current date and time, which is useful for naming log files uniquely.

# Create a log file name with timestam
LOG_FILE=f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log" 

# Define log directory path
logs_path=os.path.join(os.getcwd(),"LOGS") 
# Create directory if it doesn’t exist
os.makedirs(logs_path,exist_ok=True)

# Final log file path
LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logger= logging.getLogger(__name__)
