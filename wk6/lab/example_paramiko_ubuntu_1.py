import paramiko

hostname = "192.168.198.131"  # different for everyone
username = "root"  # same for everyone
password = "pnet"
port = 22

client = paramiko.SSHClient()

# in production, you should loat the system host keys
# client.load_system_host_keys()

client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    client.connect(
        hostname=hostname,
        username=username,
        password=password,
        port=port
    )

    stdin, stdout, stderr = client.exec_command("hostname")

    output = stdout.read().decode()

    exit_code = stdout.channel.recv_exit_status()

    print(output)
    print("Exit code:", exit_code)

except:
    print("Could not connect")
finally:
    client.close()