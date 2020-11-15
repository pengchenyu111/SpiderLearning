from urllib import request
import base64

url = 'http://localhost:5000'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
    'Host': 'localhost:5000',
    'Authorization': 'Basic ' + str(base64.b64encode(bytes('bill:1234', 'utf-8')), 'utf-8'),

}
req = request.Request(url=url, headers=headers, method="GET")
response = request.urlopen(req)
print(response.read().decode('utf-8'))
