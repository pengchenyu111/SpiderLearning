from urllib.parse import urlsplit, urlunsplit

result = urlsplit('https://search.jd.com/Searchprint;hello?keyword=Python从菜鸟到高手&enc=utf-8#comment')
print('scheme：', result.scheme)
print('netloc：', result.netloc)
# 与urlparse相比：path 包含path和params
print('path：', result.path)
print('query：', result.query)
print('fragment：', result.fragment)
print('-----------------')

# 指定scheme，忽略fragment部分
result = urlsplit('search.jd.com/Searchprint;hello?keyword=Python从菜鸟到高手&enc=utf-8#comment', scheme='ftp',
                  allow_fragments=False)
print('scheme：', result.scheme)
print('fragment：', result.fragment)
print('----------------')

# 使用urlunsplit函数合并，注意path部分
data = ['https', 'search.jd.com', 'Searchprint;world', 'keyword=Python从菜鸟到高手&enc=utf-8', 'comment']
print(urlunsplit(data))
