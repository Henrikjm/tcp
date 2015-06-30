#!/usr/bin/env python
import socket

TCP_IP = '78.91.34.147'
TCP_PORT = 12332
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
  print '7'
  data = conn.recv(BUFFER_SIZE)
  if not data: break
  print "received data:", data
  conn.send(data)  # echo

conn.close()