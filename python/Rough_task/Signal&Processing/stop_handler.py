import signal
import time 
import sys

def stop_handler(signum, frame):
    print("You cannot put me into background")

signal.signal(signal.SIGTSTP, stop_handler) #handle keyboard interrupt

while True:
    print("Hey")
    time.sleep(1)