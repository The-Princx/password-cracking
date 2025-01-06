import zipfile
from colorama import Fore, init

init(autoreset=True)

def crack_zip(zip_file, password_list):
    
    try:
        with zipfile.ZipFile(zip_file) as zf:
            for password in password_list:
                try:
                    
                    zf.extractall(pwd=password.encode('utf-8'))
                    print(f"{Fore.GREEN} Password correct: {password}")
                    return  
                except (RuntimeError, zipfile.BadZipFile, zipfile.LargeZipFile):
                    print(f"{Fore.RED} Password incorrect: {password}")
                except Exception as e:
                    print(f"{Fore.YELLOW} Error encountered with password '{password}': {e}")
    except FileNotFoundError:  
        print(f"{Fore.RED} File not found: {zip_file}")
    except Exception as e:
        print(f"{Fore.RED} An error occurred: {e}")
    
    print(f"{Fore.YELLOW} Password not found.")
