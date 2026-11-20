import json

from jinja2.utils import missing

from wk11.lecture.lib_to_connect_using_napalm import *
import time
"""
Check details of a router and determine if information is missing
"""

try:
    device.open()
    interfaces = device.get_interfaces()

    unconfigured_interface_details = dict()

    for interface, details in interfaces.items():
        print(interface, details)
        for detail, value in details.items():
            if len(str(value)) == 0:

                if interface not in unconfigured_interface_details:
                    unconfigured_interface_details[interface] = []

                unconfigured_interface_details[interface].append(detail)

    print("Interfaces that need attention")
    print(json.dumps(unconfigured_interface_details, indent=4))

except Exception as e:
    print(e)
finally:
    device.close()