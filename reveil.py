#!/usr/bin/env python
#-*- coding: utf-8 -*-

import time

from display import Display
from udpReceiver import UDPReceiver
from alarm import Alarm
from buttonHandler import ButtonHandler

class main:

    def __init__(self):
        self.__user = ""
        self.__configFileName = "config.txt"
        self.__saveFileName = "alarm.txt"
        self.__time = None
        self.__alarm = "00:00"
        self.__snoozeTime = None
        self.__volume = 0.1
        self.__brightness = 0.1
        self.__alarmIsActivated = True
        self.__alarmIsRunning = False
        self.__alarmIsPaused = False
        self.__alarmIsStopped = True
        
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

        self.__buttonHandler = ButtonHandler(self)
        self.__buttonHandler.start()
        
        self.__display.setWhatToDisplay("clock")
        
        while True:
            self.__time = time.strftime("%H:%M")
            self.__display.setTime(time.strftime("%H:%M"))

            #Sounding the alarm
            if (self.__time == self.__alarm[0:5] or datetime.now() == self.__snoozeTime) and self.__alarmIsActivated and self.__alarmIsStopped and not self.__alarmIsRunning and not self.__alarmIsPaused:
                self.__alarmIsRunning = True
                self.__alarmManager.playAlarm()
                self.__snoozeTime = datetime.now() + datetime.delta(minutes=9)

            #Pausing the alarm (snooze)
            if self.__alarmIsActivated and self.__alarmIsRunning and self.__alarmIsPaused and not self.__alarmIsStopped:
                self.__alarmManager.pauseAlarm()
                
            #Stopping the alarm
            if self.__alarmIsActivated and self.__alarmIsRunning and self.__alarmIsStopped:
                self.__alarmIsRunning = False
                self.__alarmIsPaused = False
                self.__alarmManager.stopAlarm()
                
            #Setting the volume
            if self.__alarmIsRunning:
                self.__volume += 0.01
                self.__alarmManager.setVolume(self.__volume)

            #Saving some CPU
            time.sleep(0.5)

    def readConfigFile(self):
        file = open(self.__configFileName, "r")
        self.__user = file.read()[:-1]

    def readAlarmFromFile(self):
        file = open(self.__saveFileName, "r")
        self.__alarm = file.read()[0:5]
        self.__display.setAlarm(self.__alarm)
        file.close()

    def saveAlarmToFile(self, alarm):
        file = open(self.__saveFileName, "w")
        file.write(alarm)
        file.close()

    def setBrightness(self, brightness):
        self.__display.setBrightness(brightness)

    def setAlarm(self, alarm):
        self.__alarm = alarm

    def setIsActivated(self, isActivated):
        self.__alarmIsActivated = isActivated

    def getUser(self):
        return self.__user

    def setAlarmIsPaused(self, paused):
        self.__alarmIsPaused = paused

    def setAlarmIsStopped(self, stopped):
        self.__alarmIsStopped = stopped

if __name__ == "__main__":
    main()
