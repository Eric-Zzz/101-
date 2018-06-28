# -*- coding: UTF-8 -*-

import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import image
import phone
import ipnet
from selenium import webdriver
import tag
import random


def ticket(usr,pwd):
    global frame1
    a=0


    frame1 = driver.current_window_handle
    driver.find_element_by_xpath("//*[@id='mod_head_notice_trigger']/img").click()
    time.sleep(5)
    driver.find_element_by_xpath("//*[@id='login_win_type']/div[2]/div/div/div[2]/a[1]").click()
    time.sleep(5)
    driver.find_element_by_xpath("//*[@id='login_win']/div[1]/ul/li[1]/a").click()
    # time.sleep(3)
    driver.switch_to_frame('_login_frame_quick_')
    driver.find_element_by_id("switcher_plogin").click()
    time.sleep(5)
    driver.find_element_by_xpath("//*[@id='u']").send_keys(usr)
    driver.find_element_by_xpath("//*[@id='p']").send_keys(pwd)
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='login_button']").click()


    handles = driver.window_handles
    for handle in handles:
        if handle == frame1:
            driver.switch_to_window(handle)
    time.sleep(5)
    c=driver.find_element_by_xpath("// *[ @ id = 'mod_head_notice_trigger'] / img")
    if c.get_attribute("src")!="http://i.gtimg.cn/qqlive/images/20150608/avatar.png":
        print("无需滑块验证")
        a=3


    if a==0:
        try:
            time.sleep(5)
            driver.switch_to_frame('_login_frame_quick_')
            time.sleep(3)
            text2 = driver.find_element_by_xpath("//*[@id='newVcodeIframe']/iframe")
            driver.switch_to.frame(text2)
        except:
            print("账号异常")
            return 3




    jj=0
    while a ==0:
        try:
            time.sleep(5)
            driver.find_element_by_xpath("//*[@id='e_reload']").click()
            a = run.crack_slider(driver)
            jj=jj+1
            if j>=10:
                print("滑块验证失败")
                return 2
        except:
            a=1
            print("手动验证成功")

    if a==1:
        try:
            time.sleep(5)
            c = driver.find_element_by_xpath("// *[ @ id = 'mod_head_notice_trigger'] / img")
            if c.get_attribute("src") != "http://i.gtimg.cn/qqlive/images/20150608/avatar.png":
                print("滑块验证成功")
            else:
                print("账号密码错误")
                a=2
                # time.sleep(1)
                return 1
        except:
            print("网络错误导致验证成功却无法登陆")
            a=2
            # time.sleep(1)
            return 1


    if a==1 or a ==3:
        time.sleep(5)
        handles = driver.window_handles
        for handle in handles:  # 切换窗口（切换到有道）
            if handle == frame1:
                driver.switch_to_window(handle)


        submitBtn = driver.find_element_by_css_selector(idols["刘人语"])  # 审查提交按钮的name
        driver.execute_script("arguments[0].scrollIntoView()", submitBtn)  # 使得提交按钮可点的重要代码
        driver.execute_script(js)
        time.sleep(5)
        driver.find_element_by_css_selector(idols["刘人语"]).click()

        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='vote_popper']/div[2]/div/div[2]/div[1]/div[2]/a").click()
        #验证成功流程





def vote(frame,i,j):
    time.sleep(5)
    handles = driver.window_handles
    for handle in handles:  # 切换窗口（切换到有道）
        if handle == frame:
            driver.switch_to_window(handle)
    submitBtn = driver.find_element_by_css_selector(idols[star[j]])  # 审查提交按钮的name
    driver.execute_script("arguments[0].scrollIntoView()", submitBtn)  # 使得提交按钮可点的重要代码
    driver.execute_script(js)
    time.sleep(5)
    driver.find_element_by_css_selector(idols[star[j]]).click()

    time.sleep(5)
    driver.find_element_by_xpath("//*[@id='vote_popper']/div[2]/div/div[2]/div[1]/div[2]/a").click()

    time.sleep(5)
    driver.get_screenshot_as_file('{0}.png'.format(j))
    tag.tagimage('{0}.png'.format(j), call,star[j],i)
    driver.find_element_by_xpath("//*[@id='vote_popper']/div[2]/div/div[1]/a[2]/i").click()

def getphoneNum():
    phoneNum=phone.getphone()
    print("手机号",phoneNum)
    time.sleep(5)
    driver.find_element_by_xpath("//*[@id='phoneNum']").click()
    driver.find_element_by_xpath("//*[@id='phoneNum']").clear()
    driver.find_element_by_xpath("//*[@id='phoneNum']").send_keys(phoneNum)



