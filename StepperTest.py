import PicoRobotics
import time

board = PicoRobotics.KitronikPicoRobotics()
directions = ["f","r"]

while True:
        for direction in directions:
             for stepcount in range(200):
                board.step(1,direction,8)
                board.step(2,direction,8)
        time.sleep(0.5)#pause between directions 
    
    
