from time import sleep, ctime


def fun1():
    print('开始运行fun1:', ctime())
    # 休眠4秒
    sleep(4)
    print('fun1运行结束:', ctime())


def fun2():
    print('开始运行fun2:', ctime())
    # 休眠2秒
    sleep(2)
    print('fun2运行结束:', ctime())


def main():
    print('开始运行时间:', ctime())
    # 在单线程中调用fun1函数和fun2函数
    fun1()
    fun2()
    print('结束运行时间:', ctime())


if __name__ == '__main__':
    main()
