from netmiko import ConnectHandler

import time

start = time.perf_counter()

device = {
    "host": "192.168.198.11",
    "username": "netauto",
    "password": "LabClass!",
    "device_type": "cisco_ios",
    "secret": "LabClass!"
}

connection = ConnectHandler(**device)
connection.disconnect()
end = time.perf_counter()
print("Execution Time =", end-start, "seconds")

