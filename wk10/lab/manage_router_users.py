from netmiko import ConnectHandler

# R2
router = {
    "device_type": "cisco_ios",
    "host": "192.168.198.12",
    "username": "netauto",
    "password": "LabClass!",
    "secret": "LabClass!"
}

connection = None

try:

    # Connect to router
    connection = ConnectHandler(**router)

    connection.enable()

    print("\n===== USER MANAGEMENT =====")

    # 1. Create users
    users = [
        "username john privilege 15 secret JohnPass123",
        "username mary privilege 5 secret MaryPass123",
        "username peter privilege 1 secret PeterPass123"
    ]

    print("\nCreating users...")

    output = connection.send_config_set(users)

    print(output)

    # 2. Display configured users
    print("\nDisplaying users...")

    output = connection.send_command(
        "show running-config | include ^username"
    )

    print(output)

    # 3. Change John's password
    print("\nUpdating John's password...")

    output = connection.send_config_set([
        "username john privilege 15 secret NewJohnPass456"
    ])

    print(output)

    # 4. Verify user configuration
    print("\nVerifying user configuration...")

    output = connection.send_command(
        "show running-config | include ^username"
    )

    print(output)

    print("\nUser management completed!")

except Exception as error:

    print(f"An error occurred: {error}")

finally:

    if connection:
        connection.disconnect()
