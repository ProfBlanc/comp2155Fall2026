from netmiko import ConnectHandler
router = {
    "device_type": "cisco_ios",
    "host": "192.168.198.12",
    "username": "netauto",
    "password": "LabClass!",
    "secret": "LabClass!"
}


connection = ConnectHandler(**router)

connection.enable()
output = connection.send_command("show file systems")

print(output)

connection.disconnect()
