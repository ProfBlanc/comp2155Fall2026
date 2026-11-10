from netmiko import ConnectHandler
import time
import threading


def connect(host_or_ip: str)->None:
    device = {
        "host": host_or_ip,
        "username": "netauto",
        "password": "LabClass!",
        "device_type": "cisco_ios",
        "secret": "LabClass!"
    }

    connection = ConnectHandler(**device)
    print(connection.find_prompt())
    connection.disconnect()


hosts = "192.168.198.11,192.168.198.12".split(",")

start = time.perf_counter()
actions = list()
for host in hosts:
    actions.append(
        threading.Thread(
            target=connect,
            args=(host,)
        )
    )

for action in actions:
    action.start()  #exectuion of threads

for task_to_finish in actions:
    task_to_finish.join()

end = time.perf_counter()
print("Execution Time =", end-start, "seconds")

