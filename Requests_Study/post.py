import requests
import json
from requests.auth import HTTPBasicAuth


'''
发送post请求
requests.post(
    url            #必选参数，指定URL地址。
    data=None      #可选参数，传递表单数据。可以是一个字典、字符串或二进制数据。
    json=None      #可选参数，传递JSON数据。将自动将数据编码为JSON格式并设置请求头部的Content-Type为application/json。
    headers=None   #可选参数，指定HTTP请求的头部信息。可以通过字典形式传递。
    cookies=None   #可选参数，传递Cookie信息。可以是字典或CookieJar对象。
    auth=None      #可选参数，用于身份验证，可以是身份验证相关的对象，如HTTPBasicAuth或HTTPDigestAuth等。
    timeout=None   #可选参数，设置请求的超时时间(单位：秒)
    allow_redirects  #可选参数，用于设置是否允许重定向(默认True)。
    **kwargs       #可选参数，用于传递其他参数，例如proxies、verify（SSL验证）等。
)'''

# 发送post请求
response = requests.post('https://www.baidu.com/')

#发送JSON数据的post请求
# url = 'https://www.baidu.com/'
# data = {'key': 'value'}
# headers = {'Content-Type': 'application/json'}
# response = requests.post(url, json=json.dumps(data), headers=headers)

#发送带有身份验证的POST请求
# url = 'https://www.baidu.com/'
# auth = HTTPBasicAuth('username', 'password')
# response = requests.post(url, auth=auth)

#发送带有cookie的post请求
url = 'https://www.baidu.com/'
cookies = {'session_id': '123456'}
response = requests.post(url, cookies=cookies)

print(response.cookies)