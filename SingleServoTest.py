#SingleServoTest.py
# test code that ramps each servo individually from 0-180-0 
import PicoRobotics
import time


board = PicoRobotics.KitronikPicoRobotics()
while True:
   
    for servo in range(8):
        for degrees in range(180):
            board.servoWrite(servo+1, degrees)
            time.sleep(0.01) #ramp speed over 10x180ms => approx 2 seconds.
        for degrees in range(180):
            board.servoWrite(servo+1, 180-degrees)
            time.sleep(0.01) #ramp speed over 10x180ms => approx 2 seconds.
        board.servoWrite(servo+1, 90)
        time.sleep(0.05)#pause between servos 
