import threading
from time import sleep, ctime


# 线程函数，index表示整数类型的索引，sec表示休眠时间，单位：秒
def fun(index, sec):
    print('开始执行', index, ' 时间:', ctime())
    # 休眠sec秒
    sleep(sec)
    print('结束执行', index, '时间:', ctime())


def main():
    # 创建第1个Thread对象，通过target关键字参数指定线程函数fun，传入索引10和休眠时间（4秒）
    thread1 = threading.Thread(target=fun, args=(10, 4))
    # 启动第1个线程
    thread1.start()
    # 创建第2个Thread对象，通过target关键字参数指定线程函数fun，传入索引20和休眠时间（2秒）
    thread2 = threading.Thread(target=fun, args=(20, 2))
    # 启动第2个线程
    thread2.start()
    # 等待第1个线程函数执行完毕
    thread1.join()
    # 等待第2个线程函数执行完毕
    thread2.join()


if __name__ == '__main__':
    main()