def getnumber(i,j):
    driver.find_element_by_xpath("//*[@id='vote_popper']/div[2]/div/div[3]/div/div[3]/a[1]").click()

    pwd=phone.getnumber(i)
    print(pwd)
    if pwd=="000":
        result.write(qq[i][0] + "----" + qq[i][1] + "----"+"手机号验证失败\n")
        return 1


    while 1:
        if len(pwd)==6:
            driver.find_element_by_xpath("//*[@id='codeNum']").send_keys(pwd)
            driver.find_element_by_xpath("//*[@id='confirmBind']").click()
            time.sleep(5)
            break

    time.sleep(5)
    driver.find_element_by_xpath("//*[@id='vote_popper']/div[2]/div/div[2]/div[1]/div[2]/a").click()
    time.sleep(5)
    vot2 = driver.find_element_by_xpath('//*[@id="vote_popper"]/div[2]/div/div[2]/div[1]/div[2]/a').get_attribute(
        'class')
    if vot2 == "z_btn_vote z_disabled":
        print("验证成功并投票")
        # print(star[j])
        time.sleep(5)
        newstar=["刘人语"]
        driver.get_screenshot_as_file('reyi.png')
        tag.tagimage('reyi.png', call,"刘人语",i)
        success.write(qq[i][0] + "----" + qq[i][1] + "----" + "点赞成功\n")
        driver.find_element_by_xpath("//*[@id='vote_popper']/div[2]/div/div[1]/a[2]/i").click()
        return 2


def dophone():
    getphoneNum()
    time.sleep(5)
    vot3 =driver.find_element_by_xpath("//*[@id='vote_popper']/div[2]/div/div[3]/div/div[3]/a[1]").get_attribute(
        'class')
    if vot3=="z_btn_send send_code z_disabled":
        dophone()
    elif vot3=="z_btn_send send_code":
        get=getnumber(i,j)
        if get ==1:
            return 1
#
# #
def changeip(i):
    if i%2==0:
        ipnet.disconnect()
        print("正在断开IP")
        time.sleep(5)
        print("开始连接Ip,请耐心等待")
        # time.sleep(5)
        ran=random.randint(1,436)
        ipnet.connect(ip[ran])
        # time.sleep(5)
        ii = 0
        # print(ii)
        while ii>=0:
            net_return=ipnet.getstate()
            ii = ii + 1
            time.sleep(5)
            if net_return=="0":
                print("IP连接成功")
                ipnet.getstate()
                return
            if ii>=8:
                print("IP更换失败，重新选择IP")
                changeip(i)


idols={"刘人语":".btn_vote.player_vote[data-id='1661536'][data-name='刘人语']",
       "孟美岐": ".btn_vote.player_vote[data-id='1503945'][data-name='孟美岐']",
       "吴宣仪": ".btn_vote.player_vote[data-id='1503935'][data-name='吴宣仪']",
       "yamy": ".btn_vote.player_vote[data-id='1661534'][data-name='yamy']",
       "段奥娟": ".btn_vote.player_vote[data-id='1661526'][data-name='段奥娟']",
       "李紫婷": ".btn_vote.player_vote[data-id='1661522'][data-name='李紫婷']",
       "杨超越": ".btn_vote.player_vote[data-id='1661517'][data-name='杨超越']",
       "紫宁": ".btn_vote.player_vote[data-id='1661496'][data-name='紫宁']",
       "赖美云": ".btn_vote.player_vote[data-id='1661543'][data-name='赖美云']",
       "杨芸晴": ".btn_vote.player_vote[data-id='150054'][data-name='杨芸晴']",
       "傅菁": ".btn_vote.player_vote[data-id='1661523'][data-name='傅菁']",
       "戚砚笛": ".btn_vote.player_vote[data-id='1660161'][data-name='戚砚笛']",
       "徐梦洁": ".btn_vote.player_vote[data-id='1661514'][data-name='徐梦洁']",
       "李子璇": ".btn_vote.player_vote[data-id='1661498'][data-name='李子璇']",
       "吕小雨": ".btn_vote.player_vote[data-id='1561907'][data-name='吕小雨']",
       "吴映香": ".btn_vote.player_vote[data-id='1512788'][data-name='吴映香']",
       "强东玥": ".btn_vote.player_vote[data-id='1661553'][data-name='强东玥']",
       "陈意涵": ".btn_vote.player_vote[data-id='1661556'][data-name='陈意涵']",
       "许靖韵": ".btn_vote.player_vote[data-id='191089'][data-name='许靖韵']",}


