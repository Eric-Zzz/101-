

import requests
import time
import re
import os

L=[]
L1=[]
L2=[]
L3=[]
x=""
b=""
z=""

import sys

mystr=os.popen("chrome")  #popen与system可以执行指令,popen可以接受返回对象
mystr=mystr.read() #读取输出
print("hello",mystr)


def login():
    global x,y,z
    # r = requests.get(' http://127.0.0.1:8222/api/')
    # r = requests.get('http://127.0.0.1:8222/getstate/')
    # r = requests.get('http://127.0.0.1:8222/getStableLines/')
    # r = requests.get('http://127.0.0.1:8222/connect/')
    # r = requests.get('http://127.0.0.1:8222/disconnect/')
    # r = requests.get('http://127.0.0.1:8222/logout/')
    # r = requests.get('http://127.0.0.1:8222/getuserinfo/')
    # r = requests.get('http://56ji.cn:7777/Login?uName=Ying&pWord=Ying0104')
    # print(r.status_code)    # 获取返回状态
    # print(r.url)
    # print(r.text)   #打印解码后的返回数据
    # L=r.text.split('|')
    # print(L)
    # x=str(L[1])

login()
# def getphone(flag1):
#     global x, y, z
#     flag1=False
#     #手机
#     url1="http://api.fxhyd.cn/UserInterface.aspx?action=getmobile&token="+str(x)+"&itemid=17904"
#     r1=requests.get(url1)
#     # print(url1)
#     # print(r1.text)
#     L1=r1.text.split("|")
#     # print(L1)
#     y=str(L1[1])
#     flag1=True
#     return y
#
# def getnumber(flag2):
#     global x, y, z
#     flag2=False
#     string =""
#     i = 0
#     while i<20:
#         # 获取短信
#         url2 = "http://api.fxhyd.cn/UserInterface.aspx?action=getsms&token=" + str(x) + "&itemid=17904&mobile=" + str(y) + "&release=1"
#         r2 = requests.get(url2)
#         # print(r2.text)
#         L2 = r2.text.split("|")
#         # print(L2)
#         if L2[0]!="3001":
#             break
#         i=i+1
#         time.sleep(5)
#     # print(len(L2))
#     if len(L2)!=1:
#         string = L2[1]
#         # print(string)
#         re.findall(r"\d+\.?\d*", string)
#         new = re.findall(r"\d+\.?\d*", string)
#         # print(new[1])
#         flag2=True
#         return new[1]
#     else:
#         print("手机号超时，验证失败")
