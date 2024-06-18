import requests
from appium.common.logger import logger

# 发送get请求
response = requests.get('https://www.baidu.com/')

#发送带查询参数的请求
# params = {'key1': 'value1', 'key2': 'value2'}
# response = requests.get('https://www.baidu.com/', params=params)

#加入请求头和请求超时时间
# headers = {'User-Agent': 'Mozilla/5.0'}
# response = requests.get('https://www.baidu.com/', headers=headers, timeout=5)

# 打印状态码
print(response)

'''
1、获取响应结果
response.text    #以字符串形式返回响应内容。
response.content #以字节形式返回响应内容。
response.json()  #以JSON解析并返回响应内容。如果响应内容不是有效的JSON格式，则会抛出JSONDecodeError异常。
'''
# 打印内容
# print(response.text)
# print(response.content)
# print(response.json())


'''
2、获取响应状态
response.status_code  #返回响应的状态码。
response.ok           #返回布尔值，表示请求是否成功（2xx响应码）。
response.raise_for_status()  #如果响应状态码表明请求不成功，则抛出HTTPError异常。
'''
if response.ok == True:
    print("成功访问到百度首页！")
else:
    logger.error("未访问到百度首页，请检查请求url！！")

'''
3、获取响应头信息
response.headers  #返回响应头部的字典形式。
response.headers['header_name']  #返回指定头部字段的值。
'''
# print(response.headers)
#返回指定头部 "字段的值"
print(response.headers['Date'])

'''
3.4. 处理重定向
response.history  #返回一个包含重定向历史的列表，每个元素是一个Response对象。
response.url      #返回最终响应的URL。
'''

'''
3.5. 获取其他响应信息
response.encoding   #返回响应使用的字符编码。
response.cookies    #返回响应的Cookies信息，可以进行进一步操作。
'''

'''
3.6. 指定内容字符集
'''
# 获取结果
response = requests.get('https://www.baidu.com/')

# 按内容展示
html = response.text

# 指定内容的字符集
html = response.content.decode('utf-8')

# 输出结果
print(html)