#!/usr/bin/env python
#-*- coding: utf-8 -*-

import time
import sys, os
from threading import Thread

import scrollphathd
from scrollphathd.fonts import font3x5

class Display(Thread):

    def __init__(self):
        Thread.__init__(self)
        
    def run(self):
        self.__time = "00:00"
        self.__alarm = "01:00"
        self.__brightness = 0.1
        self.__whatToDisplay = "clock"
        self.printTime()

    def setTime(self, time):
        self.__time = time

    def setAlarm(self, alarm):
        self.__alarm = alarm

    def setWhatToDisplay(self, whatToDisplay):
        self.__whatToDisplay = whatToDisplay

    def setBrightness(self, brightness):
        self.__brightness = brightness

    def printTime(self):
        while True:
            #os.system('clear')
            scrollphathd.clear()
            if self.__whatToDisplay == "clock":
                #print(self.__time)
                scrollphathd.write_string(self.__time, x=0, y=0, font=font3x5, brightness=self.__brightness)
            elif self.__whatToDisplay == "alarm":
                #print(self.__alarm)
                scrollphathd.write_string(self.__alarm, x=0, y=0, font=font3x5, brightness=self.__brightness)
            scrollphathd.show()
            time.sleep(0.1)

    
