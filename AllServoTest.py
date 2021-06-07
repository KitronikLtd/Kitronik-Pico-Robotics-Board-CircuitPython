#AllServoTest.py
# test code that ramps each servo from 0-180-0 
import PicoRobotics
import time


board = PicoRobotics.KitronikPicoRobotics()
while True:
    for degrees in range(180):
        for servo in range(1,9):
            board.servoWrite(servo, degrees)
        time.sleep(0.01) #ramp speed over 10x180ms => approx 2 seconds.
    for degrees in range(180):
        for servo in range(1,9):
            board.servoWrite(servo, 180-degrees)
        time.sleep(0.01) #ramp speed over 10x180ms => approx 2 seconds.
