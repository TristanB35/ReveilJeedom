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
        self.__lastClickTime = 0

    def run(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        while True:
            if GPIO.input(17):
                self.click()
            time.sleep(0.05)

    def click(self):
        if datetime.now() - self.__lastClickTime > 1000:
            self.__parent.setAlarmIsPaused(True)
        else:
            self.__doubleClick()

    def doubleClick(self):
        self.__parent.setAlarmIsStopped(True)
