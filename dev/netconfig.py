import os
from termcolor import colored

clear = lambda: os.system('cls')

header = "\
 _   _        _    _____                 __  _\n\
| \ | |      | |  /  __ \               / _|(_)\n\
|  \| |  ___ | |_ | /  \/  ___   _ __  | |_  _   __ _\n\
| . ` | / _ \| __|| |     / _ \ | '_ \ |  _|| | / _` |\n\
| |\  ||  __/| |_ | \__/\| (_) || | | || |  | || (_| |\n\
\_| \_/ \___| \__| \____/ \___/ |_| |_||_|  |_| \__, |\n\
                                                 __/ |\n\
                                                |___/ \n"
colors = {
    'blue': '\033[94m',
    'pink': '\033[95m',
    'green': '\033[92m',
}

def header_function():
    clear()
    print(colored(header, 'blue'))
    print(colored('version 0.1', 'green' ))

def colorize(string, color):
    if not color in colors: return string
    return colors[color] + string + '\033[0m'

def netmap():
    header_function()
    print('This is Netmap')
    input('Press Enter for menu')
    menu()

def netmap_mac():
    clear()

def setup():
    header_function()
    print('This is the menu Setup')
    input('Press Enter for menu')
    menu()

def exit():
    clear()
    input('Exiting NetConfig. Press [Enter]')


def menu():
    clear()
    print(colored(header, 'blue'))
    print(colored('version 0.1', 'green' ))
    print('1. Start Netmap')
    print('2. Setup')
    print('3. Exit')
    choice = input('Enter your choice: ')
    if choice == '1':
        netmap()
    elif choice == '2':
        setup()
    elif choice == '3':
        exit()
    else:
        clear()
        input('Unsupported input, Press [Enter] for menu')
        menu()

menu()