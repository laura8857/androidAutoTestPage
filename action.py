# -*- coding: utf-8 -*-
# @Time    : 2017/2/7 下午2:15
# @Author  : Yuhsuan
# @File    : TestCases.py
# @Software: PyCharm Community Edition
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from deepblu_lib import log
import desired_capabilities
import os
import time
import GlobalString
import random
import common
from common import screenshot
from appium.webdriver.common.touch_action import TouchAction


# desired_caps = desired_capabilities.get_desired_capabilities('appPackage', 'com.deepblu.android.deepblu.internal',
#                                                              'android')
# driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# init appium driver


def driver_init():
    global driver
    try:
        log('[driver_init] start')
        desired_caps = desired_capabilities.get_desired_capabilities('appPackage',
                                                                     'com.deepblu.android.deepblu.internal',
                                                                     'android')
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        log('[driver_init] end')
    except Exception as e:
        log(e, 'w')


def driver_close():
    try:
        log('[driver_close] start')
        driver.close_app()
        driver.close
        log('[driver_close] end')
    except Exception as e:
        log(e, 'w')


def skip_version_check():
    log('[skip version check] start')
    try:
        if common.wait(type='id', el='android:id/button2', time=5):
            screenshot('skipVersionCheck')
            driver.find_element_by_id('android:id/button2').click()
    except Exception as e:
        log(e, 'w')


def login(email=None, password=None):
    log('[login] start')
    try:
        skip_version_check()
        if email is None:
            email = desired_capabilities.account()
        if password is None:
            password = desired_capabilities.password()
        el = common.wait(type='id', el='com.deepblu.android.deepblu.internal:id/textLogin')
        if el:
            driver.find_element_by_id('com.deepblu.android.deepblu.internal:id/textLogin').click()
            common.sleep(3)
            driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/editTextEmail").send_keys(email)
            common.sleep(3)
            common.back()
            common.sleep(3)
            driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/editTextPassword").send_keys(password)
            common.back()
            common.sleep(3)
            driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/buttonSignUp").click()

            if common.wait(type='xpath',el=GlobalString.create_post):
                screenshot("login")
            else:
                log("Please check the screen shoot")
        else:
            log("Please check the screen shoot")
    except Exception as e:
        log(e, 'w')
    log('[login] end')


def login_skip():
    log('[login_skip] start')
    try:
        el = common.wait(type='id', el='com.deepblu.android.deepblu.internal:id/textLogin')
        if el:
            driver.find_element_by_id('com.deepblu.android.deepblu.internal:id/textLogin').click()
            common.sleep(2)
            common.back()
            driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/buttonSkip").click()

            checkel = common.wait(type='xpath', el=GlobalString.create_post)
            if checkel:
                screenshot('loginSkip')
            else:
                log("Please see screenshot.")
        else:
            log("Please check the screen shoot")
    except Exception as e:
        log(e, 'w')

    log('[login_skip] end')


def logout():
    log('[logout] start')

    try:
        driver.find_element_by_xpath(GlobalString.menu).click()
        common.sleep(3)
        common.swipeup()
        # logout xpath :note5 12 zenfone 10
        driver.find_element_by_xpath(GlobalString.logout).click()
        common.sleep(3)
        el = common.wait(type='id', el="android:id/button1")
        if el:
            driver.find_element_by_id("android:id/button1").click()
        else:
            log("Please check the screen shoot")
        common.sleep(3)
        # verify successful or not
        checkel = common.wait(type='id', el='com.deepblu.android.deepblu.internal:id/textLogin')
        if checkel:
            screenshot("Logout")
        else:
            log('Please check the screenshot')
    except Exception as e:
        log(e, 'w')
    log('[logout] end')


# about page
def about():
    log('[about] start')
    try:
        # menu page
        driver.find_element_by_xpath(GlobalString.menu).click()
        common.sleep(5)

        # about page
        driver.find_element_by_xpath(GlobalString.about).click()
        common.sleep(3)

        screenshot("About")
    except Exception as e:
        log(e, 'w')

    try:
        # app version
        log('[appVersion] start')
        driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/about_version_secondary_text").click()
        common.sleep(3)
        screenshot("appVersion")
        common.back()
        log('[appVersion] end')
    except Exception as e:
        log(e, 'w')

    try:
        # Term&Conditoins
        log('[Term&Condtions] start')
        driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/about_term_primary_text").click()
        common.sleep(3)
        screenshot("Term&CondtionsStart")

        i = 28
        while i > 0:
            common.swipeup()
            i -= 1
        screenshot("Term&ConditionsEnd")
        common.sleep(2)
        common.back()
        log('[Term&Conditions] end')

    except Exception as e:
        log(e, 'w')

    try:
        # Guidelines
        log('[Guidelines] start')
        driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/about_guideline_primary_text").click()
        common.sleep(3)
        screenshot("Guidelines")
        common.sleep(2)
        common.back()
        log('[Guidelines] end')

    except Exception as e:
        log(e, 'w')

    # 返回menu page
    common.back()
    log('[about] end')


# menu page的help
def help():
    log("[Help] start")
    try:
        # menu page
        driver.find_element_by_xpath(GlobalString.menu).click()
        common.sleep(5)
        # help page
        driver.find_element_by_xpath(GlobalString.help).click()
        common.sleep(3)

        path = " //android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]" \
               "/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/" \
               "android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android." \
               "webkit.WebView[1]/android.view.View[2]"
        el = common.wait(type='xpath', el=path)
        if el:
            log("網頁正常出現")
            screenshot("Help")
        else:
            log("\n 網頁沒有load出來")
    except Exception as e:
        log(e, 'w')

    # 返回menu page
    common.back()
    log("[Help] end")


