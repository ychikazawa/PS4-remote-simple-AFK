import keyboard
import time
import random

keys = ["enter", "down arrow", "up arrow"]

message = """
***************************************************
***            PS4 REMOTE SIMPLE AFK            ***
***************************************************

This tool controls your keyboard to hook key events.
It hooks part of keyboard input that allowed by PS4 
remote play app such as enter and arrow keys.
Press enter to start, Press Ctrl+C to stop.

---------------------------------------------------
"""

print(message)
print('Press enter to start...')
input('>')
print('Start!')
print('Note: press Ctrl+C to stop.')
print('\n---------------------------------------------------\n')


while True:
    keyboard.send(keys[random.randrange(3)])
    time.sleep(random.uniform(0.1, 3))
