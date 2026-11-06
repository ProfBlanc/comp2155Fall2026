from netmiko import ConnectHandler
import netmiko.exceptions

device = {
    "host": "192.168.198.131",
    "username": "root",
    "password": "pnet",
    "device_type": "linux",
}

connection = None

try:
    connection = ConnectHandler(**device)
    print("Connection Successful")
except netmiko.exceptions.NetMikoTimeoutException:
    print("Connection timed out")
except netmiko.exceptions.NetMikoAuthenticationException:
    print("Authentication Error")
except Exception as e:
    print("General Error:", e)
finally:
    if connection is not None:
        connection.disconnect()