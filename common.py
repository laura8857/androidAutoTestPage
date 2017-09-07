# -*- coding: utf-8 -*-

import random
import json

import pymysql
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import requests
import os
from pymongo import *
from selenium.webdriver.common.by import By

from deepblu_lib import log
import action
import time
import datetime
from appium.webdriver.common.touch_action import TouchAction


# 隨機字串
def randomword(size=10, chars=""):
    return ''.join(random.choice(chars) for x in range(size))


def read_json(file_path):
    empty = {}
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
            return data
        except Exception as e:
            print('[Error][read_json] %s' % (e))
            return empty
    else:
        print('[Error][read_json] The json file path is not exist, %s' % (file_path))
        return empty


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


# screenshot
def screenshot(file_name):
    directory = '%s/' % os.getcwd() + 'AndroidAppTest/' + time.strftime("%Y%m%d") + '/'
    if not os.path.exists(directory):  # 先確認資料夾是否存在
        os.makedirs(directory)
    # print(directory)
    screenshot = action.driver.save_screenshot(directory + time.strftime('%H%M%S') + '_' + file_name + ".png")


# 檢查是否抓元件
def wait(type=None, el=None, time=None):
    if type == 'id':
        type = By.ID
    elif type == 'class':
        type = By.CLASS_NAME
    elif type == 'name':
        type = By.NAME
    elif type == 'tag':
        type = By.TAG_NAME
    elif type == 'xpath':
        type = By.XPATH
    else:
        type = By.ID

    if time == None:
        time = 10

    try:
        waite_element = WebDriverWait(action.driver, time).until(EC.presence_of_element_located((type, el)))
        return True
    except Exception as e:
        screenshot("Error")
        log("[Error] The element: %s can't be found. %s" % (el, e), 'w')
        return False


def kill_app():
    log('[kill app] start')
    action.driver.close_app()
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


def browser():
    os.popen("adb shell am start -a android.intent.action.VIEW -d 'http://stackoverflow.com/?uid=isme\&debug=true'")


def home_screen():
    back()
    home()
    home()
    back()


def home():
    action.driver.press_keycode(3)


def back():
    action.driver.press_keycode(4)


def enter():
    action.driver.press_keycode(66)


def sleep(x):
    time.sleep(x)


def size():
    dict = {}
    dict = action.driver.get_window_size()
    list = []
    list.append(dict['height'])
    list.append(dict['width'])
    # print("H: "+str(list[0]))
    # print("W: "+str(list[1]))

    return list


# 0.8滑到0.1 大滑動
def swipeup():
    try:
        # 絕對位置 起始點 結束點
        list = size()
        startx = list[1] * 0.2
        starty = list[0] * 0.8
        endy = list[0] / 10
        # print("x1:" + str(startx) + " y1:" + str(starty) + " x2:" + str(startx) + " y2:" + str(endy))
        action.driver.swipe(startx, starty, startx, endy, 500)
        # driver.swipe(640,2320,640,400,100)
    except Exception as e:
        log(e, 'w')


# 14/16滑到11/16  小滑動
def swipeup2():
    try:
        # 絕對位置 起始點 結束點
        list = size()
        startx = list[1] * 0.2
        starty = list[0] * 0.875
        endy = list[0] * 0.6875
        # print("x1:" + str(startx) + " y1:" + str(starty) + " x2:" + str(startx) + " y2:" + str(endy))
        action.driver.swipe(startx, starty, startx, endy, 500)
        # driver.swipe(640,2320,640,400,100)
    except Exception as e:
        log(e, 'w')


def isElementPresent(by):
    try:
        action.driver.find_element_by_xpath(by)

        return 1

    except Exception as e:
        log(e, 'w')
        print("failed")
        return 0


def browser():
    os.popen("adb shell am start -a android.intent.action.VIEW -d 'http://stackoverflow.com/?uid=isme\&debug=true'")


