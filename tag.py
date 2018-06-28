#-*- coding:utf-8 -*-
import datetime
import pytz
import time
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
def tagimage(image_address,call,starname,i):
    #设置所使用的字体
    # print(call)
    print(starname)
    font = ImageFont.truetype("C:\\Windows\\Fonts\\simhei.ttf", 50)

    #打开图片
    imageFile = image_address
    im1 = Image.open(imageFile)

    len(im1.split())  # test
    if len(im1.split()) == 4:
        # prevent IOError: cannot write mode RGBA as BMP
        r, g, b, a = im1.split()
        im1 = Image.merge("RGB", (r, g, b))
        # 画图
        draw = ImageDraw.Draw(im1)
        call=call+"\n"+ str(datetime.datetime.now()).replace(" ",",")+"\n"+"@reyi.exe"
        draw.text((160, 0),call , (135,206,255), font=font)  # 设置文字位置/内容/颜色/字体
        draw = ImageDraw.Draw(im1)
        tz = pytz.timezone('Asia/Shanghai')  # 东八区
        t = datetime.datetime.fromtimestamp(int(time.time()), pytz.timezone('Asia/Shanghai')).strftime(
            '%Y-%m-%d %H:%M:%S')
        name=starname+t.replace(":","-")
        im1.save(u"c:\\ticket\\image\\{0}.jpg".format(name))
    else:
        # 画图
        draw = ImageDraw.Draw(im1)
        call=call+"\n"+ str(datetime.datetime.now()).replace(" ",",")+"\n"+"@reyi.exe"
        draw.text((160, 0), call, (255, 0, 0), font=font)  # 设置文字位置/内容/颜色/字体
        draw = ImageDraw.Draw(im1)
        tz = pytz.timezone('Asia/Shanghai')  # 东八区
        t = datetime.datetime.fromtimestamp(int(time.time()), pytz.timezone('Asia/Shanghai')).strftime(
            '%Y-%m-%d %H:%M:%S')
        name = starname + t.replace(":","-")
        im1.save(u"c:\\ticket\\image\\{0}.jpg".format(name))

