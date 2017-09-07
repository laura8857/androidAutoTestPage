# -*- coding: utf-8 -*-
import os

from appium.webdriver.common.touch_action import TouchAction
from pymongo import MongoClient
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from deepblu_lib import log
import desired_capabilities
from appium import webdriver
import datetime
import requests

driver = None

acc = desired_capabilities.acc
pwd = desired_capabilities.pwd
usr = desired_capabilities.username


def driver_init():
    try:
        global driver
        log('[driver_init] start')
        desired_caps = desired_capabilities.get_desired_capabilities('appPackage',
                                                                     'com.deepblu.android.deepblu.internal')
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        log('[driver_init] end')
    except Exception as e:
        log(e, 'w')


def enter():
    driver.press_keycode(66)


def home():
    driver.press_keycode(3)


def back():
    driver.press_keycode(4)


def sleep(x):
    time.sleep(x)


def size():
    dict = {}
    dict = driver.get_window_size()
    list = []
    list.append(dict['height'])
    list.append(dict['width'])
    return list

# rename the email from AAA@AAA.com to AAAYYYYMMDDHHMMSS@AAA.com
def rm_email(email):
    now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    tmp = email.split("@")
    new_mail = tmp[0] + now + '@' + tmp[1]

    # update to mongodb
    client = MongoClient("52.197.14.177", 27017)
    client.deepblu.authenticate('deepblu2', 'DGeANYhWyx8prMFgYEj6', mechanism='MONGODB-CR')
    db = client.deepblu

    if db.user.find_one({"email": email}):
        db.user.update_one({"email": email}, {"$set": {"email": new_mail}})
        if db.user.find_one({"email": email}):
            log("Please check DB, the email can't be changed")
        else:
            log("The email already modify to " + new_mail)
    else:
        log("The mail " + email + " can't be found.")
    client.close()

def getuserId(email):
    url = 'http://test.tritondive.co:3000/1/api/users?filter=%7B%22where%22%3A%7B%22email%22%3A%22' + email + \
          '%22%7D%7D&access_token=YnlyhlAnurDmKOsknbEcR1tuyvrX6Xr9wRR5fwq79WwrQtOlgRC9sQmKmzYAfqqy'
    result = requests.get(url)
    # list=result.json()
    dict = {}
    dict = result.json()[0]
    user_id = dict['id']
    # print("userid:"+str(user_id))
    return user_id


# 註冊驗證號碼
def getusercode(email):
    print('email:' + email)
    url = "http://test.tritondive.co:3000/1/api/users?access_token=YnlyhlAnurDmKOsknbEcR1tuyvrX6Xr9wRR5fwq79Wwr" \
          "QtOlgRC9sQmKmzYAfqqy&filter={\"where\":{\"email\":\"" + email + "\"}}"
    result = requests.get(url)
    if result.status_code == 200:
        if len(result.json()) == 1:
            user_code = ""
            user_code = result.json()[0]['code']
            print("usercode:" + str(user_code))
            link = "https://test.tritondive.co/apis/user/v0/activeAccount?ownerId=" + result.json()[0][
                'id'] + "&code=" + user_code
            dict = {"code": user_code, "link": link}
            return dict
        else:
            return {}


# 驗證 link
def verify_by_link(url):
    json = {"accept-language": "en"}
    res = requests.get(url, headers=json)

# 使當前token過期
def token_expired(email):
    try:
        # connect to mongo
        client = MongoClient("52.197.14.177", 27017)
        client.deepblu.authenticate('deepblu2', 'DGeANYhWyx8prMFgYEj6', mechanism='MONGODB-CR')
        db = client.deepblu

        if db.user.find_one({"email": email}):
            user = {}
            token = ""
            user = db.user.find_one({"email": email})
            id = user['_id']
            print(str(id))

            for doc in db.AccessToken.find({"userId": id}).sort("created", -1).limit(1):
                token = doc['_id']
                print(token)

            # call api
            url = "http://test.tritondive.co:8000/apis/user/v0/tokenExpire"
            data = {}
            data['accessToken'] = token
            headers = {"Accept-Language": "en"}
            result = requests.post(url, json=data, headers=headers)
            if result.status_code == 200:
                print(result.text)
                return True
        else:
            log("The mail " + email + " can't be found.", "w")
            # print("The mail "+email+" can't be found.")
            return False

        client.close()
    except Exception as e:
        log(e)
        return False

def kill_app():
    log('[kill app] start')
    driver.close_app()
    # os.popen("adb shell am force-stop com.deepblu.android.deepblu.internal")
    log('[kill app] end')


def open_app():
    log('[open app] start')
    os.popen('adb shell am start -n com.deepblu.android.deepblu.internal/'
             'com.deepblu.android.deepblu.screen.loading.LoadingActivity')
    log('[open app] end')


