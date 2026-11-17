from lib_to_connect_using_napalm import *

try:
    device.open()
    current_config = device.get_config(retrieve="running")
    config_changes = "hostname R2-from-script"

    device.load_merge_candidate(config=config_changes)
    print(device.compare_config())
    # should ask user to confirm or validate change confirmation
    answer = input("Apply changes? Y/N")
    if answer.lower().strip() == "y":
        device.commit_config()
    else:
        device.discard_config()

except Exception as e:
    print(e)
finally:
    device.close()