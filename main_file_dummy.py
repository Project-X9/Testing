from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from Web_Testing.helperClasses import WebHelper
from Web_Testing.helperClasses import ConstantsClass
from Web_Testing.Pages.LoginPage import LoginPage
from Web_Testing.Pages.SignupPage import SignupPage
import time

helper = WebHelper()
helper.firefox_driver_init()
helper.driver.get(helper.get_signup_url())
time.sleep(2)
# profiles = ConstantsClass().test_accounts_to_profiles.values()
sp = SignupPage(helper.driver)
sp.click_signup()
time.sleep(2)
sp.click_signup()
time.sleep(4)
text_dangers = helper.find_elements_by_class_name("text-danger")
# for d in text_dangers:
#     print(d.text)
# print(text_dangers)
helper.driver.close()
# lp = LoginPage(helper.driver)
# lp.set_credentials("test1@test.com", "test123")
# lp.click_login()
# helper.driver.implicitly_wait(2)
# try:
#     account_overview = helper.driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/div[3]/div/div[1]/div[2]")
#     print("Did find account overview")
#     print(len(account_overview))
# except:
#     print("Cannot find account overview")
