import os
import time
#logo
print("""

██╗░░░░░██╗███╗░░██╗██╗░░░██╗██╗░░██╗░██████╗░░█████╗░███╗░░░███╗███████╗██████╗░██████╗░░█████╗░░█████╗░████████╗
██║░░░░░██║████╗░██║██║░░░██║╚██╗██╔╝██╔════╝░██╔══██╗████╗░████║██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝
██║░░░░░██║██╔██╗██║██║░░░██║░╚███╔╝░██║░░██╗░███████║██╔████╔██║█████╗░░██████╔╝██████╦╝██║░░██║██║░░██║░░░██║░░░
██║░░░░░██║██║╚████║██║░░░██║░██╔██╗░██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░██╔══██╗██╔══██╗██║░░██║██║░░██║░░░██║░░░
███████╗██║██║░╚███║╚██████╔╝██╔╝╚██╗╚██████╔╝██║░░██║██║░╚═╝░██║███████╗██║░░██║██████╦╝╚█████╔╝╚█████╔╝░░░██║░░░
╚══════╝╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝╚═════╝░░╚════╝░░╚════╝░░░░╚═╝░░░

""")
#options
print("""
1. command-line(cli) mode
2. start <os-name>
3. reboot
4. exit
""")
#your input
boot = input()
#boot chooses
if boot == '1':
	print("""
	use this command for cli-mode:
	$ sudo python cli.py
	""")
	time.sleep(4)
	os.system("exit")
if boot ==  '2':
	print("""
	use this command to start your os:
	$ sudo python <filename>.py
	""")
	time.sleep(4)
	os.system("exit")
	# <filename> is editable
if boot == '3':
	print("""
	use this command to reboot:
	$ sudo python boot.py
	""")
	time.sleep(4)
	os.system("exit")
if boot == '4':
	time.sleep(0.5)
	os.system("exit")
# end