# menu page的app feedback
def appfeedback():
    log("[App feedback] start")
    try:
        # menu page
        driver.find_element_by_xpath(GlobalString.menu).click()
        common.sleep(5)
        # appfeedback page
        driver.find_element_by_xpath(GlobalString.app_feedback).click()
        common.sleep(3)

        optionel = common.wait(type='id', el="com.deepblu.android.deepblu.internal:id/textViewSpinner")
        if optionel:
            driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/textViewSpinner").click()
            common.sleep(2)
            option = driver.find_element_by_xpath(
                "//android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.TextView[" + str(
                    random.randint(1, 4)) + "]")
            optionstring = option.text
            option.click()
            driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/subject_edit").send_keys(
                "[Test Subject] " + optionstring)
            common.back()
            driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/content_edit").send_keys(
                optionstring + "\n" + time.strftime("%Y%m%d%H%M%S") + "\n" + common.randomword(100, GlobalString.bio))
            common.back()
            driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/main_feedback_send_report").click()
            # sumit successful
            submit = common.wait(type='id', el="com.deepblu.android.deepblu.internal:id/feedback_submitted_button")
            if submit:
                screenshot("appfeedback")
                driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/feedback_submitted_button").click()
            else:
                log("Report failed.Please check screenshot.")
                # 返回menu page
                common.back()
        else:
            log("Please check the screen shoot")

    except Exception as e:
        log(e, 'w')
    log("[App feedback] end")


def events():
    log("[Events] start")
    try:
        # menu page
        driver.find_element_by_xpath(GlobalString.menu).click()
        common.sleep(3)
        # events page
        driver.find_element_by_xpath(GlobalString.events).click()
        common.sleep(3)

        path = "//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]" \
               "/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/andr" \
               "oid.view.ViewGroup[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.webkit." \
               "WebView[1]/android.view.View[1]/android.widget.Image[1]"
        el = common.wait(type='xpath', el=path)
        if el:
            log("網頁正常出現")
            screenshot("Events")
        else:
            log("\n 網頁沒有load出來")
    except Exception as e:
        log(e, 'w')
    # 返回menu page
    common.back()
    log("[Events] end")


def academy():
    log('[Academy] start')
    try:
        # menu page
        driver.find_element_by_xpath(GlobalString.menu).click()
        common.sleep(3)
        # events page
        driver.find_element_by_xpath(GlobalString.academy).click()
        common.sleep(3)
        # 等待網頁load出來
        if common.wait(type='xpath',
                       el='//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[3]/android.widget.FrameLayout[2]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]'):
            log("網頁正常出現")
            screenshot("academy")
        else:
            log("\n 網頁沒有load出來")
    except Exception as e:
        log(e, 'w')
    # 返回menu page
    common.back()
    log('[Academy] end')


def userProfile():
    try:
        log("[User Profile] start")

        # 一般方法進入user profile page
        # # menu page
        # driver.find_element_by_xpath(GlobalString.menu).click()
        # common.sleep(5)
        # # user profile page
        # driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/item_menu_user_profile_icon").click()
        # common.sleep(3)

        # 用deepblink 進入user profile page
        os.popen("adb shell am start -W -a android.intent.action.VIEW -d 'deepblu://deepblu.link/Menu/Profile'")
        common.sleep(3)
        screenshot("UserProfile")

        # 返回menu page
        # common.back()
        log("[User Profile] end")
    except Exception as e:
        log(e, 'w')


def editUserProfile():
    log("[Edit User Profile] start")
    # 一般方法進入Edit User Profile page
    # menu page
    # driver.find_element_by_xpath(GlobalString.menu).click()
    # common.sleep(5)
    # # user profile page
    # driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/item_menu_user_profile_icon").click()
    # common.sleep(3)
    # driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/left_button").click()
    # common.sleep(3)

    # deeplink
    os.popen("adb shell am start -W -a android.intent.action.VIEW -d 'deepblu://deepblu.link/Menu/Profile/EditProfile'")
    common.sleep(3)

    screenshot("EditUserProfile")

    # 編輯user profile
    log("[Avatar&Background] start")
    driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/user_profile_edit_avatar").click()
    common.sleep(2)

    # 要求權限
    elask = common.wait(type="id", el='com.android.packageinstaller:id/permission_allow_button')
    if elask:
        driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()

    # # avatar
    # try:
    #     driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/user_profile_edit_avatar").click()
    #     common.sleep(3)
    #     # 第三個資料夾第二張照片
    #     changePhoto("3", "2")
    # except Exception as e:
    #     log(e)
    # #background
    # try:
    #     driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/user_profile_edit_background").click()
    #     common.sleep(3)
    #     # 第二個資料夾第二張照片
    #     changePhoto("2", "2")
    # except Exception as e:
    #     log(e)
    #
    # log("[Avatar&Background] end")

    log("[name] start")
    try:
        # name
        userel = driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/edit_text_user_name")
        Username = userel.text + "_" + time.strftime("%m%d")
        userel.clear()
        userel.send_keys(Username)
        common.back()
        common.swipeup2()
        firstel = driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/edit_text_first_name")
        Firstname = firstel.text + "_" + time.strftime("%m%d")
        firstel.clear()
        firstel.send_keys(Firstname)
        common.back()
        lastel = driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/edittext_last_name")
        Lastname = lastel.text + "_" + time.strftime("%m%d")
        lastel.clear()
        lastel.send_keys(Lastname)
        common.back()
    except Exception as e:
        log(e)

    log("[name] end")

    # 性別   男->女 女->其他 其他->男
    log("[gender] start")
    try:
        # gender1 = driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/spinnerItem").text
        gender = driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/spinnerItem").text
        print("gender:" + gender)
        driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/spinnerItem").click()
        option1 = driver.find_element_by_xpath(
            "//android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout["
            "1]/android.widget.TextView[1]").text
        option2 = driver.find_element_by_xpath(
            "//android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[2]"
            "/android.widget.TextView[1]").text

        if gender == option1:
            driver.find_element_by_xpath(
                "//android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout"
                "[2]/android.widget.TextView[1]").click()
        elif gender == option2:
            driver.find_element_by_xpath(
                "//android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout"
                "[3]/android.widget.TextView[1]").click()
        else:
            driver.find_element_by_xpath(
                "//android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout"
                "[1]/android.widget.TextView[1]").click()
    except Exception as e:
        log(e)
    log("[gender] end")
    common.sleep(2)

    common.swipeup2()
    # country
    log("[country] start")
    try:
        elc = driver.find_element_by_id(
            "com.deepblu.android.deepblu.internal:id/user_profile_edit_region_auto_complete_text_view")
        country = elc.text
        elc.click()
        if country == "Taiwan":
            elc.send_keys("japan")
        else:
            elc.send_keys("taiwan")
        common.sleep(2)

        location = driver.find_element_by_id(
            "com.deepblu.android.deepblu.internal:id/user_profile_edit_region_auto_complete_text_view").location
        x = location['x']
        y = location['y']
        print("location x:" + str(x) + " y:" + str(y))

        list = common.size()
        x1 = list[1] * 0.5
        y1 = y + 260
        print("location x1:" + str(x1) + " y1:" + str(y1))
        TouchAction(driver).press(x=x1, y=y1).release().perform()
        common.sleep(2)
    except Exception as e:
        log(e)

    log("[country] end")

    common.sleep(2)
    common.swipeup2()
    # short bio
    log("[short bio] start")
    try:
        driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/edit_text_short_bio").clear()
        driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/edit_text_short_bio").send_keys(
            common.randomword(100, GlobalString.bio))
        common.sleep(3)
        common.back()
        screenshot("EditUserProfileAfter")
    except Exception as e:
        log(e)
    log("[Edit User Profile] end")

    # non deepblu dive
    log("[Non-deepblu dive] start")
    common.swipeup2()
    common.swipeup2()
    try:
        diveel = driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/user_profile_edit_text_total_dive")
        divenumber = int(diveel.text)
        if divenumber < 99990:
            divenumber = divenumber + 10
        else:
            divenumber = 0
        diveel.clear()
        diveel.send_keys(divenumber)
        common.back()
    except Exception as e:
        log(e)
    log("[Non-deepblu dive] end")

    # save
    try:
        common.swipeup()
        common.sleep(2)
        # common.swipeup()
        # sleep(2)
        driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/user_profile_edit_done_button").click()
    except Exception as e:
        log(e)

    log("[Edit User Profile] end")


    # 將照片換回來
    # try:
    #     driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/left_button").click()
    #     common.sleep(3)
    #     #avatar
    #     driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/user_profile_edit_avatar").click()
    #     common.sleep(2)
    #     # 第三個資料夾第一張照片
    #     changePhoto("3", "1")
    #     common.sleep(2)
    #     #background
    #     driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/user_profile_edit_background").click()
    #     common.sleep(3)
    #     # 第二個資料夾第三張照片
    #     changePhoto("2", "3")
    #     common.sleep(2)
    #     common.swipeup()
    #     common.sleep(2)
    #     common.swipeup()
    #     common.sleep(2)
    #     # save
    #     driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/user_profile_edit_done_button").click()
    # except Exception as e:
    #     log(e)


