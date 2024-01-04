import threading

def testing():
    print("i am printing")

__message_handler_thread = threading.Thread(target=testing, args=1,daemon=True)
__message_handler_thread.start()

th2 = threading.Thread(target=testing, daemon=True)
th2.start()

