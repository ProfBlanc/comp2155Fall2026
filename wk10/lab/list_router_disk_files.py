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

commands = [
    "dir disk0:",
    "dir disk1:"
]

for command in commands:

    print(f"\n===== {command} =====")

    output = connection.send_command(command)

    print(output)

connection.disconnect()
