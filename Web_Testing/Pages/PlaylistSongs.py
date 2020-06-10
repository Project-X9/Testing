import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from Web_Testing.Pages.WebPlayerMenu import WebPlayerMenu


class PlaylistSongs(WebPlayerMenu):
    """
       A class representing the Web Player's playlist songs
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
       remove_from_playlist_btn_xpath : string
             A string containing the xpath of remove from  playlist button in the context menu of the chosen song
       add_to_playlist_btn_xpath : string
            A string containing the xpath of add to playlist button in the context menu of the chosen song
       playlist_xpath : string
             A string containing the xpath of the playlist in the add to playlist modal
       your_library_btn_xpath : string
             A string containing the xpath of your library button in home menu
       first_playlist_xpath : string
            A sting containing the xpath of the first playlist in home menu
       playlist_songs_list_xpath : string
             A string containing the xpath of the list that contain all playlist songs
       first_playlist_song_xpath : string
            A sting containing the xpath of the first song in the playlist
       song_name : string
         A string containing the name of the song to be added to the playlist

       Methods
       -------
       overview()
           get number of songs before any action
       add_song_to_playlist()
           add new song to playlist
       remove_song_from_playlist()
           remove a song from playlist
       """

    search_btn_xpath = "//*[@id='main']/div/div[2]/div[2]/nav/ul/li[2]/a"
    search_textbox_xpath = "//*[@id='main']/div/div[2]/div[1]/header/div[3]/div/div/input"
    song_xpath = "//*[@id='searchPage']/div/div/section[1]/div/div[2]/div/div/div/div[4]"
    context_menu_xpath = "//*[@id='main']/div/nav[1]"
    remove_from_playlist_btn_xpath = "// *[ @ id = 'main'] / div / nav[1] / div[5]"
    add_to_playlist_btn_xpath = "//*[@id='main']/div/nav[1]/div[4]"
    playlist_xpath = "// *[ @ id = 'main'] / div / div[3] / div / div[2] / div"
    your_library_btn_xpath = "//*[@id='main']/div/div[2]/div[2]/nav/ul/li[3]/div/a"
    first_playlist_xpath = "//*[@id='main']/div/div[2]/div[2]/nav/div[2]/div/div/ul/div[1]/li/div/div/div/a"
    playlist_songs_list_xpath = "//*[@id='main']/div/div[2]/div[4]/div[1]/div/div[2]/section[1]/div[4]/section/ol/div"
    first_playlist_song_xpath = "//*[@id='main']/div/div[2]/div[4]/div[1]/div/div[2]/section[1]/div[4]/section/ol/div[1]/div/li"
    song_name="memories maroon 5"

    def __init__(self, driver):
        """
              Initializes the driver

               :param driver : the driver to which the super class' driver is to be set
               :type driver: WebDriver
               """
        super().__init__(driver)

    def overview(self):
        """get number of songs before any action"""
        self.driver.find_element_by_xpath(self.first_playlist_xpath).click()
        time.sleep(3)
        self.no_of_playlist_songs_before_add = len(self.driver.find_elements(By.XPATH, self.playlist_songs_list_xpath))

    def add_song_to_playlist(self):
        """
                add new song to playlist

                :return: boolean true if no. of songs before add is smaller than no. of songs after add
                :rtype: bool
        """
        self.driver.find_element_by_xpath(self.search_btn_xpath).click()
        self.driver.find_element_by_xpath(self.search_textbox_xpath).send_keys(self.song_name)
        time.sleep(15)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(self.song_xpath)).context_click().context_click().perform()
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(self.context_menu_xpath))
        time.sleep(5)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(self.add_to_playlist_btn_xpath)).click().perform()
        time.sleep(3)
        self.driver.find_element_by_xpath(self.playlist_xpath).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(self.first_playlist_xpath).click()
        time.sleep(3)
        no_of_playlist_songs_after_add = len(self.driver.find_elements(By.XPATH, self.playlist_songs_list_xpath))
        if self.no_of_playlist_songs_before_add < no_of_playlist_songs_after_add:
            return True
        else:
            return False

    def remove_song_from_playlist(self):
        """
                remove a song from playlist

                :return: boolean true if no. of songs before remove is greater than no. of songs after remove
                :rtype: bool
        """
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(self.first_playlist_song_xpath)).context_click().context_click().perform()
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(self.context_menu_xpath))
        time.sleep(5)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(self.remove_from_playlist_btn_xpath)).click().perform()
        time.sleep(5)
        no_of_playlist_songs_after_add = len(self.driver.find_elements(By.XPATH, self.playlist_songs_list_xpath))
        if self.no_of_playlist_songs_before_add > no_of_playlist_songs_after_add:
            return True
        else:
            return False