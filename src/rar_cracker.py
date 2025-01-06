import rarfile

def crack_rar(rar_file, password_list):
    with rarfile.RarFile(rar_file) as rf:
        for password in password_list:
            try:
                rf.extractall(pwd=password)
                print(f"\033[1;32mPassword correct: {password}")
                return
            except rarfile.BadRarFile:
                print(f"\033[1;31mPassword incorrect: {password}")
    print("Password not found.")