def post_text():
    log("[Post Text] start")
    try:
        postIcon = GlobalString.create_post
        el = common.wait(type='xpath', el=postIcon)
        if el:
            driver.find_element_by_xpath(postIcon).click()
            common.sleep(2)
            el2 = common.wait(type='id', el="com.deepblu.android.deepblu.internal:id/text_post_group")
            if el2:
                driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/text_post_group").click()
            else:
                log("Please check the screen shoot")
                common.sleep(2)
            driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/post_caption").click()
            content = ""
            content = "[AutoTest]\n" + common.randomword(10, GlobalString.bio) + "\n" + time.strftime("%Y%m%d%H%M%S")
            driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/post_caption").send_keys(content)
            # common.sleep(1)
            # hashtag()
            common.sleep(2)
            driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/btn_control_post").click()
            common.sleep(2)
            el3 = common.wait(type='id', el="android:id/button1")
            if el3:
                driver.find_element_by_id("android:id/button1").click()
            else:
                log("Please check the screen shoot")
            common.sleep(2)
            checkel = common.wait(type='xpath', el=postIcon)
            if checkel:
                screenshot("PostText")
            else:
                log('Please check the screen shoot')
        else:
            log("Please check the screen shoot")
    except Exception as e:
        log(e, 'w')
    log("[Post Text] end")


def post_link():
    log("[Post Link] start")
    try:
        postIcon = GlobalString.create_post
        el = common.wait(type='xpath', el=postIcon)
        if el:
            driver.find_element_by_xpath(postIcon).click()
            common.sleep(2)
            el2 = common.wait(type='id', el="com.deepblu.android.deepblu.internal:id/link_post_group")
            if el2:
                driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/link_post_group").click()
            else:
                log("Please check the screen shoot")
            common.sleep(2)
            link = "https://www.deepblu.com"
            # link = random.choice(GlobalString.link)
            driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/edit_body").send_keys(link)
            common.sleep(2)
            driver.find_element_by_id("android:id/button1").click()
            common.sleep(2)
            content = ""
            content = "[AutoTest]\n" + common.randomword(10, GlobalString.bio) + "\n" + time.strftime(
                "%Y%m%d%H%M%S") + "\n" + link
            # 檢查有沒有抓到內容元件 才能輸入文字
            elcontent = common.wait(type='id', el="com.deepblu.android.deepblu.internal:id/post_caption")
            if elcontent:
                driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/post_caption").send_keys(content)
                # common.sleep(1)
                # hashtag()
                common.sleep(2)
                driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/btn_control_post").click()
                common.sleep(2)
                el3 = common.wait(type='id', el="android:id/button1")
                if el3:
                    driver.find_element_by_id("android:id/button1").click()
                else:
                    log("Please check the screen shoot")
                common.sleep(2)
                checkel = common.wait(type='xpath', el=postIcon)
                if checkel:
                    screenshot("PostLink")
                else:
                    log('Please check the screen shoot')
            else:
                log("Please check the screen shoot")
        else:
            log("Please check the screen shoot")

    except Exception as e:
        log(e, 'w')
    log("[Post Link] end")


