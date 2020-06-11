import time

from Web_Testing.Pages.WebPlayerMenu import WebPlayerMenu
from collections import defaultdict

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Artist(WebPlayerMenu):
    """
       A class representing the Web Player's artist
       ...

       Attributes
       ----------
       search_btn_xpath : string
             A string containing the xpath of search button in home menu
       search_textbox_xpath : string
            A string containing the xpath of the search textbox in search page
       search_artist_xpath : string
            A sting containing the xpath of the artist appear after search in search page
       context_menu_xpath : string
             A string containing the xpath of context menu of the chosen artist
       follow_btn_xpath : string
             A string containing the xpath of follow button in the context menu of the chosen artist
       your_library_btn_xpath : string
             A string containing the xpath of your library button in home menu
       artist_btn_xpath : string
            A sting containing the xpath of artist button in your library page
       artist_cards_xpath : string
             A string containing the xpath of the list that contain all artists
       first_artist_xpath : string
            A sting containing the xpath of the first artist in artists
       artist_name : string
         A string containing the name of the artist to be added to the artists

       Methods
       -------
       overview()
           get number of artist before any action
       follow_artist()
           follow new artist
       unfollow_artist()
           unfollow artist
       """

    search_btn_xpath = "//*[@id='main']/div/div[2]/div[2]/nav/ul/li[2]/a"
    search_textbox_xpath = "//*[@id='main']/div/div[2]/div[1]/header/div[3]/div/div/input"
    search_artist_xpath = "//*[@id='searchPage']/div/div/section[1]/div/div[2]/div/div/div/div[4]"
    context_menu_xpath = "//*[@id='main']/div/nav[6]"
    follow_btn_xpath = "//*[@id='main']/div/nav[6]/div[2]"
    your_library_btn_xpath = "//*[@id='main']/div/div[2]/div[2]/nav/ul/li[3]/div/a"
    artist_btn_xpath = "//*[@id='main']/div/div[2]/div[1]/header/div[3]/div/nav/ul/li[3]/a"
    artist_cards_xpath = "//*[@id='main']/div/div[2]/div[4]/div[1]/div/div[2]/section[1]/div[1]/div"
    first_artist_xpath = "// *[ @ id = 'main'] / div / div[2] / div[4] / div[1] / div / div[2] / section[1] / div[1] / div[1]"
    artist_name = "Maher Zain"

    def __init__(self, driver):
        """
        Initializes the page elements

        :param driver : the driver to which the super class' driver is to be set
        :type driver: WebDriver
        """
        super().__init__(driver)

    def overview(self):
        """get number of artist before any action"""
        self.driver.find_element_by_xpath(self.your_library_btn_xpath).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(self.artist_btn_xpath).click()
        time.sleep(3)
        self.no_of_artist_before_add = len(self.driver.find_elements(By.XPATH, self.artist_cards_xpath))

    def follow_artist(self):
        """
                follow new artist

                :return: boolean true if no. of artists before follow is smaller than no. of artists after follow
                :rtype: bool
        """
        self.driver.find_element_by_xpath(self.search_btn_xpath).click()
        self.driver.find_element_by_xpath(self.search_textbox_xpath).send_keys(self.artist_name)
        time.sleep(15)
        ActionChains(self.driver).move_to_element(
            self.driver.find_element_by_xpath(self.search_artist_xpath)).context_click().perform()
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(self.context_menu_xpath))
        time.sleep(5)
        ActionChains(self.driver).move_to_element(
            self.driver.find_element_by_xpath(self.follow_btn_xpath)).click().perform()
        time.sleep(3)
        self.driver.find_element_by_xpath(self.your_library_btn_xpath).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(self.artist_btn_xpath).click()
        time.sleep(3)
        no_of_artist_after_add = len(self.driver.find_elements(By.XPATH, self.artist_cards_xpath))
        if self.no_of_artist_before_add < no_of_artist_after_add:
            return True
        else:
            return False

    def unfollow_artist(self):
        """
                unfollow artist

                :return: boolean true if no. of artists before unfollow is greater than no. of artists after unfollow
                :rtype: bool
        """
        if self.no_of_artist_before_add !=0:
            ActionChains(self.driver).move_to_element(
                self.driver.find_element_by_xpath(self.first_artist_xpath)).context_click().perform()
            ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(self.context_menu_xpath))
            time.sleep(5)
            ActionChains(self.driver).move_to_element(
                self.driver.find_element_by_xpath(self.follow_btn_xpath)).click().perform()
            time.sleep(5)
            no_of_artist_after_add = len(self.driver.find_elements(By.XPATH, self.artist_cards_xpath))
            if self.no_of_artist_before_add > no_of_artist_after_add:
                return True
            else:
                return False
        else:
            print("there is no artist to unfollow")
