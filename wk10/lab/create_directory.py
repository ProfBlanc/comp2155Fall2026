from netmiko import ConnectHandler, FileTransfer

router = {
    "device_type": "cisco_ios",
    "host": "192.168.198.12",
    "username": "netauto",
    "password": "LabClass!",
    "secret": "LabClass!"
}

connection = ConnectHandler(**router)

connection.enable()

output = connection.send_command_timing("mkdir disk0:backups")






connection.disconnect()
