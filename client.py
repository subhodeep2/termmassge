#!/usr/bin/python3

import socket
import threading

def send_mssg():
	while True:
		mssg = input().encode()
		s.send(mssg)

def recv_mssg():
	while True:
		recevied = s.recv(1024)
		print(recevied.decode())

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Connecting...")
while True:
	try:
		s.connect(("127.0.0.1",8888))
		break
	except ConnectionRefusedError:
		continue
print("Connected")

t1 = threading.Thread(target=send_mssg)
t1.start()
recv_mssg()

