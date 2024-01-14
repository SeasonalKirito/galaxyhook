import requests
import json
import os
import time

from src.url_manager import url_manager
from src.ansi import Fore

TERMINAL_LOGO = f"""{Fore.MAGENTA}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⡴⢧⣀⠀⠀⣀⣠⠤⠤⠤⠤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⠏⢀⡴⠊⠁⠀⠀⠀⠀⠀⠀⠈⠙⠦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣰⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢶⣶⣒⣶⠦⣤⣀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣟⠲⡌⠙⢦⠈⢧⠀[ github.com/SeasonalKirito ]
⠀⠀⠀⣠⢴⡾⢟⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡴⢃⡠⠋⣠⠋⠀[ _seasonal_ ]
⠐⠀⠞⣱⠋⢰⠁⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⠤⢖⣋⡥⢖⣫⠔⠋⠀⠀⠀
⠈⠠⡀⠹⢤⣈⣙⠚⠶⠤⠤⠤⠴⠶⣒⣒⣚⣩⠭⢵⣒⣻⠭⢖⠏⠁⢀⣀⠀⠀⠀⠀
⠠⠀⠈⠓⠒⠦⠭⠭⠭⣭⠭⠭⠭⠭⠿⠓⠒⠛⠉⠉⠀⠀⣠⠏⠀⠀⠘⠞⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⢤⣀⠀⠀⠀⠀⠀⠀⣀⡤⠞⠁⠀⣰⣆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⠿⠀⠀⠀⠀⠀⠈⠉⠙⠒⠒⠛⠉⠁⠀⠀⠀⠉⢳⡞⠉⠀⠀⠀⠀⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{Fore.RESET}"""

TERMINAL_OPTIONS = f"""{Fore.MAGENTA}
[1] Send message
[2] Delete webhook
[3] Rename webhook
[4] Spam webhook
[5] Change avatar
[6] Logout
{Fore.RESET}"""

class galaxyhook():
    def __init__(self, webhook_url: str=None):
        self.url_manager = url_manager

        self.TERMINAL_LOGO = TERMINAL_LOGO
        self.TERMINAL_OPTIONS = TERMINAL_OPTIONS

        self.DEBUG = True
        self.CONNECTED_WEBHOOK = None
        self.BASE_WEBHOOK_URL = "https://discord.com/api/webhooks/"
        self._login(webhook_url)
        self._startup()
    
    def _clear(self, reset_terminal: bool=True):
        if reset_terminal:
            os.system("cls || clear")
            print(self.TERMINAL_LOGO)
            print(self.TERMINAL_OPTIONS)
        else:
            os.system("cls || clear")

    def _login(self, webhook_url: str=None):
        self._clear(reset_terminal=False)
        print(self.TERMINAL_LOGO)
        webhook_url = input(f"{Fore.CYAN}Enter webhook url: ")

        if webhook_url.startswith("https://discord.com/api/webhooks/"):
            pass
        else:
            print(self.url_manager._debug("Webhook url does not include https://discord.com/api/webhooks/"))
            time.sleep(2.5)
            return self._login()
        
        if webhook_url is None:
            print(self.url_manager._debug("No webhook url provided"))
            time.sleep(2.5)
            return self._login()
        
        integrity_check = self.url_manager._integrity_check(webhook_url=webhook_url)
        if integrity_check is False:
            self._clear(reset_terminal=False)
            print(self.TERMINAL_LOGO)

            print(f"{Fore.RED}Webhook is invalid, logging out...")
            time.sleep(2.5)
            return self._logout()
        else:
            self._clear(reset_terminal=False)
            print(self.TERMINAL_LOGO)
            
            print(f"{Fore.GREEN}Webhook is valid, logging in...")
            self.CONNECTED_WEBHOOK = webhook_url
            time.sleep(2.5)

    def _logout(self):
        self.CONNECTED_WEBHOOK = None
        self._login()
        self._startup()
    
    def _get(self):
        return self.CONNECTED_WEBHOOK
    
    def _startup(self):
        self._clear(reset_terminal=False)
        print(self.TERMINAL_LOGO)
        print(self.TERMINAL_OPTIONS)
        while True:
            option = input(f"{Fore.BLUE}Enter option: ")
            integrity_check = self.url_manager._integrity_check(webhook_url=self._get())
            if integrity_check is False:
                print(f"{Fore.RED}Webhook is invalid, logging out...")
                time.sleep(2.5)
                self._logout()
                break
            else:
                pass
            if option == "1":
                message = input(f"{Fore.BLUE}Enter message: ")
                self.url_manager._send(webhook_url=self._get(), message=message)
                self._clear(reset_terminal=True)
            elif option == "2":
                self.url_manager._delete(webhook_url=self._get())
                self._logout()
            elif option == "3":
                name = input(f"{Fore.BLUE}Enter name: ")
                self.url_manager._rename(webhook_url=self._get(), name=name)
                self._clear(reset_terminal=True)
            elif option == "4":
                message = input(f"{Fore.BLUE}Enter message: ")
                amount = int(input(f"{Fore.BLUE}Enter amount: "))
                self.url_manager._spam(webhook_url=self._get(), message=message, amount=amount)
                self._clear(reset_terminal=True)
            elif option == "5":
                avatar_url = input(f"{Fore.BLUE}Enter avatar url: ")
                self.url_manager._avatar(webhook_url=self._get(), avatar_url=avatar_url)
                self._clear(reset_terminal=True)
            elif option == "6":
                self._logout()
                break
            else:
                self.url_manager._debug("Invalid option")

if __name__ == "__main__":
    webhook = galaxyhook()