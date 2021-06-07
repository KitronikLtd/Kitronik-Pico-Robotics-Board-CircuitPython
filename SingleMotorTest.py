#SingleMotorTest.py
# test code that ramps each motor individually form 0-100-0 then changes direction and does it again then steps onto next motor.
import PicoRobotics
import time


board = PicoRobotics.KitronikPicoRobotics()
directions = ["f","r"]

while True:
    
    for motor in range(4):
        for direction in directions:
            for speed in range(100):
                board.motorOn(motor+1, direction, speed)
                time.sleep(0.01) #ramp speed over 10x100ms => approx 1 second.
            for speed in range(100):
                board.motorOn(motor+1, direction, 100-speed) #ramp down
                time.sleep(0.01) #ramp speed over 10x100ms => approx 1 second.
        time.sleep(0.5)#pause between motors 
    
