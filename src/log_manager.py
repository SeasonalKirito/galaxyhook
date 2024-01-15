import json
import os

from src.ansi import Fore
import os

class log_manager():
    def __init__(self):
        self.DEEP_DEBUG = False

    def _deep_debug(self, message: str= None):
        if self.DEEP_DEBUG:
            return(f"{Fore.YELLOW}[DEEP DEBUG] {message}{Fore.RESET}")
        else:
            pass

    def _deep_log(self, filename: str, message: str):
        logs_folder = "src/logs/"
        log_file_path = os.path.join(logs_folder, filename)

        if os.path.exists(log_file_path):
            with open(log_file_path, "a") as log_file:
                log_file.write(message + "\n")
        else:
            with open(log_file_path, "w") as log_file:
                log_file.write(message + "\n")