def post_photo():
    log("[Post Photo] start")
    try:
        postIcon = GlobalString.create_post
        el = common.wait(type='xpath', el=postIcon)
        if el:
            driver.find_element_by_xpath(postIcon).click()
            common.sleep(2)
            el2 = common.wait(type="id", el="com.deepblu.android.deepblu.internal:id/photo_post_group")
            if el2:
                driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/photo_post_group").click()
            else:
                log("Please check the screen shoot")

            el3 = common.wait(type="id", el="com.android.packageinstaller:id/permission_allow_button")
            if el3:
                driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
                common.sleep(1)
                driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/btn_control_media").click()
                common.sleep(1)
                driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/add_more_media").click()
                common.sleep(2)

                elphoto = driver.find_element_by_xpath(
                    "//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.support.v4.wi"
                    "dget.DrawerLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/andr"
                    "oid.widget.FrameLayout[1]/android.widget.GridView[1]/android.widget.FrameLayout[1]")
                # 選一張照片
                elphoto.click()

                # 選多張照片
                # TouchAction(driver).long_press(elphoto,None,None,5000).perform()
                # el4 = dtool.wait(type="xpath", el="//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.GridView[1]/android.widget.FrameLayout[2]")
                # if el4:
                #     driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.GridView[1]/android.widget.FrameLayout[2]").click()
                #     driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.GridView[1]/android.widget.FrameLayout[3]").click()
                #     driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.GridView[1]/android.widget.FrameLayout[4]").click()
                #
                # driver.find_element_by_id("com.android.documentsui:id/menu_sort").click()
                common.back()
            else:
                elphoto = driver.find_element_by_xpath(
                    "//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget."
                    "DrawerLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget."
                    "FrameLayout[1]/android.widget.GridView[1]/android.widget.FrameLayout[1]")
                TouchAction(driver).long_press(elphoto, None, None, 5000).perform()
                el4 = common.wait(type="xpath",
                                  el="//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.support."
                                     "v4.widget.DrawerLayout[1]/android.widget.LinearLayout[1]/android.widget."
                                     "FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.GridView[1]/"
                                     "android.widget.FrameLayout[2]")
                if el4:
                    driver.find_element_by_xpath(
                        "//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget."
                        "DrawerLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget"
                        ".FrameLayout[1]/android.widget.GridView[1]/android.widget.FrameLayout[2]").click()
                    driver.find_element_by_xpath(
                        "//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget."
                        "DrawerLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget."
                        "FrameLayout[1]/android.widget.GridView[1]/android.widget.FrameLayout[3]").click()
                    driver.find_element_by_xpath(
                        "//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget."
                        "DrawerLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget"
                        ".FrameLayout[1]/android.widget.GridView[1]/android.widget.FrameLayout[4]").click()

                driver.find_element_by_id("com.android.documentsui:id/menu_sort").click()

            content = ""
            content = "[AutoTest]\n" + common.randomword(10, GlobalString.bio) + "\n" + time.strftime("%Y%m%d%H%M%S")
            driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/post_caption").send_keys(content)
            # common.sleep(1)
            # hashtag()
            common.sleep(2)
            driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/btn_control_post").click()
            common.sleep(2)
            el3 = common.wait(type='id', el="android:id/button1")
            if el3:
                driver.find_element_by_id("android:id/button1").click()
            else:
                log("Please check the screen shoot")
            common.sleep(2)
            checkel = common.wait(type='xpath', el=postIcon)
            if checkel:
                screenshot("PostPhoto")
            else:
                log('Please check the screen shoot')
        else:
            log("Please check the screen shoot")

    except Exception as e:
        log(e, 'w')
    log("[Post Photo] end")


def post_video():
    log("[Post Video] start")
    try:
        postIcon = GlobalString.create_post
        el = common.wait(type='xpath', el=postIcon)
        if el:
            driver.find_element_by_xpath(postIcon).click()
            common.sleep(2)

            el2 = common.wait(type="id", el="com.deepblu.android.deepblu.internal:id/video_post_group")
            if el2:
                driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/video_post_group").click()
            else:
                log("Please check the screen shoot")

            # 要求權限
            el3 = common.wait(type="id", el="com.android.packageinstaller:id/permission_allow_button")
            if el3:
                driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
                common.sleep(1)
                driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/btn_control_media").click()
                common.sleep(1)
                driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/add_more_media").click()
                common.sleep(2)

                videoel = common.wait(type="xpath",
                                      el="//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/"
                                         "android.support.v4.widget.DrawerLayout[1]/android.widget.LinearLayout[1]"
                                         "/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget."
                                         "GridView[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]")
                if videoel:
                    driver.find_element_by_xpath(
                        "//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget."
                        "DrawerLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget."
                        "FrameLayout[1]/android.widget.GridView[1]/android.widget.FrameLayout[1]/android.widget."
                        "ImageView[1]").click()
                else:
                    log("Please check the screen shoot")
                common.sleep(2)
                common.back()
            else:
                videoel = common.wait(type="xpath",
                                      el="//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.support"
                                         ".v4.widget.DrawerLayout[1]/android.widget.LinearLayout[1]/android.widget."
                                         "FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.GridView[1]/"
                                         "android.widget.FrameLayout[1]/android.widget.ImageView[1]")
                if videoel:
                    driver.find_element_by_xpath(
                        "//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget."
                        "DrawerLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget."
                        "FrameLayout[1]/android.widget.GridView[1]/android.widget.FrameLayout[1]/android.widget."
                        "ImageView[1]").click()
                else:
                    log("Please check the screen shoot")
            common.sleep(5)
            content = ""
            content = "[AutoTest]\n" + common.randomword(10, GlobalString.bio) + "\n" + time.strftime("%Y%m%d%H%M%S")
            driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/post_caption").send_keys(content)
            # sleep(1)
            # hashtag()
            common.sleep(2)
            driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/btn_control_post").click()
            common.sleep(2)
            el3 = common.wait(type='id', el="android:id/button1")
            if el3:
                driver.find_element_by_id("android:id/button1").click()
            else:
                log("Please check the screen shoot")

            # upload media
            if common.wait(type='id', el='android:id/parentPanel'):
                log('Uploading media')
                for x in range(2):
                    common.sleep(1)
                    if not common.wait(type='id', el='android:id/parentPanel'):
                        log("Finished.")
                        break
            checkel = common.wait(type='xpath', el=postIcon)
            if checkel:
                screenshot("PostVideo")
            else:
                log('Please check the screen shoot')
        else:
            log("Please check the screen shoot")
    except Exception as e:
        log(e, 'w')
    log("[Post Video] end")


