import json

from wk11.lecture.lib_to_connect_using_napalm import *
import time
"""
Tracking traffic on a device
"""

try:
    device.open()

    snapshot_one = device.get_interfaces_counters()
    time.sleep(5)
    snapshot_two = device.get_interfaces_counters()

    print(json.dumps(snapshot_one, indent=4))

    for interface in snapshot_one.keys():
        if interface not in snapshot_two:
            continue # skip interface if not found in snapshot two
        print(interface)

        transmitted_packets = snapshot_two[interface]["tx_octets"] - snapshot_one[interface]["tx_octets"]

        print("transmitted from past 5 seconds is", transmitted_packets)
except Exception as e:
    print(e)
finally:
    device.close()