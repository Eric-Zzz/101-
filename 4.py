#coding=utf-8
import urllib
import requests
from urllib import request
from urllib import parse
import time
import sys
import importlib
importlib.reload(sys)


ip=[]
def api():
    global x,y,z,ip
    r = requests.get(' http://127.0.0.1:8222/api/')
    r.encoding = r.apparent_encoding
    print(r.url)
    print(r.text)
def getstate():
    global x,y,z,ip
    r = requests.get('http://127.0.0.1:8222/getstate/')
    r.encoding = r.apparent_encoding
    # print(r.url)
    print(r.text)
    M=[]
    M=r.text.split("<code>")
    M=M[1].split("</code>")
    # print(M)
    # print(M[0])
    return M[0]


def getStableLines():
    global x, y, z, ip
    r = requests.get('http://127.0.0.1:8222/getStableLines/')
    r.encoding = r.apparent_encoding
    print(r.url)
    print(r.text)

def connect(ipname):
    global x, y, z, ip
    values = {'servername':ipname,'linktype':u'0'}
    data = parse.urlencode(values).encode('utf-8')  # 提交类型不能为str，需要为byte类型
    # print(data)
    address='http://127.0.0.1:8222/connect/?%s'%data
    address=address.replace("b", "").replace("'","")
    print("当前连接节点",ipname)
    response = urllib.request.urlopen(address)
    # response = urllib.request.urlopen('http://127.0.0.1:8222/connect/')
    # r = response.read().decode('utf-8')
    # print(r)


def disconnect():
    global x, y, z, ip
    r = requests.get('http://127.0.0.1:8222/disconnect/')
    r.encoding = r.apparent_encoding
    # print(r.url)
    # print(r.text)


def logout():
    global x, y, z, ip
    r = requests.get('http://127.0.0.1:8222/logout/')
    r.encoding = r.apparent_encoding
    print(r.url)
    print(r.text)


def getuserinfo():
    global x, y, z, ip
    r = requests.get('http://127.0.0.1:8222/getuserinfo/')
    r.encoding = r.apparent_encoding
    print(r.url)
    print(r.text)

def test():
    global x, y, z, ip
    r = requests.get('http://47.106.180.108:8081/Index-generate_api_url.html?packid=7&fa=5&qty=10&port=1&format=txt&ss=1&css=&pro=&city=')
    r.encoding = r.apparent_encoding
    print(r.url)
    print(r.text)
# api()
# getuserinfo()
# getstate()
# getStableLines()
# connect("福建福州电信-036")
# disconnect()
# logout()
# i = 0
# while i <= 10:
#     getstate()
#     i = i + 1
#     time.sleep(8)
# px =request.ProxyHandler({"http":"118.253.4.200:12221"})
#
# opener=request.build_opener(px)
# req = requests.get('http://v.qq.com/biu/101_star_web')
# res=opener.open(req)
# request.install_opener(opener)
# res=request.urlopen(req)



# def use_proxy(proxy_addr,url):
#     proxy=urllib.request.ProxyHandler({'http':proxy_addr})
#     opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
#     urllib.request.install_opener(opener)
#     data=urllib.request.urlopen(url).read().decode('utf8')
#     return data
#
# proxy_addr=':118.253.4.200:12221'
# data=use_proxy(proxy_addr,'http://v.qq.com/biu/101_star_web')
# print(len(data))
#

# proxies = {
#   "http": "http://118.253.4.200:12221",
#   "https": "https://118.253.4.200:12221",
# }
#
# response = requests.get("https://www.baidu.com", proxies=proxies)
# print(response.status_code)

# proxies = { "http": "http://118.253.4.200:12221", "https": "http://118.253.4.200:12221", }
# requests.get(pro = ['1.119.129.2:8080', '115.174.66.148', '113.200.214.164']  # 在(http://www.xicidaili.com/wt/)上面收集的ip用于测试
# # 没有使用字典的原因是 因为字典中的键是唯一的 http 和https 只能存在一个 所以不建议使用字典
import requests

proxies = {
    "http": "http://118.253.4.200:12221"  # 代理ip
}

headers = {
    "User_Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Referer": "http://www.baidu.com"
}

http_url = "http://www.baidu.com"
res = requests.get(url=http_url, headers=headers, proxies=proxies, timeout=30)
print(res.text)
if res.status_code == 200:
    print(u"访问网页成功")

else:
    print(u"代理ip错误"  )
