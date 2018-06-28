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
