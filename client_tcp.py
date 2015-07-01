#!/usr/bin/env python

import socket
import time

TCP_IP = '78.91.34.203'
TCP_PORT = 12311
BUFFER_SIZE = 1024
MESSAGE = "Hello, World! You are connected. Write 'quit' to close connection."

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
MESSAGE = raw_input('Enter message to send : ')



s.close()
print "received data:", data