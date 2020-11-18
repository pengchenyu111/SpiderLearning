from urllib3 import *

disable_warnings()
http = PoolManager()
# 定义上传文件的服务端Url
url = 'http://localhost:5000'
while True:
    # 输入上传文件的名字
    filename = input('请输入要上传的文件名字（必须在当前目录下）：')
    # 如果什么也未输入，退出循环
    if not filename:
        break
    # 用二进制的方式打开要上传的文件名，然后读取文件的所有内容，使用with语句会自动关闭打开的文件
    with open(filename, 'rb') as fp:
        fileData = fp.read()
    # 上传文件
    response = http.request('POST', url, fields={'file': (filename, fileData)})
    # 输出服务端的返回结果，本例是“文件上传成功”
    print(response.data.decode('utf-8'))
