import threading
import asyncio
import time
# Threading example
def print_numbers():
    for i in range(5):
        print(f"Thread 1: {i}")
        time.sleep(1)

# Asyncio example
async def count_down():
    for i in range(5, 0, -1):
        print(f"Asyncio: {i}")
        await asyncio.sleep(1)

# Event loop example
def run_event_loop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(count_down())
    loop.close()

if __name__ == "__main__":
    # Threading
    thread = threading.Thread(target=print_numbers)
    thread.start()

    # Asyncio
    asyncio.run(count_down())

    # Event loop
    run_event_loop()
