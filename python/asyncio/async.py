import asyncio 

async def kill_time(num):
    print('Running', num)
    await asyncio.sleep(0.1)
    print('Finish', num)

async def main():
    print("Started!")
    list_of_task = []
    for i in range(1, 6):
        list_of_task.append(asyncio.create_task(kill_time(i)))
    print(list_of_task)
    #await asyncio.sleep(2)
    for j in list_of_task:
        await j

    #await asyncio.gather(*list_of_task)

    print('Done')


if __name__ == "__main__":
    asyncio.run(main())