import requests
from src.ansi import Fore

class url_manager():
    def __init__(self):
        self.DEBUG = True

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