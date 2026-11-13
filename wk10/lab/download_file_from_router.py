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

ft = FileTransfer(
    connection,
    source_file="backup.cfg",
    dest_file="downloaded_backup.cfg",
    file_system="disk0:backups",
    direction="get"
)

# Enable SCP on the Cisco device
ft.enable_scp()

# Establish SCP connection
ft.establish_scp_conn()


transfer_result = ft.transfer_file()

print(transfer_result)

# output = connection.send_command_timing("delete disk0:old_backup.cfg")


connection.disconnect()
