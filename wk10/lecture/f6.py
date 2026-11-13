from netmiko import ConnectHandler
from netmiko import FileTransfer

device = {
    "host": "192.168.198.11",
    "username": "netauto",
    "password": "LabClass!",
    "device_type": "cisco_ios",
    "secret": "LabClass!"
}

connection = ConnectHandler(**device)

source_file = "R1-2026-11-9.txt"
destination_file = "backup-1.txt"

connection.enable()

ft = FileTransfer(
    ssh_conn=connection,
    source_file=source_file,
    dest_file=destination_file,
    file_system="disk0:"
)
# Enable SCP on the Cisco device
ft.enable_scp()

# Establish SCP connection
ft.establish_scp_conn()

if not ft.check_file_exists():
    print("File does not exists, starting upload process")
    ft.transfer_file()
    print("Upload completed")
else:
    print("File already exists on disk")
    if ft.verify_file():
        print("Confirmed file exists")
    else:
        print("File couldn't be found. Checkout the issue.")

connection.disconnect()