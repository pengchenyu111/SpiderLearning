from atexit import register
from random import randrange
from threading import BoundedSemaphore, Lock, Thread
from time import sleep, ctime

# 创建线程锁
lock = Lock()
# 定义糖果机的槽数，也是信号量计数器的最大值
MAX = 5
# 创建信号量对象，并指定计数器的最大值
candytray = BoundedSemaphore(MAX)


# 给糖果机的槽补充新的糖果（每次只补充一个槽）
def refill():
    # 获取线程锁，将补充糖果的操作变成原子操作
    lock.acquire()
    print('重新添加糖果...', end=' ')
    try:
        # 为糖果机的槽补充糖果（计数器加1）
        candytray.release()
    except ValueError:
        print('糖果机都满了，无法添加')
    else:
        print('成功添加糖果')
    # 释放线程锁
    lock.release()


# 顾客购买糖果
def buy():
    # 获取线程锁，将购买糖果的操作变成原子操作
    lock.acquire()
    print('购买糖果...', end=' ')
    # 顾客购买糖果（计数器减1），如果购买失败（5个槽都没有糖果了），返回False
    if candytray.acquire(False):
        print('成功购买糖果')
    else:
        print('糖果机为空，无法购买糖果')
    # 释放线程锁
    lock.release()


# 产生多个补充糖果的动作
def producer(loops):
    for i in range(loops):
        refill()
        sleep(randrange(3))


# 产生多个购买糖果的动作
def consumer(loops):
    for i in range(loops):
        buy()
        sleep(randrange(3))


def main():
    print('开始:', ctime())
    # 参数一个2到5的随机数
    nloops = randrange(2, 6)
    print('糖果机共有%d个槽!' % MAX)
    # 开始一个线程，用于执行consumer函数
    Thread(target=consumer, args=(randrange(nloops, nloops + MAX + 2),)).start()
    # 开始一个线程，用于执行producer函数
    Thread(target=producer, args=(nloops,)).start()


@register
def exit():
    print('程序执行完毕：', ctime())


if __name__ == '__main__':
    main()
