import time

from Web_Testing.Pages.WebPlayerMenu import WebPlayerMenu
from collections import defaultdict

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class LikedSongs(WebPlayerMenu):
    """
       A class representing the Web Player's liked songs
       ...

       Attributes
       ----------
       search_btn_xpath : string
             A string containing the xpath of search button in home menu
       search_textbox_xpath : string
            A string containing the xpath of the search textbox in search page
       song_xpath : string
            A sting containing the xpath of the song appear after search in search page
       context_menu_xpath : string
             A string containing the xpath of context menu of the chosen song
       save_to_like_btn_xpath : string
             A string containing the xpath of save to liked button in the context menu of the chosen song
       liked_songs_list_xpath : string
             A string containing the xpath of the list that contain all liked songs
       liked_songs_btn_xpath : string
          A string containing the xpath of liked songs button in home menu
       first_liked_song_xpath : string
            A sting containing the xpath of the first song in liked songs
       song_name : string
         A string containing the name of the song to be added to the liked songs

       Methods
       -------
       overview()
           get number of songs before any action
       like_song()
           like new song
       unlike_song()
           unlike song
       """

    search_btn_xpath = "//*[@id='main']/div/div[2]/div[2]/nav/ul/li[2]/a"
    search_textbox_xpath = "//*[@id='main']/div/div[2]/div[1]/header/div[3]/div/div/input"
    song_xpath = "//*[@id='searchPage']/div/div/section[1]/div/div[2]/div/div/div/div[4]"
    context_menu_xpath = "//*[@id='main']/div/nav[1]"
    save_to_like_btn_xpath = "//*[@id='main']/div/nav[1]/div[2]"
    liked_songs_list_xpath = "//*[@id='main']/div/div[2]/div[4]/div[1]/div/div[2]/section[1]/div[4]/section/ol/div"
    liked_songs_btn_xpath = "//*[@id='main']/div/div[2]/div[2]/nav/div[2]/div/div/div[2]/a"
    first_liked_song_xpath = "//*[@id='main']/div/div[2]/div[4]/div[1]/div/div[2]/section[1]/div[4]/section/ol/div[1]/div/li"
    song_name = "memories maroon 5"

    def __init__(self, driver):
        """
        Initializes the page elements

        :param driver : the driver to which the super class' driver is to be set
        :type driver: WebDriver
        """
        super().__init__(driver)

    def overview(self):
        """get number of songs before any action"""
        self.driver.find_element_by_xpath(self.liked_songs_btn_xpath).click()
        time.sleep(3)
        self.no_of_liked_songs_before_add = len(self.driver.find_elements(By.XPATH, self.liked_songs_list_xpath))

    def like_song(self):
        """
                like new song

                :return: boolean true if no. of songs before like is smaller than no. of songs after like
                :rtype: bool
        """
        self.driver.find_element_by_xpath(self.search_btn_xpath).click()
        self.driver.find_element_by_xpath(self.search_textbox_xpath).send_keys(self.song_name)
        time.sleep(5)
        ActionChains(self.driver).move_to_element(
            self.driver.find_element_by_xpath(self.song_xpath)).context_click().context_click().perform()
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(self.context_menu_xpath))
        time.sleep(5)
        ActionChains(self.driver).move_to_element(
            self.driver.find_element_by_xpath(self.save_to_like_btn_xpath)).click().perform()
        time.sleep(10)
        self.driver.find_element_by_xpath(self.liked_songs_btn_xpath).click()
        time.sleep(3)
        no_of_liked_songs_after_add = len(self.driver.find_elements(By.XPATH, self.liked_songs_list_xpath))
        if self.no_of_liked_songs_before_add < no_of_liked_songs_after_add:
            return True
        else:
            return False

    def unlike_song(self):
        """
                unlike song

                :return: boolean true if no. of songs before unlike is greater than no. of songs after unlike
                :rtype: bool
        """
        if self.no_of_liked_songs_before_add != 0:
            ActionChains(self.driver).move_to_element(
                self.driver.find_element_by_xpath(self.first_liked_song_xpath)).context_click().context_click().perform()
            ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(self.context_menu_xpath))
            time.sleep(5)
            ActionChains(self.driver).move_to_element(
                self.driver.find_element_by_xpath(self.save_to_like_btn_xpath)).click().perform()
            time.sleep(10)
            no_of_liked_songs_after_add = len(self.driver.find_elements(By.XPATH, self.liked_songs_list_xpath))
            if self.no_of_liked_songs_before_add > no_of_liked_songs_after_add:
                return True
            else:
                return False
        else:
            print ("there is no song to unlike")
