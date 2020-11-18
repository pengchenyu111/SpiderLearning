import requests

files1 = {'file': open('Python从菜鸟到高手.png', 'rb')}
r1 = requests.post('http://127.0.0.1:5000', files=files1)
print(r1.text)
files2 = {'file': open('Python从菜鸟到高手.png', 'rb')}
r2 = requests.post('http://httpbin.org/post', files=files2)
print(r2.text)
