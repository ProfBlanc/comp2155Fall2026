import paramiko

username = input("Enter username: ")
password = input("Enter your secret/password: ")


hostname = "192.168.198.131"  # different for everyone


port = 22

client = paramiko.SSHClient()

client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    client.connect(
        hostname=hostname,
        username=username,
        password=password,
        port=port
    )

    stdin, stdout, stderr = client.exec_command("ben")


    output = stdout.read().decode()
    error = stderr.read().decode()


    print(output)
    print(error)

except:
    print("Could not connect")
finally:
    client.close()