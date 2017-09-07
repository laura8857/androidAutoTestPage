# -*- coding: utf-8 -*-
import unittest
from deepblu_lib import log
from base import *
from page import *
from appium_init import appium_controller
import base


class SignupUnitTest(unittest.TestCase):
    result = False

    # 開始必做
    def setUp(self):
        log('[Test Case][%s] start' % (self._testMethodName), lvl='i')
        SignupUnitTest.result = False
        driver_init()

    # 結束必做
    def tearDown(self):
        screenshot('[Test Case][' + self._testMethodName + ']')
        if SignupUnitTest.result:
            log('[Test Case][%s] Success' % (self._testMethodName), lvl='i')
        else:
            log('[Test Case][%s] Fail' % (self._testMethodName), lvl='w')
        log('[Test Case][%s] end' % (self._testMethodName), lvl='i')

    # login
    def test_95(self):
        self.assertTrue(LoginOut().check_login(False))
        self.assertTrue(LoginOut().login())
        SignupUnitTest.result = True
        self.assertTrue(SignupUnitTest.result)


    # verify_code
    def test_93_1(self):
        rm_email(acc)
        log('%s %s %s' % (usr, acc, pwd), 'w')
        self.assertTrue(Signup().signup(usr, acc, pwd))
        self.assertTrue(Signup().verify(verify='code', Useremail=acc))
        SignupUnitTest.result = True

    # verify link
    def test_93_2(self):
        rm_email(acc)
        self.assertTrue(Signup().verify(verify='link', Useremail=acc))
        SignupUnitTest.result = True

    # edit_profile_after_signup
    def test_2020(self):
        rm_email(acc)
        self.assertTrue(Signup().verify(verify='link', Useremail=acc))
        self.assertTrue(Signup().edit_profile_after_signup())
        SignupUnitTest.result = True

    # signup_with_existed_email
    def test_253(self):
        self.assertTrue(Signup().signup_with_existed_email())
        SignupUnitTest.result = True

    # signup_change_email
    def test_1949(self):
        rm_email(acc)
        self.assertTrue(Signup().signup(usr, acc, pwd))
        self.assertTrue(Signup().change_email(email=acc))
        SignupUnitTest.result = True

    # signup_resend_email
    def test_1948(self):
        rm_email(acc)
        self.assertTrue(Signup().signup(usr, acc, pwd))
        self.assertTrue(Signup().resend_email(email=acc))
        SignupUnitTest.result = True

    # signup_expire_token
    def test_2085(self):
        rm_email(acc)
        self.assertTrue(Signup().signup(usr, acc, pwd))
        self.assertTrue(Signup().skip())
        self.assertTrue(Signup().signup_token_expire(Useremail=acc))
        SignupUnitTest.result = True

    # singup_skip
    def test_1951(self):
        rm_email(acc)
        self.assertTrue(Signup().signup(usr, acc, pwd))
        self.assertTrue(Signup().skip())
        self.assertTrue(LoginOut().logout())
        self.assertTrue(Signup().login_after_skip(email=acc,password=pwd))
        SignupUnitTest.result = True

    def test_1951_2(self):
        rm_email(acc)
        self.assertTrue(Signup().signup(usr, acc, pwd))
        self.assertTrue(Signup().skip_v2())
        SignupUnitTest.result = True

    # Account - English characters are sent lowercase
    def test_1415(self):
        rm_email('test@deepblu.com')
        self.assertTrue(Signup().signup(email="TEST@deepblu.com"))
        self.assertTrue(Signup().verify(verify='code',Useremail='test@deepblu.com'))
        back()
        self.assertTrue(LoginOut().logout())
        self.assertTrue(LoginOut().login(email='test@deepblu.com',password=pwd))
        SignupUnitTest.result = True

if __name__ == '__main__':
    # m=appium_controller()
    # m.start()
    unittest.main()
    # m.end()