# sign up with email
# should be samsung IME
def signup(username=None, email=None, password=None):
    log("[Sign up] start")
    try:
        if username is None:
            username = "test" + time.strftime("%m%d%H%M")
        if email is None:
            email = username + "@deepblu.com"
        if password is None:
            password = 'a12345678'
        el = common.wait(type="id", el="com.deepblu.android.deepblu.internal:id/buttonSignUpWithEmail")
        if el:
            driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/buttonSignUpWithEmail").click()
            common.sleep(2)
            driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/editTextUserName").send_keys(username)
            common.back()
            driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/editTextEmail").send_keys(email)
            common.back()
            driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/editTextPassword").send_keys(password)
            common.back()
            driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/buttonSignUp").click()
            # check signup successful or not
            elcheck = common.wait(type='id', el="com.deepblu.android.deepblu.internal:id/activity_toolbar_title")
            if elcheck:
                screenshot('SignUp')
            else:
                log('Please check the screen shoot')

            log("[Sign up] end")
            return email

        else:
            log("Please check the screen shoot")
    except Exception as e:
        log(e, 'w')


# verify:code/url
def verify(verify='code', Useremail=None):
    log("[Verify] start")
    try:
        # if way ==None:
        #     Useremail = signup()
        # else :
        #     Useremail =way
        # common.sleep(3)
        verifydict = {}
        verifydict = common.getusercode(Useremail)
        if len(verifydict) == 0:
            log("Cannot get verify code.Please check the screen")
        else:
            if verify == "code":
                code = verifydict["code"]
                driver.find_element_by_id(
                    "com.deepblu.android.deepblu.internal:id/fragment_signup_verify_input_1").send_keys(code[0:1])
                driver.find_element_by_id(
                    "com.deepblu.android.deepblu.internal:id/fragment_signup_verify_input_2").send_keys(code[1:2])
                driver.find_element_by_id(
                    "com.deepblu.android.deepblu.internal:id/fragment_signup_verify_input_3").send_keys(code[2:3])
                driver.find_element_by_id(
                    "com.deepblu.android.deepblu.internal:id/fragment_signup_verify_input_4").send_keys(code[3:4])
                screenshot("Verify_code")
            else:
                link = verifydict["link"]
                common.verify_by_link(link)
                screenshot("Verify_link")
            common.sleep(3)
        success = common.wait(type='id', el="com.deepblu.android.deepblu.internal:id/popup_bottom_btn_right")
        if success:
            screenshot("Veirfy")
        else:
            screenshot("Veirfyfail")
            log("Please check the screen shoot")

    except Exception as e:
        log(e, 'w')
    log("[Verify] end")


def signup_skip():
    log("[Sign up and skip] start")
    try:
        driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/fragment_signup_verify_skip_text").click()
        common.sleep(2)
        # check skip successful or not
        checkel = common.wait(type='xpath', el=GlobalString.create_post)
        if checkel:
            screenshot("SignUpSkip")
        else:
            log("Please check the screen shoot", "w")

        log("[Sign up and skip] end")
    except Exception as e:
        log(e, 'w')


def signup_token_expire(Useremail):
    log("[Sign up token expire] start")
    try:
        # token expired
        token = common.token_expired(Useremail)
        if token:
            driver.find_element_by_xpath(GlobalString.community).click()
            common.sleep(2)
            # check token expired successfully or not(enter to email verify page)
            checkel = common.wait(type='id', el="com.deepblu.android.deepblu.internal:id/activity_toolbar_title")
            if checkel:
                screenshot("SignUpTokenExpire")
            else:
                log("Please check the screenshot", 'w')
        else:
            screenshot("tokenExpireFailed")
            log("Please check the screenshot.", 'w')
    except Exception as e:
        log(e, 'w')
    log("[Sign up token expire] end")


def signup_change_email():
    log("[Sign up change email] start")
    try:
        Useremail = signup()
        common.sleep(2)
        # 確認有成功換email 切換到驗證頁
        el2 = common.wait(type="id", el="com.deepblu.android.deepblu.internal:id/fragment_signup_verify_hint_msg")
        if el2:
            # change email
            driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/fragment_signup_verify_change").click()
            common.sleep(2)
            changeUseremail = "change" + Useremail
            # print('ChangeEmail:'+changeUseremail)
            driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/editTextEmail").send_keys(
                changeUseremail)
            driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/buttonSignUp").click()
            common.sleep(3)
            # verify code after change email
            verify(verify='code', Useremail=changeUseremail)
            success = common.wait(type='id', el="com.deepblu.android.deepblu.internal:id/popup_bottom_btn_right")
            if success:
                screenshot("SignUp_changeEmail")
            else:
                log("Please check the screen shoot")
        else:
            log("Please check the screen shoot")
    except Exception as e:
        log(e, 'w')
    log("[Sign up change email] end")


def signup_resend_email():
    log("[Sign up resend email] start")
    try:
        Useremail = signup()
        # resend
        driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/fragment_signup_verify_resend").click()
        common.sleep(0.5)
        screenshot('SignUp_resendEmail')
        common.sleep(2)

        # verify code after resend email
        verify(verify='code', Useremail=Useremail)
        success = common.wait(type='id', el="com.deepblu.android.deepblu.internal:id/popup_bottom_btn_right")
        if success:
            screenshot("SignUp_resendEamil_success")
        else:
            screenshot("SignUpfail")
            log("Please check the screen shoot")

    except Exception as e:
        log(e, 'w')
    log("[Sign up resend email] end")


