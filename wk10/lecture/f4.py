from netmiko import ConnectHandler
import time

def connect(host_or_ip: str)->None:
    device = {
        "host": host_or_ip,
        "username": "netauto",
        "password": "LabClass!",
        "device_type": "cisco_ios",
        "secret": "LabClass!"
    }

    connection = ConnectHandler(**device)
    connection.disconnect()

hosts = "192.168.198.11,192.168.198.12".split(",")

start = time.perf_counter()

for host in hosts:
    connect(host)

end = time.perf_counter()
print("Execution Time =", end-start, "seconds")

