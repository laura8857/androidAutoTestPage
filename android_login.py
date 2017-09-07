# -*- coding: utf-8 -*-

import unittest
import action
from deepblu_lib import log
import GlobalString


class android_login_test(unittest.TestCase):
    result = False

    def setUp(self):
        log('[Test Case] %s start ' % self._testMethodName)
        android_login_test.result = False
        action.driver_init()

    def tearDown(self):
        if android_login_test.result:
            log('[Test Case] %s passed ' % self._testMethodName)
        else:
            log('[Test Case] %s failed ' % self._testMethodName, 'w')
        action.driver_close()

    # login
    def test_95(self):
        action.login()
        self.assertTrue(action.wait(type='xpath', el=GlobalString.create_post))
        android_login_test.result = True

    # skip
    def test_1412(self):
        action.login_skip()
        self.assertTrue(action.wait(type='xpath', el=GlobalString.create_post))
        android_login_test.result = True

if __name__ == '__main__':
    unittest.main()
