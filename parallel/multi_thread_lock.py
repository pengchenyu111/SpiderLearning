import _thread as thread
from time import sleep, ctime


# 线程函数，index是一个整数类型的索引，sec是休眠时间（单位：秒），lock是锁对象
def fun(index, sec, lock):
    print('开始执行', index, '执行时间：', ctime())
    # 休眠sec秒
    sleep(sec)
    print('执行结束', index, '执行时间：', ctime())
    # 释放锁对象
    lock.release()


def main():
    # 创建第1个锁对象
    lock1 = thread.allocate_lock()
    # 获取锁（相当于把锁锁上）
    lock1.acquire()
    # 启动第1个线程，并传入第1个锁对象，10是索引，4是休眠时间，lock1是锁对象
    thread.start_new_thread(fun, (10, 4, lock1))
    # 创建第2个锁对象
    lock2 = thread.allocate_lock()
    # 获取锁（相当于把锁锁上）
    lock2.acquire()
    # 启动第2个线程，并传入第2个锁对象，20是索引，2是休眠时间，lock2是锁对象
    thread.start_new_thread(fun, (20, 2, lock2))
    # 使用while循环和locked方法判断lock1和lock2是否被释放
    # 只要有一个没有释放，while循环就不会退出
    while lock1.locked() or lock2.locked():
        pass


if __name__ == '__main__':
    main()
