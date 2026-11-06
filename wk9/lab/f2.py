from netmiko import ConnectHandler

device = {
    "host": "192.168.198.131",
    "username": "root",
    "password": "pnet",
    "device_type": "linux",
}

connection = ConnectHandler(**device)

print("Connection Successful")

print(connection.find_prompt())
connection.enable()
print(connection.find_prompt())

output = connection.send_command("whoami")
print(output)

commands = "hostname,uptime,ip addr".split(",")
for command in commands:
    print(connection.send_command(command))

connection.disconnect()