import sys # Provides system-related functionality.Here, it’s used to access the current exception details via sys.exc_info()
from networksecurity.logging.logger import logger # importing your custom logger (defined in networksecurity/logging/logger.py).

# Creating a custom exception by extending Python’s built-in Exception class
class NetworkSecurityException(Exception):
    """Purpose: Add extra debugging details (file name, line number) automatically when an error occurs.
    """
    def __init__(self,error_message,error_details:sys): # The original error message (e.g., "division by zero"), passing sys so we can use sys.exc_info() to extract traceback information
        self.error_message=error_message 
        _,_,exc_tb=error_details.exc_info() # It returns a tuple: (exc_type, exc_value, exc_traceback), needed the traceback object (exc_tb), so the first two values are ignored (_, _).

        self.lineno=exc_tb.tb_lineno
        self.file_name=exc_tb.tb_frame.f_code.co_filename

        # Log automatically when exception occurs
        logger.error(self) # self calls your __str__() automatically.It logs the error message into your log file with all formatting applied.

    def __str__(self):
        return (
            f"Error Occured in python script name [{self.file_name}] "
            f"line number [{self.lineno}] "
            f"error message [{str(self.error_message)}]"
        )
