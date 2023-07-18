import signal
import time 

def interrupt_handler(signum, frame):
    print("You are try to intrrrupt")

signal.signal(signal.SIGINT, interrupt_handler) #handle keyboard interrupt
signal.pause()
while True:
    print("Hey")
    time.sleep(1)
