from wk11.lecture.lib_to_connect_using_napalm import *
"""
Check details of a router and determine if information is missing
"""

try:
    device.open()
    interfaces = device.get_interfaces()

    unconfigured_interfaces = set()

    for interface, details in interfaces.items():
        print(interface, details)
        for value in details.values():
            if len(str(value)) == 0:
                unconfigured_interfaces.add(interface)

    print("Interfaces that need attention")
    print(unconfigured_interfaces)

except Exception as e:
    print(e)
finally:
    device.close()