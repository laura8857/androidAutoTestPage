# -*- coding: utf-8 -*-
# @Time    : 2017/2/7 下午2:13
# @Author  : Yuhsuan
# @File    : desired_capabilities.py
# @Software: PyCharm Community Edition

import os

directory = '%s/' % os.getcwd()

acc = 'tester@deepblu.com'
pwd = 'tester123'
username = 'tester'

def get_desired_capabilities(test_type, app_path):

    # desired_caps['browserName'] = 'safari'
    # desired_caps['app'] = directory+'DeepbluApp_2.0.0_adhoc.ipa'
    # desired_caps['bundleId'] = 'com.deepblu.deepblu'
    # none5:091609e258940f03
    # zenfone:G3AZCY03J892

    desired_caps = {
        'deviceName': '091609e258940f03',
        'platformName': 'Android',
        'platformVersion': '6.0',
        'appPackage': 'com.deepblu.android.deepblu.internal',
        'app': directory+'app-internal2_2_9_3_170210_173325.apk'
    }

    if test_type == 'app':
        if app_path == 'Settings':
            desired_caps['app'] = app_path
        else:
            # Need to install app
            desired_caps['app'] = directory + app_path

    elif test_type == 'bundleId':
        # Know bundle id
        desired_caps['bundleId'] = app_path

    elif test_type == 'browser':
        # Test browser
        desired_caps['browserName'] = 'safari'
    else:
        # Default is using com.deepblu.deepblu
        desired_caps['bundleId'] = 'com.deepblu.deepblu'

    return desired_caps

def account():
    return "laura2@deepblu.com"

def password():
    return "12345678"

# acc = 'test01@test.com'