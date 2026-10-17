import os
import paramiko

# Does not work because of older Cisco device and SSH protocols
host = "192.168.198.11"
port = 22
username = "netauto"

key_path = os.path.expandvars(
    r"%USERPROFILE%\.ssh\pnetlab_rsa"
)

private_key = paramiko.RSAKey.from_private_key_file(
    key_path,
    password="comp2155"
)

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    client.connect(
        hostname=host,
        port=port,
        username=username,
        pkey=private_key,

        # Match the legacy server's RSA authentication
        disabled_algorithms={
            "pubkeys": [
                "rsa-sha2-256",
                "rsa-sha2-512",
            ]
        },


        timeout=20,
        auth_timeout=10,
        allow_agent=False,
        look_for_keys=False,
    )



    print("Authentication successful!")

    stdin, stdout, stderr = client.exec_command("whoami")
    print(stdout.read().decode())

finally:
    client.close()