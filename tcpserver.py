import socket
import time
TCP_IP = '127.0.0.1'
TCP_PORT = 2005
BUFFER_SIZE = 256 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
print 'Opening socket:%d',TCP_PORT
conn, addr = s.accept()
print 'Connection address:', addr
while 1:
        data = conn.recv(BUFFER_SIZE)
        if not data: break
        print "received data:", data
        conn.send("ACK")
        #print 'ack to :',addr
conn.close()
