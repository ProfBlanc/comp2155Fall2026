import paramiko
import time
host = "192.168.198.130"
username = "root"
password = "pnet"

connection = paramiko.SSHClient()
connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
shell = None


def read_all_available(channel):
    output = ""

    while channel.recv_ready():
        data_returned = channel.recv(1024)
        if not data_returned:
            break
        output += data_returned.decode()

    return output

try:
    connection.connect(
        hostname=host,
        username=username,
        password=password
    )
    print("Successful Connection")

    shell = connection.invoke_shell()

    shell.sendall("pwd\n")
    time.sleep(3)
    output = read_all_available(shell)
    print(output)

except Exception as e:
    print(e)
finally:
    if shell is not None:
        shell.close()

    connection.close()