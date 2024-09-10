# -*- coding: UTF-8 -*-
import time
from pinpong.board import *
from pinpong.extension.unihiker import *

Board().begin()  # Initialize the UNIHIKER

while True:
    light_value = light.read()  # Read the ambient light intensity
    print("Ambient light intensity: %d" % (light_value))  # Print the ambient light intensity to the terminal
    time.sleep(0.1)  # Wait for 0.1 seconds to maintain the state