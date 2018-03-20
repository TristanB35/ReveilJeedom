#!/usr/bin/env python
#-*- coding: utf-8 -*-

from threading import Thread
from socket import *
import sys, time

from display import Display

class UDPReceiver(Thread):
    
    def __init__(self, parent, display):
        Thread.__init__(self)
        self.__parent = parent
        self.__display = display

    def run(self):
        self.receive()

    def receive(self):
        while True:
            s=socket(AF_INET, SOCK_DGRAM)
            s.bind(('',12345))
            m=s.recvfrom(1024)
            m=m[0].split(";")
            if m[0] == "setAlarm":
                user=m[1]
                alarm=m[2]
                if len(alarm) == 3:
                    alarm="0"+alarm[0]+":"+alarm[1:3]
                else:
                    alarm=alarm[0:2]+":"+alarm[2:4]
                self.updateAlarm(user, alarm)
            elif m[0] == "setBrightness":
                continue
            elif m[0] == "setVolume":
                continue

    def updateAlarm(self, user, alarm):
        if user == "tristan":
            self.__parent.saveAlarmToFile(alarm)
            self.__display.setAlarm(alarm)
            self.__display.setWhatToDisplay("alarm")
            time.sleep(5)
            self.__display.setWhatToDisplay("clock")
        elif user == "stop":
            self.__display.setWhatToDisplay("stop")
            sys.exit()
            
