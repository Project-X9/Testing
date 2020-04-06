
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Web_Testing.helperClasses import WebHelper, by, Gender
import time


class LoggedOutHome(WebHelper):
    """
    A class used to represent the Login Page

    ...

    Attributes
    ----------
    tb_download_btn : WebDriverElement
        a Web Driver element representing the Download button
    tb_help_btn : WebDriverElement
        a Web Driver element representing the help button
    tb_premium_btn : WebDriverElement
        a Web Driver element representing the premium button
    getspotify_btn : WebDriverElement
        a Web Driver element representing the get spotify button
    fb_btn : WebDriverElement
        a Web Driver element representing the facebook page link button
    twitter_btn : WebDriverElement
        a Web Driver element representing the twitter page link button
    tb_signup_btn : WebDriverElement
        a Web Driver element representing the Signup button
    tb_login_btn : WebDriverElement
        a Web Driver element representing the Login button

    Methods
    -------
    click_signup()
        Clicks on the signup button
    click_login()
        Clicks on the login button
    """
    def __init__(self, driver):
        """
        Initializes the page elements

        :param driver : the driver to which the super class' driver is to be set
        :type driver: WebDriver
        """
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

    def click_login(self):
        """
        Clicks on the login button
        """
        self.click_button_safe(self.tb_login_btn)

    def click_signup(self):
        """
        Clicks on the signup button
        """
        self.click_button_safe(self.tb_signup_btn)

