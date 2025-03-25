import os
import time
import platform
from src.utils import clear_console, read_passwords
from src.zip_cracker import crack_zip
from src.rar_cracker import crack_rar
from colorama import init, Fore, Style

init(autoreset=True)

def logo():
    
    lg = '''
  ╔═══╗────────────╔═══╗───────────╔╗── 
  ║╔═╗║────────────║╔═╗║───────────║║── 
  ║╚═╝║╔══╗╔══╗╔══╗║║─╚╝╔═╗╔══╗╔══╗║║╔╗ 
  ║╔══╝║╔╗║║══╣║══╣║║─╔╗║╔╝║╔╗║║╔═╝║╚╝╝ 
  ║║───║╔╗║╠══║╠══║║╚═╝║║║─║╔╗║║╚═╗║╔╗╗ 
  ╚╝───╚╝╚╝╚══╝╚══╝╚═══╝╚╝─╚╝╚╝╚══╝╚╝╚╝ 
    '''
    print(Fore.RED + lg)
    print(Fore.CYAN + "        Main Owner: @The_Princx")
    print(Fore.GREEN + "−−−−−−−−−−−−−−−−−−−−−−−−−−−--−−−−−−−−−−−−−−")
    print(Style.DIM + " What file do you want to crack?")
    print(Fore.BLUE + " 1. zip file")
    print(Fore.BLUE + " 2. rar file")
    print(Fore.BLUE + " 3. 7z file (Coming soon)")  
    print(Fore.GREEN + "−−−−−−−−−−−−−−−−−−−−--−−−−−−−−−−−−−−−−−−−−−")


def get_password_file():
    password_file_path = os.path.join("data", "password.txt")
    if os.path.exists(password_file_path):
        use_existing = input(" Use existing 'password.txt'? (y/n): ").strip().lower()
        print(Fore.GREEN + "−−−−−−−−−−−−−−−−−−−−−--−−−−−−−−−−−−−−−−−−−−")
        time.sleep(3)
        if use_existing == 'y':
            return password_file_path

    return input("Enter the path of your password list file: ").strip()


def main():
   
    clear_console()
    logo()


    user_input = input(Fore.GREEN + " Select the option: ").strip()

  
    if user_input == '1': 
        file_path = input(" Enter the path of the ZIP file: ").strip()
        password_file = get_password_file()
        password_list = read_passwords(password_file)
        crack_zip(file_path, password_list)

    elif user_input == '2':  
        file_path = input(" Enter the path of the RAR file: ").strip()
        password_file = get_password_file()
        password_list = read_passwords(password_file)
        crack_rar(file_path, password_list)

    elif user_input == '3': 
        print(Fore.YELLOW + "7z file cracking is coming soon. Stay tuned!")

    else:
        print(Fore.RED + " Invalid option selected. Please try again.")


if __name__ == "__main__":
    main()
