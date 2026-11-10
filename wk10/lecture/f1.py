from netmiko import ConnectHandler
import logging
#logging.basicConfig(level=logging.DEBUG, filename="test.log")
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger("netmiko")
device = {
    "host": "192.168.198.11",
    "username": "netauto",
    "password": "LabClass!",
    "device_type": "cisco_ios",
    "secret": "LabClass!"
}
connection = ConnectHandler(**device)

connection.enable()

output = connection.send_command("show run")

#print(connection.find_prompt())
device_name = connection.find_prompt()[:-1]
print(device_name)
filename = f"{device_name}"
file_extension = ".txt"
from datetime import datetime
now = datetime.now()
month = now.month  # 1-12
day = now.day
year = now.year

filename += f"-{year}-{month}-{day}{file_extension}"
print(filename)

with open(filename, "w") as fo:
    fo.write(output)
connection.disconnect()