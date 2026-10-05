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
    # low-level return
    # paramiko is a low-level language module
    # stdin = input
    # stout = output
    # sterr = error

    stdin, stdout, stderr = connection.exec_command("hostname")

    #print(stdout)
#    output = stdout.read() # returns bytes
    output = stdout.read().decode().strip()
    print(output)
    # print() => calls inner methods that we are not aware of

    errors = stderr.read().decode().strip()
    print("Errors=",errors)
    connection.close()

except Exception as e:
    print(e)