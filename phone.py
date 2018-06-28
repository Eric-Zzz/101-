import requests
import time
import re

L=[]
L1=[]
L2=[]
L3=[]
x=""
b=""
z=""
def login(username,password):
    global x,y,z
    #登录
    r = requests.get('http://api.fxhyd.cn/UserInterface.aspx?action=login&username='+str(username)+'&password='+str(password))
    L=r.text.split('|')
    x=str(L[1])


def getphone():
    global x, y, z
    #手机
    url1="http://api.fxhyd.cn/UserInterface.aspx?action=getmobile&token="+str(x)+"&itemid=17904"
    r1=requests.get(url1)
    L1=r1.text.split("|")
    y=str(L1[1])
    flag1=True
    return y

def getnumber(i):
    global x, y, z
    string =""
    i = 0
    while i<12:
        url2 = "http://api.fxhyd.cn/UserInterface.aspx?action=getsms&token=" + str(x) + "&itemid=17904&mobile=" + str(y) + "&release=1"
        r2 = requests.get(url2)
        L2 = r2.text.split("|")
        if L2[0]!="3001":
            break
        i=i+1
        print("错误编码{0}：第{1}次查询，还未收到验证码".format(L2, i))
        time.sleep(5)
    if L2[0]=="success":
        string = L2[1]
        re.findall(r"\d+\.?\d*", string)
        new = re.findall(r"\d+\.?\d*", string)
        return new[1]
    else:
        print("手机号超时，验证失败")
        return "000"

