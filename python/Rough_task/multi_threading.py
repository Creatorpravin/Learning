from time import sleep
import threading

def run01(a):
        for i in range(5):
            print("hello"+a)
           
def run02(a):
        for i in range(5):
            print("hi"+a)
            #sleep(1)            
if __name__ == "__main__":
 t1 = threading.Thread(target=run01("yes"), name="t1")
 t2 = threading.Thread(target=run02("no"), name="t2")

 t1.start()
 t2.start()

 t1.join()
 t2.join()
 


print("bye")
