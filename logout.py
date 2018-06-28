#coding=utf-8
import requests

r = requests.get('http://127.0.0.1:8222/logout/')
r.encoding = r.apparent_encoding
print(r.url)
print(r.text)
input("按任意键退出")
