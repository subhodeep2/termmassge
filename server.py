#!/usr/bin/python3

import socket
import threading

def send_mssg():
	while True:
		msg = input().encode()
		client.send(msg)

def recv_mssg():
	while True:
		recevied = client.recv(1024)
		print(recevied.decode())

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
s.bind(("127.0.0.1",8888))
print("Listening...")
s.listen(1)
client,addr = s.accept()
print("Connected")

t1 = threading.Thread(target=send_mssg)
t1.start()
recv_mssg()