users = None
user = None
username = None
password = None
users1 = None
user1 = None
username1 = None
password1 = None
frame1 = None
qq=[]
ip=[]
ym=[]
star=[]
star.append("刘人语")
call=""
js = "var q=document.documentElement.scrollTop=50"
result= None
success = None
driver=None
def readtxt():
    global call

    with open('C:\\ticket\\qq.txt') as f:
        users = f.read()
    users = users.strip().rstrip().replace('\r\n', '\n').replace("\t","").split('\n')
    for i in range(len(users)):
        user = users[i].split('----')
        if len(user)!=1:
            qq.append(user)

    with open('C:\\ticket\\ip.txt') as f:
        users2 = f.read()
    users2 = users2.strip().replace('\r\n', '\n').split('\n')
    for i in range(len(users2)):
        user2 = users2[i].split(' ')
        user2=user2[1].split('"')
        user2=user2[1]
        ip.append(user2)

    with open('C:\\ticket\\ym.txt') as ef:
        users1 = ef.read()
    users1 = users1.strip().replace('\r\n', '\n').split('\n')
    for i in range(len(users1)):
        user1 = users1[i].split('----')
        ym.append(user1)

    with open('C:\\ticket\\call.txt') as cf:
        call = cf.read()
    call =call.strip().replace('\r\n', '\n').split('\n')
    call=str(call[0])
    with open('C:\\ticket\\idols.txt') as f:
        users4 = f.read()

    users4 = users4.strip().rstrip().replace('\r\n', '\n').replace("\t","").split('\n')
    for i in range(len(users4)):
        user4 = users4[i].split('----')
    for i in range(len(user4)):
        star.append(user4[i])
    for i in star:
        if i=="刘人语":
            star.remove(i)
    while '' in star:
        star.remove('')

    print("别家小姐姐",star)





readtxt()
i = 0
j = 0
dop = 0
try:

    for i in range(len(qq)):
        try:
            result = open('C:\\ticket\\error.txt', 'a')
            success = open('C:\\ticket\\success.txt', 'a')
            dop = 0

            changeip(i)

            driver = webdriver.Chrome()
            driver.maximize_window()

            run = image.CrackSlider()
            wait = WebDriverWait(driver, 10)
            driver.get("http://v.qq.com/biu/101_star_web")
            phone.login(ym[0][0], ym[0][1])
            print("当前投票qq账号与密码", qq[i][0], qq[i][1])
            p = ticket(qq[i][0], qq[i][1])
            print("该号码最终情况p:", p)
            if p == 1:
                result.write(qq[i][0] + "----" + qq[i][1] + "----" + "账号密码错误\n")
            elif p == 2:
                result.write(qq[i][0] + "----" + qq[i][1] + "----" + "验证失败，建议重新尝试\n")
            elif p == 3:
                result.write(qq[i][0] + "----" + qq[i][1] + "----" + "账号异常\n")
            else:
                time.sleep(5)
                vot1 = driver.find_element_by_xpath(
                    '//*[@id="vote_popper"]/div[2]/div/div[2]/div[1]/div[2]/a').get_attribute(
                    'class')
                if vot1 == "z_btn_vote z_disabled":
                    print("投票成功")
                    driver.get_screenshot_as_file('reyi.png'.format(i))
                    tag.tagimage('reyi.png'.format(i, j), call, "刘人语", i)
                    success.write(qq[i][0] + "----" + qq[i][1] + "----" + "点赞成功\n")
                    time.sleep(5)
                    driver.find_element_by_xpath("//*[@id='vote_popper']/div[2]/div/div[1]/a[2]/i").click()
                    if len(star) != 0:
                        for j in range(len(star)):
                            vote(frame1, i, j)

                else:
                    dop = dophone()
                    if dop != 1:
                        if len(star) != 0:
                            for j in range(len(star)):
                                vote(frame1, i, j)


                # print(dop)

            time.sleep(5)
            if result!=None:
                result.close()
            driver.quit()
        except Exception:
            print("网络出现错误：1")
            print("跳过当前账号")
            time.sleep(5)
            driver.quit()
            result.write(qq[i][0] + "----" + qq[i][1] + "----" + "网络波动\n")
            if result!=None:
                result.close()
            if success!=None:
                success.close()
except:
    print("网络加载速度过慢")
finally:
    ipnet.disconnect()
    fina=input("按任意键退出")
