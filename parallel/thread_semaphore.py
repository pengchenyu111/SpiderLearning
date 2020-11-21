from threading import BoundedSemaphore

MAX = 3
# 创建信号量对象，并设置了计数器的最大值（也是资源的最大值），计数器不能超过这个值
semaphore = BoundedSemaphore(MAX)
# 输出当前计数器的值，输出结果：3
print(semaphore._value)

# 获取资源，计数器减1
semaphore.acquire()
# 输出结果：2
print(semaphore._value)

# 获取资源，计数器减1
semaphore.acquire()
# 输出结果：1
print(semaphore._value)

# 获取资源，计数器减1
semaphore.acquire()
# 输出结果：0
print(semaphore._value)

# 当计数器为0时，不能再获取资源，所以acquire方法会返回False
# 输出结果：False
print(semaphore.acquire(False))
# 输出结果：0
print(semaphore._value)

# 释放资源，计数器加1
semaphore.release()
# 输出结果：1
print(semaphore._value)

# 释放资源，计数器加1
semaphore.release()
# 输出结果：2
print(semaphore._value)

# 释放资源，计数器加1
semaphore.release()
# 输出结果：3
print(semaphore._value)

# 抛出异常，当计数器达到最大值时，不能再次释放资源，否则会抛出异常
semaphore.release()
