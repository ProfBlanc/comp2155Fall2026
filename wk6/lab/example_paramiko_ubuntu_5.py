import time

import paramiko

hostname = "192.168.198.131"  # different for everyone
username = "root"  # same for everyone
password = "pnet"
port = 22

client = paramiko.SSHClient()

client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

shell = None

try:
    client.connect(
        hostname=hostname,
        username=username,
        password=password,
        port=port
    )

    shell = client.invoke_shell()

    shell.send("ls -la\n")

    time.sleep(0.5)

    output = ""

    while shell.recv_ready():
        output += shell.recv(1024).decode()

    print(output)


except:
    print("Could not connect")
finally:
    if shell is not None:
        shell.close()
    if client is not None:
      client.close()