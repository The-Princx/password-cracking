import os
import sys

def clear_console():

    osystem = sys.platform
    if osystem == "linux" or osystem == "darwin": 
        os.system("clear")
    else:
        os.system("cls")

def read_passwords(password_file):
    with open(password_file, 'r') as f:
        return [line.strip() for line in f.readlines()]