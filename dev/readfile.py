import os
file = open("config", "r")

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

    # Print the device
    #print(fields)
    #print('The switch mac is: '+ mac + ' his management IP is: ' + management + ' Uplink: ' + uplink + ' hostname: ' + hostname + ' having AP start at port: ' + apstart + ' to ' + apend)

    macsearch = os.popen('/sbin/ip neigh | grep'+ mac)
    print(macsearch.read())

# It is good practice to close the file at the end to free up resources
file.close()