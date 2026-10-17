import paramiko

host = "192.168.198.11"  # put the host of R1 or R2
username = "netauto"
password = "LabClass!"
port = 22

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect(
    hostname=host,
    password=password,
    username=username,
    port=port
)

stdin, stdout, stderr = client.exec_command("show ip int brief")
print(stdout.read().decode())
client.close()