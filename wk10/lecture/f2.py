from netmiko import ConnectHandler
device = {
    "host": "192.168.198.11",
    "username": "netauto",
    "password": "LabClass!",
    "device_type": "cisco_ios",
    "secret": "LabClass!"
}

connection = ConnectHandler(**device)

connection.enable()

commands = [
    "int loopback 0",
    "ip address 1.1.1.1 255.255.255.255",
    'exit',
    'username netmiko secret cisco'
]

output = connection.send_config_set(commands)
print(output)
connection.save_config()