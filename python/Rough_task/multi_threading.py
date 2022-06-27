from time import sleep
import threading

def run01():
        for i in range(5):
            print("hello")
            sleep(1)
def run02():
        for i in range(5):
            print("hi")
            sleep(1)            
if __name__ == "__main__":
 t1 = threading.Thread(target=run01, name="t2")
 t2 = threading.Thread(target=run02, name="t2")

 t1.start()
 t2.start()

 t1.join()
 t2.join()


print("bye")