def signup_with_existed_email():
    log("[Sign up with existed email] start")
    try:
        el = common.wait(type="id", el="com.deepblu.android.deepblu.internal:id/buttonSignUpWithEmail")
        if el:
            driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/buttonSignUpWithEmail").click()
            common.sleep(2)
            Useremail = desired_capabilities.account()
            driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/editTextUserName").send_keys(
                "ExistedUser")
            common.back()
            driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/editTextEmail").send_keys(Useremail)
            common.back()
            driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/editTextPassword").click()
            # check successful or not
            elcheck = common.wait(type='id', el="com.deepblu.android.deepblu.internal:id/editTextEmailError")
            if elcheck:
                screenshot('SignupExistedEmail')
            else:
                log('Please check the screen shoot')
        else:
            log("Please check the screen shoot")
    except Exception as e:
        log(e, 'w')
    log("[Sign up with existed email] end")


# 要先verify過才能執行此function
def edit_profile_after_signup():
    log("[Edit Profile after sign up] start")
    try:
        common.sleep(2)
        driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/popup_bottom_btn_right").click()
        common.sleep(2)
        checkel = common.wait(type='id', el='com.deepblu.android.deepblu.internal:id/edit_text_user_name')
        if checkel:
            screenshot('editProfileAfterSignup')
        else:
            log('Please check the screenshot')
    except Exception as e:
        log(e, 'w')
    log("[Edit Profile after sign up] end")


def guest():
    log('[Guest] start')
    try:
        skip_version_check()
        if common.wait(type='id', el='com.deepblu.android.deepblu.internal:id/buttonSkip'):
            driver.find_element_by_id('com.deepblu.android.deepblu.internal:id/buttonSkip').click()
        if common.wait(type='xpath', el=GlobalString.community):
            common.sleep(2)
            screenshot('Guest')
        else:
            log('Please check screenshot.')
    except Exception as e:
        log(e, 'w')
    log('[Guest] end')


# 要先執行guest
def guest_pass_signup():
    log('[Guest pass signup] start')
    try:
        if common.wait(type='xpath', el=GlobalString.create_post):
            driver.find_element_by_xpath(GlobalString.create_post).click()

            if common.wait(type='id', el='com.deepblu.android.deepblu.internal:id/buttonNotNow'):
                driver.find_element_by_id('com.deepblu.android.deepblu.internal:id/buttonNotNow').click()

                if common.wait(type='xpath', el=GlobalString.create_post):
                    common.sleep(2)
                    screenshot('guestPassSignup')
                else:
                    log('Please check screenshot.')
    except Exception as e:
        log(e, 'w')
    log('[Guest pass signup] end')


# not yet
def forget_password(email):
    log('[Forget password] start')
    try:
        if common.wait(type='id', el='com.deepblu.android.deepblu.internal:id/textLogin'):
            driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/textLogin").click()

            # enter to login page
            common.sleep(3)
            # 縮起鍵盤
            common.back()
            if common.wait(type='id', el='com.deepblu.android.deepblu.internal:id/textTerms2'):
                driver.find_element_by_id('com.deepblu.android.deepblu.internal:id/textTerms2').click()
                #  resend message
                if common.wait(type='id', el='com.deepblu.android.deepblu.internal:id/editTextEmail'):
                    driver.find_element_by_id('com.deepblu.android.deepblu.internal:id/editTextEmail').send_keys(email)
                    common.sleep(2)
                    # click ok
                    driver.find_element_by_id('android:id/button1').click()
                    if common.wait(type='id', el='android:id/button1'):
                        btn = driver.find_element_by_id('android:id/button1').text
                        if btn == 'Confirm':
                            driver.find_element_by_id('android:id/button1').click()
                        else:
                            log('Send resend email failed.')
                    else:
                        log('Please see the screenshot.')
                else:
                    log('Please see the screenshot.')
            else:
                log('Please see the screenshot.')
    except Exception as e:
        log(e, 'w')
    log('[Forget password] end')


def changePhoto(file, photo):
    try:
        x1 = "//android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]" \
             "/android.view.View[1]/com.sec.samsung.gallery.glview.composeView.PositionControllerBase.ThumbObject[" + file + "]"
        x2 = "//android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/" \
             "android.view.View[1]/com.sec.samsung.gallery.glview.composeView.PositionControllerBase.ThumbObject[" + photo + "]"
        driver.find_element_by_xpath(x1).click()
        common.sleep(3)
        el = common.wait(type='xpath', el=x2)
        el.click()
        common.sleep(2)
        driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/menu_crop").click()
        common.sleep(2)
    except Exception as e:
        log(e, 'w')


def hashtag():
    try:
        driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/btn_control_hashtag").click()
        common.sleep(1)
        driver.find_element_by_id("com.deepblu.android.deepblu.internal:id/new_hash_tag").send_keys("TestHashTag")
        common.enter()
    except Exception as e:
        log(e, 'w')


# test swip and find element
def test():
    log('[Test] start')
    log('[logout] start')

    try:
        driver.find_element_by_xpath(GlobalString.menu).click()
        common.sleep(3)
        if common.swip_find_el('xpath', GlobalString.logout, 'Log Out'):
            # logout xpath :note5 12 zenfone 10
            driver.find_element_by_xpath(GlobalString.logout).click()
            common.sleep(3)
            el = common.wait(type='id', el="android:id/button1")
            if el:
                driver.find_element_by_id("android:id/button1").click()
            else:
                log("Please check the screen shoot")
            common.sleep(3)
            # verify successful or not
            checkel = common.wait(type='id', el='com.deepblu.android.deepblu.internal:id/textLogin')
            if checkel:
                screenshot("Logout")
            else:
                log('Please check the screenshot')
        else:
            log('Cannot find element')
    except Exception as e:
        log(e, 'w')
    log('[logout] end')
    log('[Test] end')


# not yet
def like():
    log('[like] start')
    try:
        # os.popen("adb shell am start -W -a android.intent.action.VIEW -d 'deepblu://deepblu.link/Discover/Trending'")
        # common.sleep(3)
        common.swipeup()
        user = driver.find_elements_by_id('com.deepblu.android.deepblu.internal:id/account_level')
        for x in range(len(user)):
            path = GlobalString.post + '[' + str(
                x + 1) + ']/android.widget.RelativeLayout[3]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]'
            print(path)
            if common.wait(type='xpath', el=path):
                driver.find_element_by_xpath(path).click()
    except Exception as e:
        log(e, 'w')
    log('[like] end')


