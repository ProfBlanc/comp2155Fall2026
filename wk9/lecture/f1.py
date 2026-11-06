from netmiko import ConnectHandler

con = ConnectHandler()  # pass in arguments

con.enable()

con.find_prompt()

con.send_command("show version")
con.send_command_timing("show version")
con.disable_paging()

con.disconnect()