import os

# 以读写模式打开urls.txt文件
f = open('./files/urls.txt', 'r+')
# 保存当前读上来的文本
url = ''
while True:
    # 从urls.txt文件读一行文本
    url = f.readline()
    # 将最后的行结束符去掉
    url = url.rstrip()
    # 当读上来的是空串，结束循环
    if url == '':
        break
    else:
        # 输出读上来的行文本
        print(url)
print('-----------')
# 将文件指针重新设为0
f.seek(0)
# 读urls.txt文件中的所有行
print(f.readlines())
# 向urls.txt文件中添加一个新行
f.write('https://jiketiku.com' + os.linesep)
#  关闭文件
f.close()
# 使用'a+'模式再次打开urls.txt文件
f = open('./files/urls.txt', 'a+')
# 定义一个要写入urls.txt文件的列表
urlList = ['https://geekori.com' + os.linesep, 'https://www.google.com' + os.linesep]
# 将urlList写入urls.txt文件
f.writelines(urlList)
# 关闭urls.txt文件
f.close()
