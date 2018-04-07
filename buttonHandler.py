#!/usr/bin/env python
#-*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from threading import Thread
import time
import os
from datetime import datetime
from datetime import timedelta

class ButtonHandler(Thread):
    
    def __init__(self, parent):
        Thread.__init__(self)
        self.__parent = parent
        self.__lastClickTime = None

    def run(self):
        self.__lastClickTime = datetime.now()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        while True:
            if not GPIO.input(17):
                self.click()
                time.sleep(0.05)
                print("Click")

    def click(self):
        if datetime.now() - self.__lastClickTime > datetime.timedelta(500):
            if self.__parent.getAlarmIsRunning():
                self.__lastClickTime = datetime.now()
                self.__parent.setAlarmIsPaused(True)
        else:
            if self.__parent.getAlarmIsRunning() or self.__parent.getAlarmIsPaused():
            self.__doubleClick()

    def doubleClick(self):
        self.__parent.setAlarmIsStopped(True)
