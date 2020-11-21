from random import randrange
from time import sleep, time, ctime
from threading import Lock, Thread
from queue import Queue

# 创建线程锁对象
lock = Lock()


# 从Thread派生的子类
class MyThread(Thread):
    def __init__(self, func, args):
        super().__init__(target=func, args=args)


# 向队列中添加商品
def writeQ(queue):
    # 获取线程锁
    lock.acquire()
    print('生产了一个对象，并将其添加到队列中', end='  ')
    # 向队列中添加商品
    queue.put('商品')
    print("队列尺寸", queue.qsize())
    # 释放线程锁
    lock.release()


# 从队列中获取商品
def readQ(queue):
    # 获取线程锁
    lock.acquire()
    # 从队列中获取商品
    val = queue.get(1)
    print('消费了一个对象，队列尺寸：', queue.qsize())
    # 释放线程锁
    lock.release()


# 生成若干个生产者
def writer(queue, loops):
    for i in range(loops):
        writeQ(queue)
        sleep(randrange(1, 4))


# 生成若干个消费者
def reader(queue, loops):
    for i in range(loops):
        readQ(queue)
        sleep(randrange(2, 6))


funcs = [writer, reader]
nfuncs = range(len(funcs))


def main():
    nloops = randrange(2, 6)
    q = Queue(32)

    threads = []
    # 创建2个线程运行writer函数和reader函数
    for i in nfuncs:
        t = MyThread(funcs[i], (q, nloops))
        threads.append(t)
    # 开始线程
    for i in nfuncs:
        threads[i].start()

    # 等待2个线程结束
    for i in nfuncs:
        threads[i].join()
    print('所有的工作完成')


if __name__ == '__main__':
    main()
