#!/usr/bin/env python
import socket
import time

print socket.gethostname()

TCP_IP = '0.0.0.0'
TCP_PORT = 12311
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response

print '1'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print '2'
s.bind((TCP_IP, TCP_PORT))
print '3'
s.listen(1)
print '4'
conn, addr = s.accept()
print '5'
print 'Connection address:', addr
print '6'

while 1:
  data = conn.recv(BUFFER_SIZE)
  if not data: break
  elif data == "quit": break
  print "received data:", data
  conn.send(data)  # echo

conn.close()