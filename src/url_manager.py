import requests
import datetime

from src.ansi import Fore
from src.log_manager import log_manager

class url_manager():
    def __init__(self):
        self.DEBUG = True
        self.log_manager = log_manager()

    def _get_time(self):
        return str(datetime.datetime.now().strftime('%H:%M:%S'))
    
    def _extract_webhook_id(self, webhook_url: str=None):
        if webhook_url is None:
            return self._debug("No webhook url provided")
        else:
            webhook_url = webhook_url.replace("https://discord.com/api/webhooks/", "")
            webhook_url = webhook_url.replace("/", "][")
            return str("[" + webhook_url)

    def _success(self, message: str= None):
        return(f"{Fore.GREEN}[SUCCESS] {message}{Fore.RESET}")
    
    def _error(self, message: str= None):
        return(f"{Fore.RED}[ERROR] {message}{Fore.RESET}")
    
    def _info(self, message: str= None):
        return(f"{Fore.CYAN}[INFO] {message}{Fore.RESET}")

    def _debug(self, message: str= None):
        if self.DEBUG:
            print(f"{Fore.YELLOW}[DEBUG] {message}{Fore.RESET}")
        else:
            pass

    def _rename(self, webhook_url: str=None, name: str=None):
        if webhook_url is None:
            return self._debug("No webhook url provided")
        if name is None:
            return self._debug("No name provided")
        requests.patch(webhook_url, json={"name": name})

    def _delete(self, webhook_url: str=None):
        if webhook_url is None:
            return self._debug("No webhook url provided")
        requests.delete(webhook_url)

    def _send(self, webhook_url: str=None, message: str=None):
        if webhook_url is None:
            return self._debug("No webhook url provided")
        if message is None:
            return self._debug("No message provided")
        
        webhook_extracted_id = self._extract_webhook_id(webhook_url)
        print(self.log_manager._deep_debug(f"[{self._get_time()}] [{webhook_extracted_id}] SENT: {message}"))
        self.log_manager._deep_log(f"{webhook_extracted_id}.log", f"[{self._get_time()}] [{webhook_extracted_id}] SENT: [{message}]")

        requests.post(webhook_url, json={"content": message})

    def _spam(self, webhook_url: str=None, message: str=None, amount: int=None):
        if webhook_url is None:
            return self._debug("No webhook url provided")
        if message is None:
            return self._debug("No message provided")
        if amount is None:
            return self._debug("No amount provided")
        for _ in range(amount):
            requests.post(webhook_url, json={"content": message})

    def _avatar(self, webhook_url: str=None, avatar_url: str=None):
        if webhook_url is None:
            return self._debug("No webhook url provided")
        if avatar_url is None:
            return self._debug("No avatar url provided")
        requests.patch(webhook_url, json={"avatar_url": avatar_url})

    def _integrity_check(self, webhook_url: str=None):
        if webhook_url is None:
            return self._debug("No webhook url provided")
        r = requests.get(webhook_url)
        if r.status_code == 200:
            return True
        else:
            return False

url_manager = url_manager()