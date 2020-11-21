from bs4 import BeautifulSoup

# .classname: 选取class属性值为classname的结点
# nodename：选取节点名为nodename的结点
# #idname：选取id属性值为idname的节点

# 获取属性值：使用tag.attrs['xxx']或直接tag['xxx']
# 获取文本值： tag.get_text()或tag.string

html = '''
<div>
    <ul>
        <li class="item1" value1="1234" value2 = "hello world"><a href="https://geekori.com"> geekori.com</a></li>
        <li class="item"><a href="https://www.jd.com"> 京东商城</a></li>        
    </ul>
    <button id="button1">确定</button>
    <ul>
        <li class="item3"><a href="https://www.taobao.com">淘宝</a></li>
        <li class="item" ><a href="https://www.microsoft.com">微软</a></li>
        <li class="item2"><a href="https://www.google.com">谷歌</a></li>
    </ul>
</div>

'''

soup = BeautifulSoup(html,'lxml')
tags = soup.select('.item')
for tag in tags:
    print(tag)

tags = soup.select('#button1')
print(tags)
tags = soup.select('a')[2:]
for tag in tags:
    print(tag)

