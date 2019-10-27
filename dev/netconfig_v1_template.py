from jinja2 import Template

file_location_root= 'C:/Users/quent/OneDrive/Documents/Python Scripts/netconfig'
management_ip = '172.19.255.10'
management_mask = '255.255.255.0'
hostname = 'Test-Jinja2'
ovi_server = '172.27.1.1'
vlans = [
    {'name:': 'Guest_Wireless',
     'vlan_var': 1000},
    {'name:': 'Management IP',
     'vlan_var' : 100,
     'ip_var' : management_ip,
     'mask_var' : management_mask }

]

### Vlan template test, --- to be cleared ---
#with open('C:/Users/qdaems/Documents/script/netconfig/dev/vendor/hp/vlan_template.j2') as f:
#    vlan_in_template = Template(f.read())
###

with open (file_location_root+'/dev/vendor/hp/svi_template.j2') as f:
    svi_in_template = Template(f.read())

with open(file_location_root+'/dev/vendor/hp/config_loop.j2') as f:
    config_in = Template(f.read())

config_out = config_in.render(hostname=hostname,vlans=vlans,ovi_server=ovi_server)

### SVI template test, --- to be cleared ---
#svi_output = svi_in_template.render(hostname=hostname, ip=management_ip, mask=management_mask)
###

print('*' * 30)
print()
#print('!SVI Output from SVI template')
#print(svi_output)
print('Script generator creation started')
print('*' * 30)
print(config_out)
print('*' * 30)
print()
