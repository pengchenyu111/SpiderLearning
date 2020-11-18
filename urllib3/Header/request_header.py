from urllib3 import *
import re

disable_warnings()
http = PoolManager()
# 定义天猫的搜索页面URL
# url = 'https://list.tmall.com/search_product.htm?spm=a220m.1000858.1000724.4.53ec3e72bTyQhM&q=%D0%D8%D5%D6&sort=d&style=g&from=mallfp..pc_1_searchbutton#J_Filter'
url = 'http://httpbin.org/get'


# 从headers.txt文件读取HTTP请求头，并将其转换为字典形式
def str2Headers(file):
    headerDict = {}
    f = open(file, 'r')
    # 读取headers.txt文件中的所有内容
    headersText = f.read()
    headers = re.split('\n', headersText)
    for header in headers:
        result = re.split(':', header, maxsplit=1)
        headerDict[result[0]] = result[1]
    f.close()
    return headerDict


headers = str2Headers('headers.txt')
# 请求天猫的搜索页面，并传递HTTP请求头
response = http.request('GET', url, headers=headers)
# 将服务端返回的数据按GB18030格式解码
data = response.data.decode('GB18030')
print(data)
