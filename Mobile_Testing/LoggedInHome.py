
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Web_Testing.helperClasses import WebHelper, by, Gender
import time
from Mobile_Testing.helperClasses import MobileHelper


class LoggedInHome(MobileHelper):

    def __init__(self, driver):
        # tb refers to Toolbar, tb_.. refers to Toolbar elements
        self.driver = driver
        self.logout_btn = self.find_element_by_id(self.driver, "id/logOut_bt")
        self.open_playlist_btn = self.find_element_by_id(self.driver, "id/openPlaylist")
        self.play_music_btn = self.find_element_by_id(self.driver, "id/playMusic")

    def is_open(self):
        if (self.logout_btn is None):
            return False
        else:
            return True

    def click_logout_button(self):
        self.logout_btn.click()

    def click_playlist_button(self):
        self.open_playlist_btn.click()

    def click_play_music_button(self):
        self.play_music_btn.click()

