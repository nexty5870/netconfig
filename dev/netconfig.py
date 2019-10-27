import os
from termcolor import colored

clear = lambda: os.system('cls')

header = "\
 _   _      _                          __ _       \n\
| \ | |    | |                        / _(_)      \n\
|  \| | ___| |_ ______ ___ ___  _ __ | |_ _  __ _ \n\
| . ` |/ _ \ __|______/ __/ _ \| '_ \|  _| |/ _` |\n\
| |\  |  __/ |_      | (_| (_) | | | | | | | (_| |\n\
\_| \_/\___|\__|      \___\___/|_| |_|_| |_|\__, |\n\
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
    print(colored('*'*30, 'yellow'))
    print()

def colorize(string, color):
    if not color in colors: return string
    return colors[color] + string + '\033[0m'


def netmap_mac():
    clear()
    header_function()
    print('Start by scanning the mac address of the device: ')
    print('When finish press <CTRL+D>')
    mac = []
    while True:
        try:
            line = input()
            mac.append(line)
        except EOFError:
            break

    print(mac)
    netmap_ip()

def netmap_ip():
    clear()
    header_function()
    print('Enter the management IP for each MAC you scanned: ')
    print('When finish press <CTRL+D>')
    ips = []
    while True:
        try:
            line = input()
            ips.append(line)
        except EOFError:
            break

    print ('This is netmap_ip()')
    print(ips)
    netmap_uplink()

def netmap_uplink():
    clear()
    header_function()
    print('Enter each uplink for the switch you scanned: ')
    print('When finish press <CTRL+D>')
    uplink = []
    while True:
        try:
            line = input()
            uplink.append(line)
        except EOFError:
            break

    print ('This is netmap_uplink()')
    print(uplink)
    netmap_apstart()

def netmap_apstart():
    clear()
    header_function()
    print('Enter the AP port start for each switch you scanned: ')
    print('When finish press <CTRL+D>')
    apstart = []
    while True:
        try:
            line = input()
            apstart.append(line)
        except EOFError:
            break

    print ('This is netmap_apstart()')
    print(apstart)
    netmap_apend()

def netmap_apend():
    clear()
    header_function()
    print('Enter the AP port end for each switch you scanned: ')
    print('When finish press <CTRL+D>')
    apend = []
    while True:
        try:
            line = input()
            apend.append(line)
        except EOFError:
            break

    print ('This is netmap_apend()')
    print(apend)
    netmap_filecreation()

def netmap_filecreation():
    clear()
    header_function()
    input('Netmap process finish. Press [Enter] to create the file')
    print (mac,ips,uplink,apstart,apend)

def setup():
    header_function()
    print('This is the menu Setup')
    input('Press [Enter] for menu')
    menu()

def exit():
    clear()
    input('Exiting NetConfig. Press [Enter]')


def menu():
    clear()
    header_function()
    print('1. Start Netmap')
    print('2. Setup')
    print('3. Exit')
    choice = input('Enter your choice: ')
    if choice == '1':
        netmap_mac()
    elif choice == '2':
        setup()
    elif choice == '3':
        exit()
    else:
        clear()
        input('Unsupported input, Press [Enter] for menu')
        menu()

menu()