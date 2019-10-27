from jinja2 import Template


file_location_root= 'C:/Users/quent/OneDrive/Documents/Python Scripts/netconfig'
apstart = '1'
apend = '15'

ports = [
    {'name': apstart + ' '+ 'to ' + apend,
     'mode': 'AP',
     'vlan': 1000,
     'state': 'enable'},
    {'name': '2',
     'mode': 'none',
     'vlan': 1000,
     'state': 'enable'},
    {'name': '24',
     'mode': 'Uplink',
     'vlan': '100,1000',
     'state': 'enable'}
]

with open(file_location_root+'/dev/vendor/hp/conditional.j2') as f:
    config_in = Template(f.read())

config_out = config_in.render(ports=ports)

print('*' * 30)
print()
print('Script generator creation started')
print(config_out)