from netmiko import ConnectHandler

router = {
    "device_type": "cisco_ios",
    "host": "192.168.198.12",
    "username": "netauto",
    "password": "LabClass!",
    "secret": "LabClass!"
}

users = [
    {
        "username": "john",
        "password": "JohnPass123",
        "privilege": 15
    },
    {
        "username": "mary",
        "password": "MaryPass123",
        "privilege": 5
    },
    {
        "username": "peter",
        "password": "PeterPass123",
        "privilege": 1
    }
]

connection = ConnectHandler(**router)

connection.enable()

for user in users:

    command = (
        f"username {user['username']} "
        f"privilege {user['privilege']} "
        f"secret {user['password']}"
    )

    output = connection.send_config_set([command])

    print(f"Created user: {user['username']}")
    print(output)

connection.disconnect()
