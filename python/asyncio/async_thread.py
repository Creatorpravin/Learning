import asyncio
import threading
import time

# Function to run asynchronously with asyncio
async def async_function():
    for i in range(5):
        await asyncio.sleep(1)
        print(f"Async Task {i}")

# Function to run in a separate thread
def thread_function():
    for i in range(5):
        print(f"Thread Task {i}")
        # time.sleep(1)

if __name__ == "__main__":
    # Create an event loop for asyncio
    asyncio_loop = asyncio.get_event_loop()

    # Create a thread for the thread function
    thread = threading.Thread(target=thread_function)

    # try:
        # Start the thread
    thread.start()

        # Run the asyncio task
    asyncio_loop.run_until_complete(async_function())
    # finally:
    #     # Ensure the thread has finished
    #     thread.join()

    # Close the event loop
    asyncio_loop.close()
