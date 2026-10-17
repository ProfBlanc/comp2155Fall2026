import paramiko

hostname = "192.168.198.131"  # different for everyone
username = "root"  # same for everyone
password = "pnet"
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

    stdin, stdout, stderr = client.exec_command("rm -i a.txt")

    stdin.write("yes\n")  # inner, method that is called when input()
    stdin.flush()

    output = stdout.read().decode()


    print(output)

except:
    print("Could not connect")
finally:
    client.close()