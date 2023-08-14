import asyncio

async def compute_square(number, future):
    print(f"Computing the square of {number}")
    await asyncio.sleep(1)  # Simulating a time-consuming operation
    square = number ** 2
    future.set_result(square)

async def main():
    loop = asyncio.get_event_loop()
    future = loop.create_future()  # Create an asyncio.Future instance
    
    # Schedule the compute_square coroutine
    asyncio.ensure_future(compute_square(8, future))
#    asyncio.ensure_future(compute_square(8, future))
    
    print("Waiting for the result...")
    result = await future  # Wait for the result to be available
    print(f"The result is: {result}")

asyncio.run(main())