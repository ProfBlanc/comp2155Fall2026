"""
Using netmiko, create an application that asks the user for a command to
execute, save the command to a timestamped output
Hard-code the connection details
"""
from netmiko import ConnectHandler

device = {
    "host": "192.168.198.131",
    "username": "root",
    "password": "pnet",
    "device_type": "linux",
}

connection = ConnectHandler(**device)

command = input("Enter a command to execute: ")

output = connection.send_command(command)

fo = open(f"{command}.txt", "w")
fo.write(output)
fo.close()

connection.disconnect()
