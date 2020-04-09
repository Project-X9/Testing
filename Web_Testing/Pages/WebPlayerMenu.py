from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Web_Testing.helperClasses import WebHelper
from selenium.webdriver.support import expected_conditions as EC

class WebPlayerMenu(WebHelper):
    def __init__(self, driver):
        super().__init__()
        self.set_driver(driver)
        self.home_link = self.find_element_by_xpath("//text()[.='Home']/ancestor::a[1]")
        self.search_link = self.find_element_by_xpath("//text()[.='Search']/ancestor::a[1]")
        self.your_library_button = self.find_element_by_xpath("/html/body/div/div/div/div/div[1]/div/div/div[1]/div/button")
        self.liked_songs_link = self.find_element_by_xpath("//text()[.='Liked Songs']/ancestor::a[1]")
        self.create_playlist_link = self.find_element_by_xpath("//text()[.='Create Playlist']/ancestor::a[1]")
        self.back_btn = self.find_element_by_xpath("/html/body/div/div/div/div/div[1]/div/div/div[2]/div/div/div[1]/div/div/nav/ul[1]/li[1]/button/a")
        self.forward_btn = self.find_element_by_xpath("/html/body/div/div/div/div/div[1]/div/div/div[2]/div/div/div[1]/div/div/nav/ul[1]/li[2]/button/a")
        self.profile_btn = self.find_element_by_xpath("/html/body/div/div/div/div/div[1]/div/div/div[2]/div/div/div[1]/div/div/nav/ul[2]/li/li/div[1]/button/a")
        self.logout_btn = self.find_element_by_xpath("/html/body/div/div/div/div/div[1]/div/div/div[2]/div/div/div[1]/div/div/nav/ul[2]/li/li/div[2]/button[3]/button")
        self.account_btn = self.find_element_by_xpath("/html/body/div/div/div/div/div[1]/div/div/div[2]/div/div/div[1]/div/div/nav/ul[2]/li/li/div[2]/button[1]/a")

    def click_logout(self):
        """Clicks Logout button in profile list"""
        self.profile_btn.click()
        logout_btn_xpath = "/html/body/div/div/div/div/div[1]/div/div/div[2]/div/div/div[1]/div/div/nav/ul[2]/li/li/div[2]/button[3]/button"
        logout_btn_element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, logout_btn_xpath)))
        logout_btn_element.click()

    def click_your_library(self):
        (self.find_element_by_xpath("/html/body/div/div/div/div/div[1]/div/div/div[1]/div/button")).click()

    def click_account(self):
        self.profile_btn.click()
        element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.account_btn)))
        did_scroll = element.location_once_scrolled_into_view
        element.click()

    def click_back_button(self):
        self.back_btn = self.find_element_by_xpath(
            "/html/body/div/div/div/div/div[1]/div/div/div[2]/div/div/div[1]/div/div/nav/ul[1]/li[1]/button/a")
        self.back_btn.click()

    def click_forward_button(self):
        self.forward_btn = self.find_element_by_xpath(
            "/html/body/div/div/div/div/div[1]/div/div/div[2]/div/div/div[1]/div/div/nav/ul[1]/li[2]/button/a")
        self.forward_btn.click()


