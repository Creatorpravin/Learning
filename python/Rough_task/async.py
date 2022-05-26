import asyncio

async def prin():
    print("A")
    await asyncio.sleep(1)
    print("B")

asyncio.run(prin())

