import signal
import time 
import sys

def termination_handler(signum, frame):
    print("Termination requested")
    print("clean up.....")
    sys.exit()

signal.signal(signal.SIGINT, termination_handler) #handle keyboard interrupt
signal.pause()

while True:
    print("Hey")
    time.sleep(1)