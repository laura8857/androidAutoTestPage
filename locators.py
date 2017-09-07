from appium.webdriver.common.mobileby import MobileBy as By
# from selenium.webdriver.common.by import By

# 一進來的主畫面
class MainPageLocators(object):
    btn_facebook        = (By.ID, 'com.deepblu.android.deepblu.internal:id/rlFacebookContainer')
    btc_email           = (By.ID, 'com.deepblu.android.deepblu.internal:id/buttonSignUpWithEmail')
    btn_login           = (By.ID, 'com.deepblu.android.deepblu.internal:id/textLogin')
    btn_preview         = (By.ID, 'com.deepblu.android.deepblu.internal:id/buttonSkip')

# loading畫面
class LoadingLocators(object):
    btn_do_it_later     = (By.ID, 'android:id/button2')
    btn_update          = (By.ID, 'android:id/button1')
    chk_dont_show       = (By.ID, 'com.deepblu.android.deepblu.internal:id/dialog_checkbox')

# 登入畫面
class LoginPageLocators(object):
    btn_facebook        = (By.ID, 'com.deepblu.android.deepblu.internal:id/buttonLogInFacebook')
    txt_acc             = (By.ID, 'com.deepblu.android.deepblu.internal:id/editTextEmail')
    txt_pwd             = (By.ID, 'com.deepblu.android.deepblu.internal:id/editTextPassword')
    btn_login           = (By.ID, 'com.deepblu.android.deepblu.internal:id/buttonSignUp')
    btn_fogot_pwd       = (By.ID, 'com.deepblu.android.deepblu.internal:id/textTerms2')
    btn_skip            = (By.ID, 'com.deepblu.android.deepblu.internal:id/buttonSkip')

# discover~menu的tab
class MainTabLocators(object):
    btn_discover        = (By.XPATH, '//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/'
                                     'android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/'
                                     'android.widget.RelativeLayout[1]/android.widget.HorizontalScrollView[1]'
                                     'android.widget.LinearLayout[1]/android.support.v7.app.ActionBar.Tab[1]')
    btn_community       = (By.XPATH, '//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/'
                                     'android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/'
                                     'android.widget.RelativeLayout[1]/android.widget.HorizontalScrollView[1]/'
                                     'android.widget.LinearLayout[1]/android.support.v7.app.ActionBar.Tab[2]')
    btn_create_post     = (By.XPATH, '//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/'
                                     'android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/'
                                     'android.widget.RelativeLayout[1]/android.widget.HorizontalScrollView[1]/'
                                     'android.widget.LinearLayout[1]/android.support.v7.app.ActionBar.Tab[3]')
    btn_connect         = (By.XPATH, '//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/'
                                     'android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/'
                                     'ndroid.widget.RelativeLayout[1]/android.widget.HorizontalScrollView[1]'
                                     '/android.widget.LinearLayout[1]/android.support.v7.app.ActionBar.Tab[4]')
    btn_menu            = (By.XPATH, '//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/'
                                     'android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/'
                                     'android.widget.RelativeLayout[1]/android.widget.HorizontalScrollView[1]/'
                                     'android.widget.LinearLayout[1]/android.support.v7.app.ActionBar.Tab[5]')

# menu 畫面
class MenuPageLocators(object):
    btn_profile         = (By.XPATH, '//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/'
                                     'android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/'
                                     'android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/'
                                     'android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/'
                                     'android.widget.ListView[1]/android.widget.LinearLayout[1]')
    btn_notification    = (By.XPATH, '//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/'
                                     'android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/'
                                     'android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/'
                                     'android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/'
                                     'android.widget.ListView[1]/android.widget.LinearLayout[2]')
    btn_log_drafts      = (By.XPATH, '//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/'
                                     'android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/'
                                     'android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/'
                                     'android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/'
                                     'android.widget.ListView[1]/android.widget.LinearLayout[3]')
    btn_dive_computer   = (By.XPATH, '//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/'
                                     'android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/'
                                     'android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/'
                                     'android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/'
                                     'android.widget.ListView[1]/android.widget.LinearLayout[5]')
    btn_app_setting     = (By.XPATH, '//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/'
                                     'android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/'
                                     'android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/'
                                     'android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/'
                                     'android.widget.ListView[1]/android.widget.LinearLayout[7]')
    btn_events          = (By.XPATH, '//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/'
                                     'android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/'
                                     'android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/'
                                     'android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/'
                                     'android.widget.ListView[1]/android.widget.LinearLayout[8]')
    btn_academy         = (By.XPATH, '//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/'
                                     'android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/'
                                     'android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/'
                                     'android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/'
                                     'android.widget.ListView[1]/android.widget.LinearLayout[9]')
    btn_help            = (By.XPATH, '//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/'
                                     'android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/'
                                     'android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/'
                                     'android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/'
                                     'android.widget.ListView[1]/android.widget.LinearLayout[10]')
    btn_app_feedback    = (By.XPATH, '//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/'
                                     'android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/'
                                     'android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/'
                                     'android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/'
                                     'android.widget.ListView[1]/android.widget.LinearLayout[11]')
    btn_about           = (By.XPATH, '//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/'
                                     'android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/'
                                     'android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/'
                                     'android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/'
                                     'android.widget.ListView[1]/android.widget.LinearLayout[12]')
    btn_logout          = (By.XPATH, '//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/'
                                     'android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/'
                                     'android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/'
                                     'android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/'
                                     'android.widget.ListView[1]/android.widget.LinearLayout[12]')
    btn_logout_ok       = (By.ID, 'android:id/button1')
    btn_logout_cancel   = (By.ID, 'android:id/button2')

