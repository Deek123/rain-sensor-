#!/usr/bin/python
# Derrick Elliott with some help from the raspbery pi forums
#this program will interface with a sensor in order to tell if there is rain or not  
#later revisions may include use of the LCD plate 
import time
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)


import socket
import time
SERVERIP = '10.0.0.22'
n = 0 


while True: 
    state = GPIO.input(23)


    if (state == 0):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((SERVERIP, 8881))
        localtime = time.asctime( time.localtime(time.time()) )
        data = "$$$$Delliott$$$ ,%d, water detected %s" %(n, localtime)
        sock.sendall(data)
        sock.close( )
        time.sleep(5)
        n = n+1
        print " sent:", data



        print "Water detected!", localtime
    else:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((SERVERIP, 8881))
        localtime = time.asctime( time.localtime(time.time()) )
        data = "$$$$Delliott$$$ ,%d, No water %s" %(n, localtime)
        sock.sendall(data)
        sock.close( )
        time.sleep(5)
        n = n+1
        print "Water not detected", localtime
    time.sleep(20) 

