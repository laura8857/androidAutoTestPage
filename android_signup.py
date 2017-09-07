# -*- coding: utf-8 -*-

import unittest
import action
from deepblu_lib import log
from common import rm_email


class android_signup_test(unittest.TestCase):
    result = False

    def setUp(self):
        log('[Test Case] %s start ' % self._testMethodName)
        android_signup_test.result = False
        action.driver_init()

    def tearDown(self):
        if android_signup_test.result:
            log('[Test Case] %s passed ' % self._testMethodName)
        else:
            log('[Test Case] %s failed ' % self._testMethodName, 'w')
        action.driver_close()

    # # logout
    # def test_97(self):
    #     action.login()
    #     action.logout()
    #     self.assertTrue(action.wait(type='id', el='com.deepblu.android.deepblu.internal:id/textLogin'))
    #     android_signup_test.result = True

    #verify_code
    def test_93_1(self):
        email = action.signup()
        print("email1:" + email)
        action.verify(verify='code', Useremail=email)
        self.assertTrue(action.wait(type='id', el="com.deepblu.android.deepblu.internal:id/popup_bottom_btn_right"))
        android_signup_test.result = True

    # verify link
    def test_93_2(self):
        email = action.signup()
        action.verify(verify='link', Useremail=email)
        self.assertTrue(action.wait(type='id', el="com.deepblu.android.deepblu.internal:id/popup_bottom_btn_right"))
        android_signup_test.result = True

    # edit_profile_after_signup
    def test_2020(self):
        email = action.signup()
        action.verify(verify='code', Useremail=email)
        action.edit_profile_after_signup()
        self.assertTrue(action.wait(type='id', el='com.deepblu.android.deepblu.internal:id/edit_text_user_name'))
        android_signup_test.result = True

    # signup_with_existed_email
    def test_253(self):
        action.signup_with_existed_email()
        self.assertTrue(action.wait(type='id', el="com.deepblu.android.deepblu.internal:id/editTextEmailError"))
        android_signup_test.result = True

    # not yet
    # signup_change_email

    def test_1949(self):
        action.signup_change_email()
        self.assertTrue(action.wait(type='id', el="com.deepblu.android.deepblu.internal:id/popup_bottom_btn_right"))
        android_signup_test.result = True

    # signup_resend_email
    def test_1948(self):
        action.signup_resend_email()
        self.assertTrue(action.wait(type='id', el="com.deepblu.android.deepblu.internal:id/popup_bottom_btn_right"))
        android_signup_test.result = True

    # signup_expire_token
    def test_2085(self):
        email = action.signup()
        action.signup_skip()
        action.signup_token_expire(email)
        self.assertTrue(action.wait(type='id', el="com.deepblu.android.deepblu.internal:id/activity_toolbar_title"))
        android_signup_test.result = True

    # singup_skip
    def test_1951(self):
        email = action.signup()
        action.signup_skip()
        action.logout()
        action.login(email, 'a12345678')
        self.assertTrue(action.wait(type='id', el="com.deepblu.android.deepblu.internal:id/activity_toolbar_title"))
        android_signup_test.result = True

    def test_1951_2(self):
        email = action.signup()
        action.kill_app()
        action.sleep(2)
        action.open_app()
        self.assertTrue(action.wait(type='id', el="com.deepblu.android.deepblu.internal:id/activity_toolbar_title"))
        android_signup_test.result = True

    # Account - English characters are sent lowercase
    def test_1415(self):
        rm_email('test@deepblu.com')
        action.signup(email="TEST@deepblu.com")
        action.verify(verify='code', Useremail='test@deepblu.com')
        action.back()
        action.logout()
        action.login('test@deepblu.com', 'a12345678')
        self.assertTrue(action.wait(type='id', el="com.deepblu.android.deepblu.internal:id/headerContainer"))
        android_signup_test.result = True


if __name__ == '__main__':
    unittest.main()
