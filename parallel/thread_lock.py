from atexit import register
import random
from threading import Thread, Lock, currentThread
from time import sleep, ctime

# 创建线程锁对象
lock = Lock()


def fun():
    # 获取线程锁权限
    lock.acquire()
    # for循环已经变成了原子操作
    for i in range(5):
        print('Thread Name', '=', currentThread().name, 'i', '=', i)
        # 休眠一段时间（1到4秒）
        sleep(random.randint(1, 5))
    # 释放线程锁，其他线程函数可以获得这个线程锁的权限了
    lock.release()


def main():
    # 通过循环创建并启动了3个线程
    for i in range(3):
        Thread(target=fun).start()


# 当程序结束时会调用这个函数
@register
def exit():
    print('线程执行完毕:', ctime())


if __name__ == '__main__':
    main()
