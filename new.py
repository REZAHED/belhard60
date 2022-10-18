import asyncio
# import multiprocessing

# import threading
# from time import sleep
# from datetime import datetime
#
# def foo(i:int):
#     for _ in range(10):
#         sleep(1)
#         print(i)
# if __name__ == '__main__':
#     threads = [multiprocessing.Process(target=foo,args=(j,)) for j in range(10)]
#     for thread in threads:
#         thread.start()


async def foo(i):
    for _ in range(10):
        await asyncio.sleep(1)
        print(i)


async def main():
    tasks = [asyncio.create_task(foo(j)) for j in range(10)]
    await asyncio.wait(tasks)

if __name__ == '__main__':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())