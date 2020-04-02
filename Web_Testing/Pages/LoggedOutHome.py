
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Web_Testing.helperClasses import WebHelper, by, Gender
import time

class LoggedOutHome(WebHelper):

    def __init__(self, driver):
        # tb refers to Toolbar, tb_.. refers to Toolbar elements
        self.set_driver(driver)
        self.tb_login_btn = self.find_element_by_xpath("/html/body/div[1]/div/div/div/nav/div/div/ul/li[6]/a")
        self.tb_signup_btn = self.find_element_by_link_text("Sign up")
        self.tb_download_btn = self.find_element_by_link_text("Download")
        self.tb_help_btn = self.find_element_by_link_text("Help")
        self.tb_premium_btn = self.find_element_by_link_text("Premium")
        # self.tb_logo = self.find_element_by_xpath("/html/body/div[2]/div/header/div/div[1]/a/span/svg/g/path")
        self.getspotify_btn = self.find_element_by_class_name("getSpotifyBtn")
        self.fb_btn = self.find_element_by_class_name("btn btn-social-icon btn-facebook")
        self.twitter_btn = self.find_element_by_class_name("btn btn-social-icon btn-twitter")
        self.instagram_btn = self.find_element_by_class_name("btn btn-social-icon btn-instagram")
        # self.subheading = self.helper.find_element_by_xpath(self.driver, "//h4[text()='Millions of songs. No credit card needed.']")
        # self.heading = self.helper.find_element_by_xpath(self.driver, "//h1[text()='Music for everyone.']")
        # self.for_artists_btn = self.helper.find_element_by_xpath(self.driver, "//a[text()='For Artists']")

    def getButtons(self):

        btns_arr = [self.tb_download_btn, self.tb_help_btn,
                    self.tb_login_btn,
                    self.tb_signup_btn, self.tb_premium_btn,
                    self.getspotify_btn]
        return btns_arr

    def click_login(self):
        try:
            self.tb_login_btn.click()
        except:
            pass

