

from PIL import Image, ImageEnhance
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import cv2
import numpy as np
from io import BytesIO
import time, requests

class CrackSlider():
    """
    通过浏览器截图，识别验证码中缺口位置，获取需要滑动距离，并模仿人类行为破解滑动验证码
    """
    def __init__(self):
        super(CrackSlider, self).__init__()
        # 实际地址
        # self.url = 'http://dun.163.com/trial/jigsaw'
        # driver = webdriver.Chrome()
        # self.wait = WebDriverWait(driver, 20)
        self.zoom = 1

    # def open(self):
        # driver.get(self.url)

    def get_pic(self,driver1):
        time.sleep(2)
        target = WebDriverWait(driver1, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#slideBkg')))
        template = WebDriverWait(driver1, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#slideBlock')))
        target_link = target.get_attribute('src')
        template_link = template.get_attribute('src')
        target_img = Image.open(BytesIO(requests.get(target_link).content))
        template_img = Image.open(BytesIO(requests.get(template_link).content))
        target_img.save('target.jpg')
        template_img.save('template.png')
        # size_orign = target.size
        local_img = Image.open('target.jpg')
        size_loc = local_img.size
        self.zoom = 280 / int(size_loc[0])

    def get_tracks(self, distance):
        # print(distance)
        distance += 20
        v = 0
        t = 0.2
        forward_tracks = []
        current = 0
        mid = distance * 3/5
        while current < distance:
            if current < mid:
                a = 2
            else:
                a = -3
            s = v * t + 0.5 * a * (t**2)
            v = v + a * t
            current += s
            forward_tracks.append(round(s))

        back_tracks = [-3,-3,-2,-2,-2,-2,-2,-1,-1,-1]
        return {'forward_tracks':forward_tracks,'back_tracks':back_tracks}


    def get_tracks1(self, distance):
        track = []
        current = 0
        mid = distance * 3 / 5.
        t = 0.2
        v = 0
        while current < distance:
            if current < mid:
                a = 2.
            else:
                a = -3.
            v0 = v
            v = v0 + a * t
            move = v0 * t + 1 / 2. * a * t * t
            current += move
            track.append(round(move))
        return track
    def match1(self, target, template):
        img_rgb = cv2.imread(target)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)  # 将图像从一个颜色空间转换为另一个颜色空间
        temp = cv2.imread(template, 0)
        run = 1
        w, h = temp.shape[::-1]
        # res = cv2.matchTemplate(img_rgb, temp, cv2.TM_CCOEFF_NORMED)
        res = cv2.matchTemplate(img_gray, temp, cv2.TM_CCOEFF_NORMED)
        L = 0
        R = 1
        flag = 0
        # while run < 20:
        while not flag:
            run += 1
            threshold = (R + L) / 2.
            # print threshold
            if threshold < 0:
                print('get_distance Error')
                return None
            loc = np.where(res >= threshold)
            # print len(loc[1])
            if len(loc[1]) > 1:
                L += (R - L) / 2.
            elif len(loc[1]) == 1:
                print('目标区域起点x坐标为：%d' % loc[1][0])
                flag = 1
            # break
            else:
                R -= (R - L) / 2.
        # 展示圈出来的区域
        # for pt in zip(*loc[::-1]):
        # 	cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (7, 249, 151), 2)
        # cv2.imshow('Detected', img_rgb)
        # # cv2.imshow('aaa', img_gray)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        # try:
        #     os.remove(target)
        # except Exception as e:
        #     print('remove target error: %s' % e)
        #
        # try:
        #     os.remove(template)
        # except Exception as e:
        #     print('remove template error: %s' % e)

        return loc[1][0]


    def match(self, target, template):
        img_rgb = cv2.imread(target)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(template,0)
        run = 1
        w, h = template.shape[::-1]
        # print(w, h)
        res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)

        # 使用二分法查找阈值的精确值
        L = 0
        R = 1
        while run < 20:
            run += 1
            threshold = (R + L) / 2
            # print(threshold)
            if threshold < 0:
                print('Error')
                return None
            loc = np.where( res >= threshold)
            # print(len(loc[1]))
            if len(loc[1]) > 1:
                L += (R - L) / 2
            elif len(loc[1]) == 1:
                # print('目标区域起点x坐标为：%d' % loc[1][0])
                break
            elif len(loc[1]) < 1:
                R -= (R - L) / 2
        # for pt in zip(*loc[::-1]):
        # 	cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (7, 249, 151), 2)
        # cv2.imshow('Detected', img_rgb)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        return loc[1][0]


    def crack_slider(self, driver1):
        # self.open()
        target = 'target.jpg'
        template = 'template.png'
        driver=driver1
        self.get_pic(driver1)
        distance = self.match(target, template)
        # tracks = self.get_tracks((distance+27)*self.zoom)
        tracks = self.get_tracks((distance + 7 )*self.zoom) # 对位移的缩放计算
        # print("zoom", self.zoom)
        # print("tracks",tracks)
        slider = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#tcaptcha_drag_button')))
        # slider = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, 'yidun_slider')))
        ActionChains(driver).click_and_hold(slider).perform()

        for track in tracks['forward_tracks']:
            ActionChains(driver).move_by_offset(xoffset=track, yoffset=0).perform()

        time.sleep(0.5)
        for back_tracks in tracks['back_tracks']:
            ActionChains(driver).move_by_offset(xoffset=back_tracks, yoffset=0).perform()

        # for i in tracks:
        #     ActionChains(driver).move_by_offset(xoffset=i, yoffset=0).perform()
        #     ActionChains(driver).reset_actions()
        #
        ActionChains(driver).move_by_offset(xoffset=-3, yoffset=0).perform()
        ActionChains(driver).move_by_offset(xoffset=3, yoffset=0).perform()
        time.sleep(0.5)
        ActionChains(driver).release().perform()
        # try:
        #     failure = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#slideBkg')))
        #     print("失败了！",failure)
        # except:
        #     print('验证成功')
        #     return 1
        #
        # if failure:
        #     driver.find_element_by_xpath("//*[@id='e_reload']").click()
        #     self.crack_slider(driver1)
        # else:
        #     print('验证成功')
        #     driver.switch_to.parent_frame()
        #     return 1
        # return 0

        time.sleep(2)
        # b=self.is_element_exist(driver,"//*[@id='u']")
        # if b==True:
        #     print("账号密码错误")
        #     return 2
        # failure = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#slideBkg')))
        #
        # if failure:
        #     print("失败了！")
        #     return 0
        # else:
        #     print("成功了!")
        #     return 1
        try:
            failure = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#slideBkg')))
            print("差一点！")
            return 0
        except:
            print('验证成功')
            return 1

    def is_element_exist(self,driver,xpath):
        flag=True
        try:
            driver.find_element_by_xpath(xpath)
            return flag
        except:
            flag = False
            return flag








                # if __name__ == '__main__':
#     c = CrackSlider()
#     c.crack_slider()