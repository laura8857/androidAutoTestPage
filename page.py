# -*- coding: utf-8 -*-

from deepblu_lib import log
import desired_capabilities
from locators import *
from appium import webdriver
import time
from base import *
import base
# import common


class LoginOut:
    def __init__(self):
        pass

    def check_login(self, status):
        log('[check login] start')
        try:
            log('[check login] status is %s' % status)
            if status is True:
                if element(MainTabLocators.btn_create_post).wait():
                    pass
                else:
                    self.login()
            else:
                if element(MainTabLocators.btn_create_post).wait():
                    self.logout
            log('[check login] end')
            return True
        except Exception as e:
            log(e, 'w')
            return False

    def version_skip(self):
        log('[skip version check] start')
        try:
            element(LoadingLocators.btn_do_it_later).click()
        except Exception as e:
            log(e, 'w')
        log('[skip version check] end')

    def login(self, email=None, password=None):
        log('[login] start')
        try:
            self.version_skip()
            if email is None:
                email = desired_capabilities.account()
            if password is None:
                password = desired_capabilities.password()

            element(MainPageLocators.btn_login).click()
            element(LoginPageLocators.txt_acc).input(email)
            element(LoginPageLocators.txt_pwd).input(password)
            back()
            element(LoginPageLocators.btn_login).click()
            if not element(MainTabLocators.btn_create_post).wait():
                return False
            log('[login] end')
            return True
        except Exception as e:
            log(e, 'w')
            return False

    def login_skip(self):
        log('[login_skip] start')
        try:

            element(MainPageLocators.btn_login).click()
            sleep(2)
            back()
            element(LoginPageLocators.btn_skip).click()
            if not element(MainTabLocators.btn_create_post).wait():
                return False

            screenshot('logSkip')
            log('[login_skip] end')
            return True
        except Exception as e:
            log(e, 'w')
            return False

    def logout(self):
        log('[logout] start')

        try:
            element(MainTabLocators.btn_menu).click()
            move(MenuPageLocators.btn_logout).swip_find_el(text='Log Out')
            element(MenuPageLocators.btn_logout_ok).click()
            if not element(MainPageLocators.btn_login).wait():
                return False

            screenshot('Logout')
            log('[logout] end')
            return True

        except Exception as e:
            log(e, 'w')
            return False


