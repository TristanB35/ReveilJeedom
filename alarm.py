#!/usr/bin/env python
#-*- coding: utf-8 -*-

import pygame
from threading import Thread

class Alarm(Thread):

    def __init__(self):
        Thread.__init__(self)

    def run(self):
        pygame.mixer.init()

    def playAlarm(self):
        pygame.mixer.music.load("sleep_cycle.wav")
        pygame.mixer.music.play(loops=9999, start=0.0)
        pygame.mixer.music.set_volume(0.1)

    def pauseAlarm(self):
        pygame.mixer.music.pause()

    def stopAlarm(self):
        pygame.mixer.music.stop()

    def setVolume(self, volume):
        pygame.mixer.music.set_volume(volume)