# video id :com.deepblu.android.deepblu.internal:id/post_video_gallery
# post cotent id :com.deepblu.android.deepblu.internal:id/post_post_type_content_group
# photo content id :com.deepblu.android.deepblu.internal:id/post_photo_content
# photo id :com.deepblu.android.deepblu.internal:id/post_photo_gallery
def scroll_post():
    log('[scroll post] start')
    dict = []
    # os.popen("adb shell am start -W -a android.intent.action.VIEW -d 'deepblu://deepblu.link/Discover/Following'")
    common.sleep(2)
    # user = driver.find_elements_by_id('com.deepblu.android.deepblu.internal:id/post_post_type_author')
    # post_count = len(user)
    # print(post_count)
    # # print(user)
    # for x in range(post_count - 1):
    #     print(x)
    #     usr = user[x].find_element_by_id('com.deepblu.android.deepblu.internal:id/user_name_text').text
    #     type = user[x].find_element_by_id('com.deepblu.android.deepblu.internal:id/dive_type_text').text
    #     post_time = user[x].find_element_by_id('com.deepblu.android.deepblu.internal:id/text_area_1').text
    #     print(usr, type, post_time)
    #
    #     dict.append({
    #         'user': usr,
    #         'post_type': type,
    #         'time': post_time
    #     })
    # print(dict)

    # dive log headr: com.deepblu.android.deepblu.internal:id/header
    # dive log user info:com.deepblu.android.deepblu.internal:id/user_info_text_group
    #  post user info :com.deepblu.android.deepblu.internal:id/user_info_text_group
    # dive log username:com.deepblu.android.deepblu.internal:id/user_name_text
    # dvee log dive type :com.deepblu.android.deepblu.internal:id/dive_type_text
    # dive log post time:com.deepblu.android.deepblu.internal:id/text_area_1
    while len(dict) < 8:
        common.sleep(4)
        user2 = driver.find_elements_by_id('com.deepblu.android.deepblu.internal:id/user_info_text_group')
        post_count2 = len(user2)
        print('total:' + str(post_count2))

        for y in range(post_count2):
            print(y)
            try:
                usr = user2[y].find_element_by_id('com.deepblu.android.deepblu.internal:id/user_name_text').text
                post_type = user2[y].find_element_by_id('com.deepblu.android.deepblu.internal:id/dive_type_text').text
                post_time = user2[y].find_element_by_id('com.deepblu.android.deepblu.internal:id/text_area_1').text

                print(usr, post_type, post_time)

                if len(dict) == 0:
                    dict.append({
                        'user': usr,
                        'post_type': post_type,
                        'time': post_time
                    })
                else:
                    duplicate = False
                    for item in dict:
                        if usr == item['user']:
                            if post_type == item['post_type']:
                                if post_time == item['time']:
                                    duplicate = True
                                    break
                    print(duplicate)
                    if not duplicate:
                        dict.append({
                            'user': usr,
                            'post_type': post_type,
                            'time': post_time
                        })
            except Exception as e:
                log(e)
        print(len(dict), dict)
        common.swipeup2()
        common.sleep(2)

    log('[scroll post] end')


# video content-desc: 20170810163139272 from Deepblu on Vimeo
# photo content id:com.deepblu.android.deepblu.internal:id/post_photo_content
# status content id: com.deepblu.android.deepblu.internal:id/post_status_content
# video content id:com.deepblu.android.deepblu.internal:id/post_video_content
# link content id :com.deepblu.android.deepblu.internal:id/post_url_content
# dive log content id:com.deepblu.android.deepblu.internal:id/dive_note_text

# hash_tag id  也不一樣欸 =口=
# status hashtag id :com.deepblu.android.deepblu.internal:id/post_status_tags
# phtot hashtag id :com.deepblu.android.deepblu.internal:id/post_photo_tags
# url og title id :com.deepblu.android.deepblu.internal:id/open_graph_title
# url og derscription:com.deepblu.android.deepblu.internal:id/open_graph_description
# article title id :com.deepblu.android.deepblu.internal:id/post_article_title
# article content id :com.deepblu.android.deepblu.internal:id/post_article_short_content

