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

output = connection.send_command_timing("rmdir disk0:backups")
# output = connection.send_command_timing("delete disk0:backups/backup.cfg")
print(output)

# confirm action
response = connection.send_command_timing("\n")
print(response)

# Confirm deletion
response = connection.send_command_timing("\n")
print(response)



connection.disconnect()
