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
    print("Successful Connection")

    commands = "hostname,whoami,pwd,uptime,df -h".split(",")

    for command in commands:
        stdin, stdout, stderr = connection.exec_command(command=command)
        output = stdout.read().decode()
        print("Command Ran =", command)
        print("Commad Output =", output)
        print("*" * 20)
    connection.close()

except Exception as e:
    print(e)