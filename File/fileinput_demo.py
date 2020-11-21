import fileinput

# 使用input方法打开urls.txt文件
fileobj = fileinput.input('./files/urls.txt')
# 输出fileobj的类型
print(type(fileobj))
# 读取urls.txt文件第1行
print(fileobj.readline().rstrip())
# 通过for循环输出urls.txt文件的其他行
for line in fileobj:
    line = line.rstrip()
    # 如果file不等于空串，输出当前行号和内容
    if line != '':
        print(fileobj.lineno(), ':', line)
    else:
        # 输出当前正在操作的文件名
        # 必须在第1行读取后再调用，否则返回None
        print(fileobj.filename())
