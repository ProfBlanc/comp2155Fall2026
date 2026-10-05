import paramiko
import time
host = "192.168.198.130"
username = "root"
password = "pnet"

connection = paramiko.SSHClient()

connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    connection.connect(
        hostname=host,
        username=username,
        password=password
    )
    print("Successful Connection")

    shell = connection.invoke_shell()
    time.sleep(3)  # creates delay to allow connection to be established

    command = "pwd\n"
    shell.send(command)
    time.sleep(1)
    if shell.recv_ready():
        output = shell.recv(1024).decode()
        print(output)

    shell.close()
    connection.close()

except Exception as e:
    print(e)