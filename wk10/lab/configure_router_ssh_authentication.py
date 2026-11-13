from netmiko import ConnectHandler


# R2 router
router = {
    "device_type": "cisco_ios",
    "host": "192.168.198.12",
    "username": "netauto",
    "password": "LabClass!",
    "secret": "LabClass!"
}

connection = ConnectHandler(**router)

connection.enable()

commands = [
    "aaa new-model",
    "aaa authentication login default local",
    "line vty 0 4",
    "login authentication default",
    "transport input ssh"
]

output = connection.send_config_set(commands)

print(output)

connection.disconnect()
