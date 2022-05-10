import RPi.GPIO as gpio

import time
import pygame
import sys
import threading
PWM_ENA=None
PWM_ENB=None
class Rc:
    def __init__(self):
        gpio.setmode(gpio.BCM)
        self.IN1 =20
        self.IN2 =21
        self.ENA =26

        self.IN3 =6
        self.IN4 =13
        self.ENB =12
        self.led=17
        gpio.setwarnings(False)
    def motor_init(self):
        global PWM_ENA
        global PWM_ENB
        gpio.setup(self.led,gpio.OUT,initial=gpio.LOW)
        gpio.setup(self.ENA,gpio.OUT,initial=gpio.HIGH)
        gpio.setup(self.IN1,gpio.OUT,initial=gpio.LOW)
        gpio.setup(self.IN2,gpio.OUT,initial=gpio.LOW)
        gpio.setup(self.ENB,gpio.OUT,initial=gpio.HIGH)
        gpio.setup(self.IN3,gpio.OUT,initial=gpio.LOW)
        gpio.setup(self.IN4,gpio.OUT,initial=gpio.LOW)
        PWM_ENA=gpio.PWM(self.ENA,2000)
        PWM_ENB=gpio.PWM(self.ENB,2000)
        PWM_ENA.start(0)
        PWM_ENB.start(0)
    def turn_on(self):
        gpio.output(self.led,gpio.HIGH)
    def turn_off(self):
        gpio.output(self.led,gpio.LOW)
    def forward_(self,speed_):
        global PWM_ENA
        global PWM_ENB
        gpio.output(self.IN1,gpio.HIGH)
        gpio.output(self.IN2,gpio.LOW)
        gpio.output(self.IN3,gpio.HIGH)
        gpio.output(self.IN4,gpio.LOW)
        PWM_ENA.ChangeDutyCycle(speed_)
        PWM_ENB.ChangeDutyCycle(speed_)
        PWM_ENA.ChangeDutyCycle(250)
        PWM_ENB.ChangeDutyCycle(250)
    def backward_(self,speed_):
        global PWM_ENA
        global PWM_ENB
        gpio.output(self.IN1,gpio.LOW)
        gpio.output(self.IN2,gpio.HIGH)
        gpio.output(self.IN3,gpio.LOW)
        gpio.output(self.IN4,gpio.HIGH)
        PWM_ENA.ChangeDutyCycle(speed_)
        PWM_ENB.ChangeDutyCycle(speed_)
        PWM_ENA.ChangeDutyCycle(250)
        PWM_ENB.ChangeDutyCycle(250)
    def right_(self,speed_):
        global PWM_ENA
        global PWM_ENB
        gpio.output(self.IN1,gpio.HIGH)
        gpio.output(self.IN2,gpio.LOW)
        gpio.output(self.IN3,gpio.LOW)
        gpio.output(self.IN4,gpio.LOW)
        PWM_ENA.ChangeDutyCycle(speed_)
        PWM_ENB.ChangeDutyCycle(speed_)
        time.sleep(0.3)
        PWM_ENA.ChangeDutyCycle(0)
        PWM_ENB.ChangeDutyCycle(0)
    def left_(self,speed_):
        global PWM_ENA
        global PWM_ENB
        gpio.output(self.IN1,gpio.LOW)
        gpio.output(self.IN2,gpio.LOW)
        gpio.output(self.IN3,gpio.HIGH)
        gpio.output(self.IN4,gpio.LOW)
        PWM_ENA.ChangeDutyCycle(speed_)
        PWM_ENB.ChangeDutyCycle(speed_)
        time.sleep(0.3)
        PWM_ENA.ChangeDutyCycle(0)
        PWM_ENB.ChangeDutyCycle(0)
    def stop_(self):
        global PWM_ENA
        global PWM_ENB
        PWM_ENA.ChangeDutyCycle(0)
        PWM_ENB.ChangeDutyCycle(0)
'''
r=Rc()
r.motor_init()

r.forward_(100)
time.sleep(1)
r.stop_()
time.sleep(1)

r.backward_(100)
time.sleep(1)
r.stop_()
time.sleep(1)

r.left_(100)
time.sleep(1)
r.stop_()
time.sleep(1)
r.right_(100)
time.sleep(1)
r.stop_()
'''
