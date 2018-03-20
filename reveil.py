#!/usr/bin/env python
#-*- coding: utf-8 -*-

import time

from display import Display
from udpReceiver import UDPReceiver
from alarm import Alarm

class main:

    def __init__(self):
        self.__user = ""
        self.__configFileName = "config.txt"
        self.__saveFileName = "alarm.txt"
        self.__time = None
        self.__alarm = "00:00"
        self.__volume = 0.1
        self.__brightness = 0.1
        self.__alarmIsActivated = False
        self.__alarmIsRunning = False
        
        self.__display = Display()
        self.__display.start()
        self.readConfigFile()
        print("User is set to "+self.__user)
        self.readAlarmFromFile()
        print("Alarm is set at "+self.__alarm)
        
        self.udpReceiver = UDPReceiver(self, self.__display)
        self.udpReceiver.start()

        self.__alarmManager = Alarm(self)
        self.__alarmManager.start()
        
        self.__display.setWhatToDisplay("clock")
        
        while True:
            self.__time = time.strftime("%H:%M")
            #if int(time.strftime("%S"))%2 == 0:
            self.__display.setTime(time.strftime("%H:%M"))
            #else:
            #    self.__display.setTime(time.strftime("%H %M"))

            if self.__time == self.__alarm[0:5] and self.__alarmIsActivated and not self.__alarmIsRunning:
                self.__alarmIsRunning = True
                self.__alarmManager.playAlarm()

            if self.__alarmIsRunning:
                self.__volume += 0.01
                self.__alarmManager.setVolume(self.__volume)
                
            time.sleep(0.5)

    def readConfigFile(self):
        file = open(self.__configFileName, "r")
        self.__user = file.read()[:-1]

    def readAlarmFromFile(self):
        file = open(self.__saveFileName, "r")
        self.__alarm = file.read()[:-1]
        self.__display.setAlarm(self.__alarm)
        file.close()

    def saveAlarmToFile(self, alarm):
        file = open(self.__saveFileName, "w")
        file.write(alarm)
        file.close()

    def getDisplay(self):
        return self.__display()

    def setAlarm(self, alarm):
        self.__alarm = alarm

    def setIsActivated(self, isActivated):
        self.__alarmIsActivated = isActivated

    def getUser(self):
        return self.__user

if __name__ == "__main__":
    main()
