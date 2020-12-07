#!/usr/bin/python2
import socket # socket library is needed but also installs with Python
import time
import pdb
HOST = '131.215.194.223'	# the remote host
HOST = '198.202.125.206'
#HOST = '169.254.1.172'
PORT = 10000			          # use telnet (other ports work fine)a

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Make the socket
s.connect((HOST, PORT)) # open the socket connection

while 1 :
    # get keyboard input
    input = raw_input(">> ")
        # Python 3 users
        # input = input(">> ")
    if input == 'exit':
        s.close()
        exit()
    else:
        # send the character to the device
        # (note that I happend a \r\n carriage return and line feed to the characters - this is requested by my device)
        s.sendall(input + '\r')
        out = ''
        # let's wait one second before reading output (let's give device time to answer)
        time.sleep(0.1)        
        out += s.recv(100)

        if out != '':
            print ">>" + out


#s.sendall('TC 1\r') # all commands should be terminated (\r here)
#data = s.recv(1024) # get response with a buffer of 1024
#print data # print the response

s.close() # close the socket
