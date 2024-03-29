import os
from bs4 import BeautifulSoup
import requests
import subprocess

file = open("config", "r")

#maclist formater
def str_grouper(n, iterable):
     args = [iter(iterable)] * n
     for part in zip(*args): #itertools.izip in 2.x for efficiency.
         yield "".join(part)

# Repeat for each song in the text file
for line in file:
    # Let's split the line into an array called "fields" using the "tab" as a separator:

    fields = line.split("\t")
    # line = line.rstrip()
    # line = line.split('#', 1)[0]

    # and let's extract the data:
    mac = fields[0]
    management = fields[1]
    uplink = fields[2]
    hostname = fields[3]
    apstart = fields[4]
    apend = fields[5]

    # Convert the mac list to string
    maclist = ''.join(mac)
    maclistformated = ':'.join(str_grouper(2,mac))

    #print(maclist)

    source = requests.get('https://hwaddress.com/?q=' + maclist).text
    soup = BeautifulSoup(source, 'lxml')
    vendor = soup.find('div', class_='table-responsive')
    company = vendor.a.text
    defineip = {}
    defineip = '/sbin/ip neigh | sed -nr ' + maclistformated +' "/Is/ dev.*$//p"'
    subprocess.call(defineip,shell=True)
    print('Mac found vendor is: '+company)
    while company == 'Ruckus Wireless':
        print('Ruckus subroutine')
        print(defineip)
        print('The switch mac is: ' + maclistformated + ' his management IP is: ' + management + ' Uplink: ' + uplink + ' hostname: ' + hostname + ' having AP start at port: ' + apstart + ' to ' + apend)
        break
    else:
        print('Vendor not supported')

    # Print the device
    #print('The switch mac is: '+ mac + ' his management IP is: ' + management + ' Uplink: ' + uplink + ' hostname: ' + hostname + ' having AP start at port: ' + apstart + ' to ' + apend)

    #macsearch = os.popen('/sbin/ip neigh | grep'+ mac)
    #print(macsearch.read())



# It is good practice to close the file at the end to free up resources
file.close()