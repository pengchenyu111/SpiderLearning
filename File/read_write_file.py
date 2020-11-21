# 以写模式打开test1.txt文件
f = open('./files/test1.txt', 'w')
# 向test1.txt文件写入“I love "，运行结果：7
print(f.write('I love '))
# 向test1.txt文件写入“python"，运行结果：6
print(f.write('python'))
# 关闭test1.txt文件
f.close()
# 以读模式打开test1.txt文件
f = open('./files/test1.txt', 'r')
# 从test1.txt文件中读取7个字节的数据，运行结果：I love
print(f.read(7))
# 从test1.txt文件的当前位置开始读取6个字节的数据，运行结果：python
print(f.read(6))
# 关闭test.txt文件
f.close()
try:
    # 如果test2.txt文件不存在，会抛出异常
    f = open('./files/test2.txt', 'r+')
except Exception as e:
    print(e)
# 用追加可读写模式打开test2.txt文件
f = open('./files/test2.txt', 'a+')
# 向test2.txt文件写入”hello“
print(f.write('hello'))
# 关闭test2.txt文件
f.close()
# 用追加可读写模式打开test2.txt文件

f = open('./files/test2.txt', 'a+')
# 读取test2.txt文件的内容，由于目前文件指针已经在文件的结尾，所以什么都不会读出来
print(f.read())
# 将文件指针设置到文件开始的位置
f.seek(0)
# 读取文件的全部内容，运行结果：hello
print(f.read())
# 关闭test2.txt文件
f.close()
try:
    # 用写入可读写的方式打开test2.txt文件，该文件的内容会清空
    f = open('./files/test2.txt', 'w+')
    # 读取文件的全部内容，什么都没读出来
    print(f.read())
    # 向文件写入”How are you?“
    f.write('How are you?')
    # 重置文件指针到文件的开始位置
    f.seek(0)
    # 读取文件的全部内容，运行结果：How are you?
    print(f.read())
finally:
    # 关闭test2.txt文件，建议在finally中关闭文件
    f.close()