# rename the email from AAA@AAA.com to AAAYYYYMMDDHHMMSS@AAA.com
def rm_email(email):
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    tmp = email.split("@")
    new_mail = tmp[0] + now + '@' + tmp[1]

    # update to mongodb
    client = MongoClient("52.197.14.177", 27017)
    client.deepblu.authenticate('deepblu2', 'DGeANYhWyx8prMFgYEj6', mechanism='MONGODB-CR')
    db = client.deepblu

    if db.user.find_one({"email": email}):
        db.user.update_one({"email": email}, {"$set": {"email": new_mail}})
        if db.user.find_one({"email": email}):
            print("Please check DB, the email can't be changed")
        else:
            print("The email already modify to " + new_mail)
    else:
        print("The mail " + email + " can't be found.")
    client.close()


# remove Facebook connection
def rm_fb(email):
    client = MongoClient("52.197.14.177", 27017)
    client.deepblu.authenticate('deepblu2', 'DGeANYhWyx8prMFgYEj6', mechanism='MONGODB-CR')
    db = client.deepblu

    if db.socialId.find_one({"email": email}):
        db.socialId.delete_one({"email": email})
        if db.socialId.find_one({"email": email}):
            print("Please check DB, the fb can't be changed")
        else:
            print("The facebook account is removed.")
    else:
        print("The facebook account " + email + " can't be found.")

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

# remove terms and conditions
def remove_terms_conditions(email):
    # connect to mongo
    client = MongoClient("52.197.14.177", 27017)
    client.deepblu.authenticate('deepblu2', 'DGeANYhWyx8prMFgYEj6', mechanism='MONGODB-CR')
    db = client.deepblu

    if db.user.find_one({"email": email}):
        user = {}
        token = ""
        user = db.user.find_one({"email": email})
        id = str(user['_id'])
        # print(str(id))

    else:
        print("The mail " + email + " can't be found.")
    client.close()

    # connect mysql db
    db = pymysql.connect(host='52.197.14.177', user='root', passwd='54353297', db='test', port=3306, charset='utf8')
    cursor = db.cursor()

    sql = "DELETE FROM deepblu.SignCondition WHERE userId='" + id + "'"

    try:
        cursor.execute(sql)
        db.commit()
        print('Succuss')
    except:
        print('Error')
    db.close()


# 滑動找元件  14/16滑到11/16  先往下滑動 找不到 在往上滑動找
def swip_find_el(type, el, text=None, time=None):
    try:
        # 絕對位置 起始點 結束點
        list = size()
        startx = list[1] * 0.5
        starty = list[0] * 0.875
        endy = list[0] * 0.8125
        starty1 = list[0] * 0.6875
        endy1 = list[0] * 0.5625

        if type == 'id':
            type = By.ID
        elif type == 'class':
            type = By.CLASS_NAME
        elif type == 'name':
            type = By.NAME
        elif type == 'tag':
            type = By.TAG_NAME
        elif type == 'xpath':
            type = By.XPATH
        else:
            type = By.ID

        if time is None:
            time = 8

        if text is None:
            # 先找 找不到從下往上滑
            for x in range(time):
                if wait(type, el, 3):
                    return True
                else:
                    pass
                # 為了避開 深度圖，android 在起始點為深度圖時，無法往上滑
                # 因此有兩個往上滑的起始點
                action.driver.swipe(startx, starty, startx, endy, 500)
                sleep(1)
                action.driver.swipe(startx, starty1, startx, endy1, 500)

            # # 同上，不過是從上往下滑
            # for x in range(time):
            #     if wait(type, el, 3):
            #         return True
            #     else:
            #         pass
            #
            #     action.driver.swipe(startx, endy1, startx, starty, 500)
            #     sleep(1)
            #     action.driver.swipe(startx, endy, startx, starty, 500)
        else:
            get_text = action.driver.find_element(type, el).text
            for x in range(time):
                if wait(type, el, 3):
                    if get_text == text:
                        return True
                else:
                    pass
                    # 為了避開 深度圖，android 在起始點為深度圖時，無法往上滑
                    # 因此有兩個往上滑的起始點
                action.driver.swipe(startx, starty, startx, endy, 500)
                sleep(1)
                action.driver.swipe(startx, starty1, startx, endy1, 500)

            # 同上，不過是從上往下滑
            for x in range(time):
                if wait(type, el, 3):
                    return True
                else:
                    pass

                action.driver.swipe(startx, endy1, startx, starty, 500)
                sleep(1)
                action.driver.swipe(startx, endy, startx, starty, 500)
    except Exception as e:
        log(e, 'w')
        return False


