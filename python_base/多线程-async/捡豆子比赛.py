import random
import asyncio

"""
    async 定义异步函数
    await 执行异步
    gather 将异步函数批量执行
    run 执行主异步函数
"""

# 豆子总数
beans = list(range(1, 51))


async def child_a():
    a_beans = []


    while True:
        await  asyncio.sleep((random.random() * 2))
        if len(beans) == 0:
            print("done")
            break
        else:
         bean = random.choice(beans)
         a_beans.append(bean)
         beans.remove(bean)

    return "done%s" % len(a_beans)


async def child_b():
    b_beans = []
    if len(beans) == 0:
        print("done")

    while True:
        await  asyncio.sleep((random.random() * 2))
        if len(beans) == 0:
            print("done")
            break
        else:
            bean = random.choice(beans)
            b_beans.append(bean)
            beans.remove(bean)
    return "done%s" % len(b_beans)


async def main():
    result = await asyncio.gather(child_a(), child_b())
    return result


if __name__ == '__main__':
    result = asyncio.run(main())
    print("a_beans:", result[0])
    print("b_beans:", result[1])