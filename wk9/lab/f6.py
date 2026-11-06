from netmiko import ConnectHandler


device = {
    "host": "192.168.198.11",
    "username": "netauto",
    "password": "LabClass!",
    "device_type": "cisco_ios",
    "secret": "LabClass!"
}

connection = ConnectHandler(**device)

print(connection.find_prompt())
connection.enable()
print(connection.find_prompt())

connection.disable_paging()
print(connection.send_command("show version"))

connection.disconnect()
