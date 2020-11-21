import threading
from time import sleep, ctime


# 从Thread类派生的子类
class MyThread(threading.Thread):
    # 重写父类的构造方法，其中func是线程函数，args是传入线程函数的参数，name是线程名
    def __init__(self, func, args, name=''):
        # 调用父类的构造方法，并传入相应的参数值
        super().__init__(target=func, name=name,
                         args=args)

    # 重写父类的run方法
    def run(self):
        self._target(*self._args)


# 线程函数
def fun(index, sec):
    print('开始执行', index, '时间:', ctime())
    # 休眠sec秒
    sleep(sec)
    print('执行完毕', index, '时间:', ctime())


def main():
    print('开始:', ctime())
    # 创建第1个线程，并指定线程名为“线程1”
    thread1 = MyThread(fun, (10, 4), '线程1')
    # 创建第2个线程，并指定线程名为“线程2”
    thread2 = MyThread(fun, (20, 2), '线程2')
    # 开启第1个线程
    thread1.start()
    # 开启第2个线程
    thread2.start()
    # 输出第1个线程的名字
    print(thread1.name)
    # 输出第2个线程的名字
    print(thread2.name)
    # 等待第1个线程结束
    thread1.join()
    # 等待第2个线程结束
    thread2.join()

    print('结束:', ctime())


if __name__ == '__main__':
    main()
