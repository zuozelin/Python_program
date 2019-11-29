# from urllib import request

# url ='http://www.baidu.com'
# response = request.urlopen(url,timeout=1)
# print(response.read().decode('utf-8'))

# gbk
# utf-8

from urllib import parse
from urllib import request

data = bytes(parse.urlencode({'word': 'hello'}),encoding= 'utf8')
# print(data)

response = request.urlopen('http://httpbin.org/post', data=data)
print(response.read().decode('utf-8'))

response2 = request.urlopen('http://httpbin.org/get', timeout=1)
print(response2.read())
