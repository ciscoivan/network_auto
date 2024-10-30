# coding:utf-8

import os
import time
import multiprocessing
import asyncio

async def a():
    for i in range(10):
        print(i, 'a')
        await asyncio.sleep(1)
    return 'a'

async def b():
    for i in range(10):
        await asyncio.sleep(1)
        print(i, 'b')
    return 'b'

async def c():
    print('hello xiaomu')

async def main():
    result = await asyncio.gather(
        a(),
        b(),
        c()
    )
    print(result)

def check(i, lock):
    try:
        lock.acquire()
        print(i, os.getpid())
        time.sleep(2)
    finally:
        lock.release()

async def test():
    return 'test'

if __name__ == '__main__':
   res = asyncio.run(main())