def scroll_live():
    log('[scroll live] start')
    dict = {}
    dict = common.live_feed()

    duplicate = False

    # while not duplicate
    userInfo = driver.find_elements_by_id('com.deepblu.android.deepblu.internal:id/user_info_text_group')
    post_count = len(userInfo)
    print('total:' + str(post_count))

    for x in range(post_count):
        try:
            usr = userInfo[x].find_element_by_id('com.deepblu.android.deepblu.internal:id/user_name_text').text
            post_type = userInfo[x].find_element_by_id(
                'com.deepblu.android.deepblu.internal:id/dive_type_text').text.lower()
            # post_time = userInfo[x].find_element_by_id(
            #     'com.deepblu.android.deepblu.internal:id/text_area_1').text

            print(usr, post_type)

            if usr == dict[0]['user']:
                if post_type == dict[0]['postType']:
                    if dict[0]['postType'] == 'scuba log':
                        if common.swip_find_el('id', 'com.deepblu.android.deepblu.internal:id/time_text_value'):
                            divetime = driver.find_element_by_id('com.deepblu.android.deepblu.internal:id/'
                                                                 'time_text_value').text
                            divetime = divetime[:divetime.find('m')]

                            max_depth = driver.find_element_by_id('com.deepblu.android.deepblu.internal:id/'
                                                                  'depth_text_value').text
                            max_depth = max_depth[:max_depth.find('m')]
                            print(divetime, max_depth)
                            if int(divetime) == dict[0]['duration'] / 60:
                                # 單位 m
                                if float(max_depth) == dict[0]['maxDepth']:
                                    if common.swip_find_el('id',
                                                           'com.deepblu.android.deepblu.internal:id/dive_note_text',
                                                           time=2):
                                        content = driver.find_elements_by_id('com.deepblu.android.deepblu.internal:id/'
                                                                             'dive_note_text').text
                                    else:
                                        content = ''
                                    if content == dict[0]['content']:
                                        duplicate = True
                                        break
                        else:
                            log('找不到duration,太神奇了', 'w')
                    elif dict[0]['postType'] == 'freedive log':
                        if common.swip_find_el('id', 'com.deepblu.android.deepblu.internal:id/time_text_value'):
                            divetime = driver.find_element_by_id('com.deepblu.android.deepblu.internal:id/'
                                                                 'time_text_value').text
                            divetime = divetime[:divetime.find('s')]
                            max_depth = driver.find_element_by_id('com.deepblu.android.deepblu.internal:id/'
                                                                  'depth_text_value').text
                            max_depth = max_depth[:max_depth.find('m')]
                            print(divetime)
                            if int(divetime) == dict[0]['duration']:
                                # 單位 m
                                if float(max_depth) == dict[0]['maxDepth']:
                                    if common.swip_find_el('id',
                                                           'com.deepblu.android.deepblu.internal:id/dive_note_text',
                                                           time=4):
                                        content = driver.find_element_by_id('com.deepblu.android.deepblu.internal:id/'
                                                                             'dive_note_text').text
                                    else:
                                        content = ''
                                    if content == dict[0]['content']:
                                        duplicate = True
                                        break
                        else:
                            log('找不到duration,太神奇了', 'w')
                    elif dict[0]['postType'] == 'photo':
                        if common.swip_find_el('id', 'com.deepblu.android.deepblu.internal:id/post_photo_content'):
                            content = driver.find_element_by_id('com.deepblu.android.deepblu.internal:id/'
                                                                'post_photo_content').text
                        else:
                            content = ''
                        # if common.swip_find_el('id', 'com.deepblu.android.deepblu.internal:id/post_photo_tags', time=5):
                        #     tag = driver.find_element_by_id(
                        #         'com.deepblu.android.deepblu.internal:id/post_photo_tags').text
                        if content == dict[0]['content']:
                            duplicate = True
                            break
                    elif dict[0]['postType'] == 'video':
                        if common.swip_find_el('id', 'com.deepblu.android.deepblu.internal:id/post_video_content'):
                            content = driver.find_element_by_id('com.deepblu.android.deepblu.internal:id/'
                                                                'post_video_content').text
                        else:
                            content = ''

                        if content == dict[0]['content']:
                            duplicate = True
                            break
                    elif dict[0]['postType'] == 'url':
                        if common.swip_find_el('id', 'com.deepblu.android.deepblu.internal:id/open_graph_title'):
                            og_title = driver.find_element_by_id('com.deepblu.android.deepblu.internal:id/'
                                                                 'open_graph_title').text
                            common.swipeup2()
                            # check if og_description exist or not
                            if common.wait('id', 'com.deepblu.android.deepblu.internal:id/open_graph_description'):
                                og_desc = driver.find_element_by_id('com.deepblu.android.deepblu.internal:id/'
                                                                    'open_graph_description').text
                            if common.wait('id', 'com.deepblu.android.deepblu.internal:id/post_url_content'):
                                content = driver.find_element_by_id('com.deepblu.android.deepblu.internal:id/'
                                                                    'post_url_content').text
                            else:
                                content = ''
                            if og_title == dict[0]['og_title']:
                                if og_desc == dict[0]['og_desc']:
                                    if content == dict[0]['content']:
                                        duplicate = True
                                        break
                        else:
                            log('好吧，就是沒有og title', 'w')

                    elif dict[0]['postType'] == 'article':
                        if common.swip_find_el('id','com.deepblu.android.deepblu.internal:id/post_article_title'):
                            title = driver.find_element_by_id('com.deepblu.android.deepblu.internal:id'
                                                               '/post_article_title').text
                            if title == dict[0]['title']:
                                if common.swip_find_el('id','com.deepblu.android.deepblu.internal:id/'
                                                            'post_article_short_content'):
                                    content = driver.find_element_by_id('com.deepblu.android.deepblu.internal:id/'
                                                                        'post_article_short_content').text
                                    if content == dict[0]['content']:
                                        if common.swip_find_el('id',
                                                               'com.deepblu.android.deepblu.internal:id/post_status_tags'):
                                            tag = driver.find_element_by_id('com.deepblu.android.deepblu.internal:id/'
                                                                            'post_status_tags').text
                                            tag = tag.replace("#", "")
                                            tag = tag.replace(" ", "")
                                        else:
                                            tag = ''
                                        if tag == dict[0]['tag']:
                                            duplicate = True
                                            break
                                else:
                                    log('article content 沒有,到底是哪位大大發的文','w')
                        else:
                            log('article tilte都找不到，怪我囉！','w')
                        pass

                    elif dict[0]['postType'] == 'status':
                        content_total = driver.find_elements_by_id('com.deepblu.android.deepblu.internal:id/'
                                                                   'post_status_content')
                        for n in range(len(content_total)):
                            content = content_total[n].text

                            if content == dict[0]['content']:
                                if common.swip_find_el('id','com.deepblu.android.deepblu.internal:id/post_status_tags'):
                                    tag = driver.find_element_by_id('com.deepblu.android.deepblu.internal:id/'
                                                                    'post_status_tags').text
                                    tag = tag.replace("#", "")
                                    tag = tag.replace(" ", "")
                                else:
                                    tag = ''
                                if tag == dict[0]['tag']:
                                    duplicate = True
                                    break
                    else:
                        print('nonoo ')
                else:
                    print('postTypenoooo')
            else:
                print('Name noooo')
            print(duplicate)

            if duplicate:
                break

        except Exception as e:
            log(e, 'w')

    if duplicate:
        screenshot('scroll')
        print('success')
    else:
        log('Cannot find 10th post.Please see log.')
    log('[scroll live] end')


def test():
    # tag = driver.find_element_by_id('com.deepblu.android.deepblu.internal:id/post_status_tags').text
    tag = '#1 #2 #3'
    tag = tag.replace("#","")
    tag = tag.replace(" ",'')
    print(tag)