class Signup:
    def __init__(self):
        pass

    def signup(self, username=None, email=None, password=None):
        log("[Sign up] start")
        try:
            if username is None:
                username = usr
            if email is None:
                email = acc
            if password is None:
                password = pwd

            element(MainPageLocators.btc_email).click()
            element(SignUpPageLocators.txt_username).input(username)
            base.back()
            element(SignUpPageLocators.txt_acc).input(email)
            base.back()
            element(SignUpPageLocators.txt_pwd).input(password)
            base.back()
            element(SignUpPageLocators.btn_submit).click()

            if not element(VerifyEmailPageLocators.txt_verify).wait():
                return False
            screenshot('SignUp')
            log("[Sign up] end")
            return True

        except Exception as e:
            log(e, 'w')
            return False

    # verify:code/url
    def verify(self, verify='code', Useremail=None):
        log("[Verify] start")
        try:
            if Useremail is None:
                Useremail = acc
            verifydict = {}
            verifydict = base.getusercode(Useremail)
            if len(verifydict) == 0:
                log("Cannot get verify code.Please check the screen")
            else:
                if verify == "code":
                    code = verifydict["code"]
                    element(VerifyEmailPageLocators.txt_code1).input(code[0:1])
                    element(VerifyEmailPageLocators.txt_code2).input(code[1:2])
                    element(VerifyEmailPageLocators.txt_code3).input(code[2:3])
                    element(VerifyEmailPageLocators.txt_code4).input(code[3:4])
                    screenshot("Verify_code")
                else:
                    link = verifydict["link"]
                    base.verify_by_link(link)
                    screenshot("Verify_link")
            if not element(VerifyEmailPageLocators.btn_edit).wait():
                return False

            screenshot("Veirfy")
            log("[Verify] end")
            return True

        except Exception as e:
            log(e, 'w')
            return False

    # 要先verify過才能執行此function
    def edit_profile_after_signup(self):
        log("[Edit Profile after sign up] start")
        try:
            element(VerifyEmailPageLocators.btn_edit).click()
            if not element(EditProfilePageLocators.txt_usr).wait():
                return False

            screenshot('editProfileAfterSignup')
            log("[Edit Profile after sign up] end")
            return True
        except Exception as e:
            log(e, 'w')
            return False

    def signup_with_existed_email(self):
        log("[Sign up with existed email] start")
        try:
            element(MainPageLocators.btc_email).click()
            email = desired_capabilities.account()
            element(SignUpPageLocators.txt_username).input('Existed User')
            back()
            element(SignUpPageLocators.txt_acc).input(email)
            back()
            element(SignUpPageLocators.txt_pwd).click()
            if not element(SignUpPageLocators.txt_duplicate_acc).wait():
                return False

            screenshot('SignupExistedEmail')
            log("[Sign up with existed email] end")
            return True

        except Exception as e:
            log(e, 'w')
            return False

    def change_email(self, email=None):
        log("[Sign up change email] start")
        try:
            if email is None:
                email = acc

            # 確認有成功換email 切換到驗證頁
            if not element(VerifyEmailPageLocators.txt_verify).wait():
                return False

            element(VerifyEmailPageLocators.btn_change).click()
            changeUseremail = time.strftime("%m%d%H%M") + email
            element(ChangeEmailPageLocators.txt_acc).input(changeUseremail)
            element(ChangeEmailPageLocators.btn_submit).click()

            # 確認有成功換email 切換到驗證頁
            if not element(VerifyEmailPageLocators.txt_verify).wait():
                return False

            if not self.verify(verify='code', Useremail=changeUseremail):
                return False

            screenshot("SignUp_changeEmail")
            log("[Sign up change email] end")
            return True

        except Exception as e:
            log(e, 'w')
            return False

    def resend_email(self, email=None):
        log("[Sign up resend email] start")
        try:
            if email is None:
                email = acc

            # 確認有成功換email 切換到驗證頁
            if not element(VerifyEmailPageLocators.txt_verify).wait():
                return False

            element(VerifyEmailPageLocators.btn_resend).click()
            sleep(0.5)
            screenshot('SignUp_resendEmail')

            if not self.verify(verify='code', Useremail=email):
                return False

            screenshot("SignUp_resendEamil_success")
            log("[Sign up resend email] end")
            return True
        except Exception as e:
            log(e, 'w')
            return False

    def skip(self):
        log("[Sign up and skip] start")
        try:
            # 確認有成功換email 切換到驗證頁
            if not element(VerifyEmailPageLocators.txt_verify).wait():
                return False

            element(VerifyEmailPageLocators.btn_skip).click()
            if not element(MainTabLocators.btn_create_post).wait():
                return False

            screenshot("SignUpSkip")
            log("[Sign up and skip] end")
            return True
        except Exception as e:
            log(e, 'w')
            return False

    def skip_v2(self):
        log("[Sign up and skip2] start")
        try:
            # 確認有成功換email 切換到驗證頁
            if not element(VerifyEmailPageLocators.txt_verify).wait():
                return False
            kill_app()
            sleep(2)
            open_app()

            if not element(VerifyEmailPageLocators.txt_verify).wait():
                return False

            screenshot("SignUpSkip2")
            log("[Sign up and skip2] end")
            return True
        except Exception as e:
            log(e, 'w')
            return False

    def signup_token_expire(self, Useremail):
        log("[Sign up token expire] start")
        try:
            if not token_expired(Useremail):
                return False
            element(MainTabLocators.btn_create_post).click()
            # check token expired successfully or not(enter to email verify page)
            if not element(VerifyEmailPageLocators.txt_verify).wait():
                return False
            screenshot("SignUpTokenExpire")
            log("[Sign up token expire] end")
        except Exception as e:
            log(e, 'w')
            return False

    def login_after_skip(self, email=None, password=None):
        log("[Login after skip] start")
        try:
            LoginOut().version_skip()
            if email is None:
                email = desired_capabilities.account()
            if password is None:
                password = desired_capabilities.password()

            element(MainPageLocators.btn_login).click()
            element(LoginPageLocators.txt_acc).input(email)
            element(LoginPageLocators.txt_pwd).input(password)
            back()
            element(LoginPageLocators.btn_login).click()

            if not element(VerifyEmailPageLocators.txt_verify).wait():
                return False

            log("[Login after skip] end")
            screenshot('LoginAfterSkip')
            return True
        except Exception as e:
            log(e, 'w')
            return False

class MainPost:
    def __init__(self):
        pass

    def post_text(self):
        log("[Post Text] start")
        try:
            if not element(MainTabLocators.btn_create_post).click():
                return False
            if not element(PostPageLocators.btn_txt).click():
                return False
            content = '[AutoTest]\n' + time.strftime("%Y%m%d%H%M%S")
            if not element(PostPageLocators.txt_content).input(content):
                return False
            if not element(PostPageLocators.btn_ctrl_hashtag).click():
                return False
            if not element(PostPageLocators.txt_hashtag).input('test'):
                return False
            enter()
            if not element(PostPageLocators.btn_ctrl_post).click():
                return False
            if not element(PostPageLocators.btn_ok).click():
                return False
            sleep(5)
            if not element(MainTabLocators.btn_create_post).wait():
                return False

            screenshot("PostText")
            log("[Post Text] end")
            return True
        except Exception as e:
            log(e, 'w')
            return False

    def post_link(self):
        log("[Post Link] start")
        try:
            if not element(MainTabLocators.btn_create_post).click():
                return False
            if not element(PostPageLocators.btn_link).click():
                return False
            if not element(PostPageLocators.input_link).input('https://test.deepblu.com/discover/live'):
                return False
            if not element(PostPageLocators.btn_ok).click():
                return False
            if not element(PostPageLocators.img_og).wait():
                return False
            content = '[AutoTest]\n' + time.strftime("%Y%m%d%H%M%S")
            if not element(PostPageLocators.txt_content).input(content):
                return False
            if not element(PostPageLocators.btn_ctrl_hashtag).click():
                return False
            if not element(PostPageLocators.txt_hashtag).input('test'):
                return False
            enter()
            if not element(PostPageLocators.btn_ctrl_post).click():
                return False
            if not element(PostPageLocators.btn_ok).click():
                return False
            sleep(5)
            if not element(MainTabLocators.btn_create_post).wait():
                return False
            screenshot("PostLink")
            log("[Post Link] end")
            return True

        except Exception as e:
            log(e, 'w')
            return False