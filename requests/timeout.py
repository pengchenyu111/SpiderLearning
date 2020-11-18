import requests.exceptions

try:
    r = requests.get('https://www.jd.com', timeout=0.001)
    print(r.text)
except requests.exceptions.Timeout as e:
    print(e)

# 抛出连接超时异常
requests.get('https://www.jd.com', timeout=(0.01, 0.001))

# 永久等待，不会抛出超时异常
requests.get('https://www.jd.com', timeout=None)
