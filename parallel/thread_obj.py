import threading
from time import sleep, ctime


# 线程对象对应的类
class MyThread(object):
    # func表示线程函数，args表示线程函数的参数
    def __init__(self, func, args):
        # 将线程函数与线程函数的参数赋给当前类的成员变量
        self.func = func
        self.args = args

    # 线程启动时会调用该方法
    def __call__(self):
        # 调用线程函数，并将元组类型的参数值分解为单个的参数值传入线程函数
        self.func(*self.args)


# 线程函数
def fun(index, sec):
    print('开始执行', index, ' 时间:', ctime())
    # 延迟sec秒
    sleep(sec)
    print('结束执行', index, '时间:', ctime())


def main():
    print('执行开始时间:', ctime())
    # 创建第1个线程，通过target关键字参数指定了线程对象（MyThread），延迟4秒
    thread1 = threading.Thread(target=MyThread(fun, (10, 4)))
    # 启动第1个线程
    thread1.start()
    # 创建第2个线程，通过target关键字参数指定了线程对象（MyThread），延迟2秒
    thread2 = threading.Thread(target=MyThread(fun, (20, 2)))
    # 启动第2个线程
    thread2.start()
    # 创建第3个线程，通过target关键字参数指定了线程对象（MyThread），延迟1秒
    thread3 = threading.Thread(target=MyThread(fun, (30, 1)))
    # 启动第3个线程
    thread3.start()
    # 等待第1个线程函数执行完毕
    thread1.join()
    # 等待第2个线程函数执行完毕
    thread2.join()
    # 等待第3个线程函数执行完毕
    thread3.join()
    print('所有的线程函数已经执行完毕:', ctime())


if __name__ == '__main__':
    main()
