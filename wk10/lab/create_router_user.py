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

# Create a local user
commands = [
    "username john privilege 15 secret MyPassword123"
]

output = connection.send_config_set(commands)

print(output)

connection.disconnect()