# clear cache and data
def clear_app():
    log('[clear app] start')
    os.popen("adb shell pm clear com.deepblu.android.deepblu.internal")
    log('[clear app] end')

class element:
    def __init__(self, el):
        self.element = el

    def wait(self):
        try:
            log('[wait]' + str(self.element))
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((self.element)))
            return True
        except Exception as e:
            screenshot("[Error][wait]")
            log("[Error][wait] The element source %s: %s can't be found.Message: %s" % (self.element[0], self.element[1],e), lvl='e')
            return False

    def click(self):

        if self.wait():
            try:
                log('[click]' + str(self.element))
                driver.find_element(self.element[0], self.element[1]).click()
                return True
            except Exception as e:
                log("[Error][click] The element source %s: %s can't be clicked.Message: %s" % (self.element[0], self.element[1], e),
                    lvl='e')
                return False
        else:
            log("[Error][click] The element source %s: %s can't be clicked." % (self.element[0], self.element[1]),
                lvl='e')
            return False

    def input(self, words):
        if self.wait():
            try:
                log('[input]' + str(self.element))
                driver.find_element(self.element[0], self.element[1]).clear()
                driver.find_element(self.element[0], self.element[1]).send_keys(words)
                return True
            except Exception as e:
                log("[Error][input] The element source %s: %s can't be input data.Message: %s" % (self.element[0], self.element[1],e),
                    lvl='e')
                return False
        else:
            log("[Error][input] The element source %s: %s can't be input data." % (self.element[0], self.element[1]),
                lvl='e')
            return False




def screenshot(file_name):
    directory = '%s/' % os.getcwd() + 'AndroidAppTest/' + time.strftime("%Y%m%d") + '/'
    if not os.path.exists(directory):  # 先確認資料夾是否存在
        os.makedirs(directory)
    # print(directory)
    path = directory + time.strftime('%H%M%S') + '_' + file_name + ".png"
    log("[Screenshot] %s"% path)
    driver.save_screenshot(path)

class move:
    def __init__(self, el1=None, el2=None):
        if el1 is not None:
            self.el1 = el1
        if el2 is not None:
            self.el2 = el2

    # el1 滑到 el2
    def touch_action_move(self):
        log('[touch_action_move] %s to %s' %(str(self.el1),str(self.el2)))
        try:

            el_start = driver.find_element(self.el1[0], self.el1[1])
            el_end = driver.find_element_by_xpath(self.el2[0], self.el2[1])
            TouchAction(driver).press(el_start).move_to(el_end).release().perform()
        except Exception as e:
            log(e, 'w')
        log('[Error][touch_action_move] %s to %s' % (str(self.el1), str(self.el2)))

    # 14/16滑到11/16  小滑動
    def swipe(self):
        try:
            # 絕對位置 起始點 結束點
            list = size()
            startx = list[1] * 0.2
            starty = list[0] * 0.875
            endy = list[0] * 0.6875
            driver.swipe(startx, starty, startx, endy, 500)
        except Exception as e:
            log(e, 'w')

    # 0.8滑到0.1 大滑動
    def swipe_2(self):
        try:
            # 絕對位置 起始點 結束點
            list = size()
            startx = list[1] * 0.2
            starty = list[0] * 0.8
            endy = list[0] / 10
            driver.swipe(startx, starty, startx, endy, 500)
        except Exception as e:
            log(e, 'w')

    # 滑動找元件  14/16滑到11/16  先往下滑動 找不到 在往上滑動找
    def swip_find_el(self,text=None):
        log('[swip_find_el] %s' % (str(self.el1)))
        try:
            # 絕對位置 起始點 結束點
            list = size()
            startx = list[1] * 0.5
            starty = list[0] * 0.875
            endy = list[0] * 0.8125
            starty1 = list[0] * 0.6875
            endy1 = list[0] * 0.5625


            # 先找 找不到從下往上滑
            for x in range(10):
                if element(self.el1).wait():
                    if text is not None:
                        el_text = driver.find_element(self.el1[0], self.el1[1]).text
                        if el_text == text:
                            return True
                    else:
                        return True
                else:
                    pass
                # 為了避開 深度圖，android 在起始點為深度圖時，無法往上滑
                # 因此有兩個往上滑的起始點
                driver.swipe(startx, starty, startx, endy, 500)
                sleep(1)
                driver.swipe(startx, starty1, startx, endy1, 500)


            # 同上，不過是從上往下滑
            for x in range(time):
                if element(self.el1).wait():
                    return True
                else:
                    pass

                driver.swipe(startx, endy1, startx, starty, 500)
                sleep(1)
                driver.swipe(startx, endy, startx, starty, 500)

        except Exception as e:
            log('[Error][swip_find_el] %s.Message:%s' % (str(self.el1),e), 'w')
            return False