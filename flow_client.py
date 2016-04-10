import socket
import time
TCP_IP = '192.168.4.4'
TCP_PORT = 2005
BUFFER_SIZE = 256
MESSAGE = "Hello, Server! This is ACN Project 2. How is load balancer doing?Hello, Server!?"
for x in range (0,1):
    buff = "%s"%(MESSAGE)

for x in range (0,99): 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send(MESSAGE)
    data = s.recv(BUFFER_SIZE)
    s.close()
    print "received data:",data
    TCP_PORT += 1
    time.sleep(0.5)

