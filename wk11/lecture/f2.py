from lib_to_connect_using_napalm import *

try:
    device.open()
    result = device.is_alive()
    print(result) # dictionary of data
    if result['is_alive']:
        print("connection alive")
    else:
        print("connection NOT alive")
except:
    print("Could not connect")
finally:
    device.close()