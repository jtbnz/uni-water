# -*- coding: UTF-8 -*-
# Experiment Effect: Control an external LED to blink once every second
# Wiring: Connect an LED to the UNIHIKER P21 pin
import time
from pinpong.board import Board, Pin

Board().begin()  # Initialize the UNIHIKER

led = Pin(Pin.P22, Pin.OUT)  # Initialize the pin as an output pin

count = 0
while count < 10:
    led.write_digital(1)
    print("1")
    time.sleep(1)

    led.write_digital(0)
    print("0")
    time.sleep(1)

    count += 1