import socket
import time
TCP_IP = '127.0.0.1'
TCP_PORT = 2005
BUFFER_SIZE = 256 
MESSAGE = "Hello, Server! This is Yuan sending how are you"
 
buff = "%s"%(MESSAGE)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()
print "received data:",data
time.sleep(0.5)
