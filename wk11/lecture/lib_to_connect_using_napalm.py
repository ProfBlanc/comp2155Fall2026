from napalm import get_network_driver

driver = get_network_driver("ios")

device = driver(
    hostname="192.168.198.12",
    username="netauto",
    password="LabClass!"
)