import paramiko

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

    print("Success!")

    stdin, stdout, stderr = connection.exec_command("ls /ben")

    exit_code = stdout.channel.recv_exit_status()

    errors = stderr.read().decode().strip()
    output = stdout.read().decode().strip()


    print("Exit Status=",exit_code)
    print("Output=", output)
    print("Errors=",errors)
    connection.close()

except Exception as e:
    print(e)