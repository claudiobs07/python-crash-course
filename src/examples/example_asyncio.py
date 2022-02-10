import asyncio
import time


async def do_something(seconds):
    print(f'Sleeping {seconds} second...')
    await asyncio.sleep(seconds)
    print('Done Sleeping...')


async def main():
    tasks = []
    for _ in range(100):
        tasks.append(asyncio.create_task(do_something(2)))

    for task in tasks:
        await task


if __name__ == '__main__':
    start = time.perf_counter()
    asyncio.run(main())
    finish = time.perf_counter()
    print(f'Finished in {round(finish - start, 2)} seconds')

