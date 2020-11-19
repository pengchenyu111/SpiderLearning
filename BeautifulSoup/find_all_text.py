from bs4 import BeautifulSoup
import re
html = '''
<div>
    <xyz>Hello World, what's this?</xyz>
    <button>Hello, my button. </button>
    <a href='https://geekori.com'>geekori.com</a>
</div>

'''

soup = BeautifulSoup(html,'lxml')
tags = soup.find_all(text='geekori.com')
print(tags)
tags = soup.find_all(text=re.compile('Hello'))
print(tags)