# 註冊畫面
class SignUpPageLocators(object):
    btn_back            = (By.ID, 'com.deepblu.android.deepblu.internal:id/signUpFragmentButtonBack')
    txt_username        = (By.ID, 'com.deepblu.android.deepblu.internal:id/editTextUserName')
    txt_acc             = (By.ID, 'com.deepblu.android.deepblu.internal:id/editTextEmail')
    txt_pwd             = (By.ID, 'com.deepblu.android.deepblu.internal:id/editTextPassword')
    btn_submit          = (By.ID, 'com.deepblu.android.deepblu.internal:id/buttonSignUp')
    btn_terms           = (By.ID, 'com.deepblu.android.deepblu.internal:id/textTerms2')

    txt_duplicate_acc    = (By.ID, 'com.deepblu.android.deepblu.internal:id/editTextEmailError')

# 驗證畫面
class VerifyEmailPageLocators(object):
    btn_back            = (By.XPATH, '//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/'
                                     'android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/'
                                     'android.widget.RelativeLayout[1]/android.view.ViewGroup[1]/'
                                     'android.widget.ImageButton[1]')
    txt_verify          = (By.ID, 'com.deepblu.android.deepblu.internal:id/fragment_signup_verify_hint_msg')
    txt_code1           = (By.ID, 'com.deepblu.android.deepblu.internal:id/fragment_signup_verify_input_1')
    txt_code2           = (By.ID, 'com.deepblu.android.deepblu.internal:id/fragment_signup_verify_input_2')
    txt_code3           = (By.ID, 'com.deepblu.android.deepblu.internal:id/fragment_signup_verify_input_3')
    txt_code4           = (By.ID, 'com.deepblu.android.deepblu.internal:id/fragment_signup_verify_input_4')
    btn_skip            = (By.ID, 'com.deepblu.android.deepblu.internal:id/fragment_signup_verify_skip_text')
    btn_resend          = (By.ID, 'com.deepblu.android.deepblu.internal:id/fragment_signup_verify_resend')
    btn_change          = (By.ID, 'com.deepblu.android.deepblu.internal:id/fragment_signup_verify_change')

    txt_title           = (By.ID, 'com.deepblu.android.deepblu.internal:id/popup_bottom_title')
    btn_not_now         = (By.ID, 'com.deepblu.android.deepblu.internal:id/popup_bottom_btn_left')
    btn_edit            = (By.ID, 'com.deepblu.android.deepblu.internal:id/popup_bottom_btn_right')

class ChangeEmailPageLocators(object):
    txt_acc             = (By.ID, 'com.deepblu.android.deepblu.internal:id/editTextEmail')
    btn_submit          = (By.ID, 'com.deepblu.android.deepblu.internal:id/buttonSignUp')

#編輯profile頁面 not yetttt
class EditProfilePageLocators(object):
    img_backgroud       = (By.ID, 'com.deepblu.android.deepblu.internal:id/user_profile_edit_background')
    img_avatar          = (By.ID, 'com.deepblu.android.deepblu.internal:id/account_level')
    txt_usr             = (By.ID, 'com.deepblu.android.deepblu.internal:id/edit_text_user_name')
    txt_first_name      = (By.ID, 'com.deepblu.android.deepblu.internal:id/edit_text_first_name')
    txt_last_name       = (By.ID, 'com.deepblu.android.deepblu.internal:id/edittext_last_name')
    txt_birthday        = (By.ID, 'com.deepblu.android.deepblu.internal:id/button_birthday')
