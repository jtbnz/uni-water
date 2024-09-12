# -*- coding: UTF-8 -*-
# Experiment Effect: Control an external LED to blink once every second
# Wiring: Connect an LED to the UNIHIKER P21 pin
import time
from pinpong.board import Board, Pin

Board().begin()  # Initialize the UNIHIKER

led = Pin(Pin.P22, Pin.OUT)  # Initialize the pin as an output pin

while True:
    # led.value(1)  # Set the pin output to high level - Method 1
    led.write_digital(1)  # Set the pin output to high level - Method 2
    print("1")  # Print message to the terminal
    time.sleep(1)  # Wait for 1 second to maintain the state

    # led.value(0)  # Set the pin output to low level - Method 1
    led.write_digital(0)  # Set the pin output to low level - Method 2
    print("0")  # Print message to the terminal
    time.sleep(1)  # Wait for 1 second to maintain the state