def touch_action_move(type1, el1, type2, el2):
    try:
        if type1 == 'id':
            type1 = By.ID
        elif type1 == 'class':
            type1 = By.CLASS_NAME
        elif type1 == 'name':
            type1 = By.NAME
        elif type1 == 'tag':
            type1 = By.TAG_NAME
        elif type1 == 'xpath':
            type1 = By.XPATH
        else:
            type1 = By.ID

        if type2 == 'id':
            type2 = By.ID
        elif type2 == 'class':
            type2 = By.CLASS_NAME
        elif type2 == 'name':
            type2 = By.NAME
        elif type2 == 'tag':
            type2 = By.TAG_NAME
        elif type2 == 'xpath':
            type2 = By.XPATH
        else:
            type2 = By.ID

        el_start = action.driver.find_element(type1, el1)
        el_end = action.driver.find_element_by_xpath(type2, el2)

        TouchAction(action.driver).press(el_start).move_to(el_end).release().perform()
    except Exception as e:
        log(e, 'w')


def live_feed(limit=None):
    try:
        if limit is None:
            limit = '10'
        url = 'http://test.tritondive.co:8000/apis/discover/v0/post/liveFeed?skip=0&limit=' + limit + '&orderCriteria=media'
        headers = {"Accept-Language": "en"}
        result = requests.get(url, headers=headers)
        last_post = []
        if result.status_code == 200:
            print(result.json()['result']['posts'])
            dict = result.json()['result']['posts']
            # count = len(dict)-1
            count = 0
            print(len(dict))
            print(dict[count]['userName'], dict[count]['postType'], dict[count]['publishTime'])
            print(dict[0]['userName'], dict[0]['postType'], dict[0]['publishTime'])

            tag = ''
            if len(dict[0]['tags']) > 0:
                for x in dict[0]['tags']:
                    tag = tag + x
            else:
                tag = ''
            print(tag)

            if dict[count]['postType'] != 'divelog':
                last_post.append({
                    'user': dict[count]['userName'],
                    'postType': dict[count]['postType'],
                    'time': dict[count]['publishTime'],
                    'content': dict[count]['content'],
                    'likeCount': dict[count]['likeCount'],
                    'commentCount': dict[count]['commentCount'],
                    'shareCount': dict[count]['shareCount'],
                    'tag': tag,
                    'og_title': dict[count]['ogTitle'],
                    'og_desc': dict[count]['ogDescription'],
                    'title': dict[count]['title']
                })
            else:
                # duration 回傳秒數 要記得轉換 scuba為分鐘 free為秒數
                if dict[count]['diveLog']['diveType'] == 'Scuba':
                    dive_type = 'scuba log'
                else:
                    dive_type = 'freedive log'

                max = max_depth(dict[count]['diveLog'])
                last_post.append({
                    'user': dict[count]['userName'],
                    'postType': dive_type,
                    'duration': dict[count]['diveLog']['diveDuration'],
                    'time': dict[count]['publishTime'],
                    'content': dict[count]['content'],
                    'likeCount': dict[count]['likeCount'],
                    'commentCount': dict[count]['commentCount'],
                    'shareCount': dict[count]['shareCount'],
                    'tag': tag,
                    'maxDepth': max

                })

            print(last_post)
            return last_post
        else:
            print('Error')
            return {}
    except Exception as e:
        log(e, 'w')

def max_depth(dict):

    if ('airPressure' in dict):
        airPressure = dict['airPressure']
        # print(airPressure)
    else:
        airPressure = 1000

    if ('waterType' in dict):
        if dict['waterType'] == 1:
            watertype = 102.5
        else:
            watertype = 100
    else:
        watertype = 100

    max_depth = (dict['diveMaxDepth'] - airPressure) /float(watertype)
    max_depth = round(max_depth * 10) / 10
    print(max_depth)

    return max_depth


def test():
    dict = {}
    dict = live_feed()
    print(dict[0]['user'])
