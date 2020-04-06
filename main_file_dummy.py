from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from Web_Testing.helperClasses import WebHelper
from Web_Testing.helperClasses import ConstantsClass
from Web_Testing.Pages.LoginPage import LoginPage
from Web_Testing.Pages.SignupPage import SignupPage
from Web_Testing.helperClasses import DOB
import time

# print(help(LoginPage))
dob1 = DOB(20, 5, 2004)
dob2 = DOB(20, 5, 2003)
is_eq = dob1.is_equal(dob2)
print(is_eq)