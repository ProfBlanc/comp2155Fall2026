import json

from lib_to_connect_using_napalm import *

try:
    device.open()

    users = device.get_users()
    print(json.dumps(users, indent=4))

    interfaces = device.get_interfaces()
    print(json.dumps(interfaces, indent=4))

    ips = device.get_interfaces_ip()
    print(json.dumps(ips, indent=4))

    arp_table = device.get_arp_table()
    print(json.dumps(arp_table, indent=4))


except Exception as e:
    print("Could not connect")
    print(e)
finally:
    device.close()