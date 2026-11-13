from netmiko import ConnectHandler
from paramiko import SSHClient
from scp import SCPClient
import os

device = {
    "host": "192.168.198.131",
    "username": "root",
    "password": "pnet",
    "device_type": "linux"
}

source_file = "R1-2026-11-9.txt"
destination_file = "/var/tmp/backup-1.txt"

connection = ConnectHandler(**device)

try:
    # Establish SCP connection using the existing SSH transport
    with SCPClient(connection.remote_conn.transport) as scp:

        # Check whether destination file exists
        output = connection.send_command(
            f"test -f {destination_file} && echo EXISTS || echo MISSING"
        )

        if output.strip() == "MISSING":
            print("File does not exist, starting upload...")

            scp.put(source_file, destination_file)

            print("Upload completed!")

        else:
            print("File already exists on disk")

finally:
    connection.disconnect()