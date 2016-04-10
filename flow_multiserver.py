#!/usr/bin/python

import socket
import threading
import time

TCP_IP = '192.168.4.4'
TCP_PORT = 2005
BUFFER_SIZE = 1024
NUM_FLOWS = 50
MESSAGE = "Hello, Server! This is ACN Project 2. How is load balancer doing?"

for x in range (0,50):
    buff = "%s"%(MESSAGE)

class myThread (threading.Thread):
    def __init__(self, threadID, srvr, port):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.srvr = srvr
        self.port = port
        #elf.port = 1
        #self.name = name
        #self.counter = 1
    def run(self):
        print "Starting port" + str(self.threadID)
        # Get lock to synchronize threads
        #threadLock.acquire()
        #print_time(self.name, self.counter, 3)
        recv_tcpdatato(self.srvr,self.port)
        # Free lock to release next thread
        #threadLock.release()

def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print "%s: %s" % (threadName, time.ctime(time.time()))
        counter -= 1
def recv_tcpdatato(server_ip,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)
    print 'Opening socket:%d',TCP_PORT
    conn, addr = s.accept()
    print 'Connection address:', addr
    while 1:
            data = conn.recv(BUFFER_SIZE)
            if not data: break
            #print "received data:", data
            conn.send("ACK")
            #print 'ack to :',addr
    conn.close()

#hreadLock = threading.Lock()
threads = []

# Create new threads
for x in range (0,NUM_FLOWS):

    #thread = myThread(x, TCP_IP, TCP_PORT)
    thread = myThread(x, TCP_IP, TCP_PORT)
    #print ("created thread :%s"%thread)
    thread.start()
    threads.append(thread)
    time.sleep(2)
    TCP_PORT += 1

# Wait for all threads to complete
for t in threads:
    #print( "join thrd %s" %t)
    t.join()

print "Exiting Main Thread"
