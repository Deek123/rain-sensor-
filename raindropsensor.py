#!/usr/bin/python
# Derrick Elliott with some help from the raspbery pi forums
#this program will interface with a sensor in order to tell if there is rain or not  
#later revisions may include use of the LCD plate 

import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
state = GPIO.input(23)

if (state == 0):
    print "Water detected!"
else:
    print "Water not detected"
