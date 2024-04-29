import threading
import time

class SimpleThread:
    def __init__(self):
        self.stop_event = threading.Event()  # Event to signal thread to stop
        self.thread = threading.Thread(target=self.run)  # Create the thread
        

    def run(self):
        self.run2()
        while not self.stop_event.is_set():  # While stop event is not set
            print("Thread is running...")
            time.sleep(1)  # Sleep for 1 second between iterations
        
    def run2(self):
        while not self.stop_event.is_set():  # While stop event is not set
            print("Thread 2 is running...--------------------")
            time.sleep(0.5)  # Sleep for 1 second between iterations


    def start(self):
        self.thread.start()  # Start the 
    

    def stop(self):
        self.stop_event.set()  # Set the stop event to stop the thread
        self.thread.join()  # Wait for the thread to terminate

# Example usage:
if __name__ == "__main__":
    thread_instance = SimpleThread()  # Create an instance of SimpleThread
    thread_instance.start()  # Start the thread

    try:
        # Run main application loop here
        while True:
            time.sleep(1)  # Dummy loop to keep the main thread alive
    except KeyboardInterrupt:
        thread_instance.stop()  # Stop the thread when the application is terminated
