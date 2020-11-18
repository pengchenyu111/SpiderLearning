import requests

r1 = requests.get('http://www.baidu.com')
print(r1.cookies)
for key, value in r1.cookies.items():
    print(key, '=', value)

# 获取简书首页内容

# 第一种设置Cookies的方式，直接通过Header设置
headers = {
    'Host': 'www.jianshu.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
    'Cookie': 'Hm_lvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1550805089,1550815557,155116976; locale=zh-CN; read_mode=day; default_font=font2; remember_user_token=W1sxMzYxNDI1OF0sIiQyYSQxMSRWWDhUU0JKOU5oZDZtYjhoblMwclYuIiwiMTU1MTM0Nzk5MS4wMzU3MjI3Il0%3D--04787a1b6cfda5ed5974bf50e178b899e99eb4ec; __yadk_uid=xeqG3EJDiKBRfxVO3j2WeLKEUSNMutrB; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2213614258%22%2C%22%24device_id%22%3A%22169338b879465f-05e36cc0827c6-36657105-3686400-169338b8795759%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%221699465f-05e36cc0827c6-36657105-3686400-169338b8795759%22%7D; _m7e_session_core=f79a4a7802e2ffb7035adf0c44294875; Hm_lpvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1551429715'

}

r2 = requests.get('https://www.jianshu.com', headers=headers)
print(r2.text)

# 另外一种设置Cookie的方式：RequestsCookieJar
headers = {
    'Host': 'www.jianshu.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
}
cookies = 'Hm_lvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1550805089,1550815557,1551167360,1551347976; locale=zh-CN; read_mode=day; default_font=font2; remember_user_token=W1sxMzYxNDI1OF0sIiQyYSQxMSRWWDhUU0JKOU5oZDZtYjhoblMwclYuIiwiMTU1MTM0Nzk5MS4wMzU3MjI3Il0%3D--04787a1b6cfda5ed5974bf50e178b899e99eb4ec; __yadk_uid=xeqG3EJDiKBRfxVO3j2WeLKEUSNMutrB; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2213614258%22%2C%22%24device_id%22%3A%22169338b879465f-05e36cc0827c6-36657105-3686400-169338b8795759%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22169338b879465f-05e36cc0827c6-36657105-3686400-169338b8795759%22%7D; _m7e_session_core=f79a4a7802e2ffb7035adf0c44294875; Hm_lpvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1551429715'
jar = requests.cookies.RequestsCookieJar()
for cookie in cookies.split(';'):
    # 继续拆分出key，value，1为最大分割数
    key, value = cookie.split('=', 1)
    jar.set(key, value)
r3 = requests.get('http://www.jianshu.com', cookies=jar, headers=headers)
print(r3.text)
