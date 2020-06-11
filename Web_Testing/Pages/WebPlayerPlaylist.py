import time

from Web_Testing.Pages.WebPlayerMenu import WebPlayerMenu
from collections import defaultdict

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class WebPlayerPlaylist(WebPlayerMenu):
    """
    A class representing the Web Player's playlist
    ...

    Attributes
    ----------
    three_dots_xpath : string
          A string containing the xpath of the three dots that open context of the chosen playlist
    context_menu_xpath : string
          A string containing the xpath of context menu of the chosen playlist
    home_context_menu_xpath : string
          A string containing the xpath of context menu of the chosen playlist in home menu
    rename_btn_xpath : string
        A sting containing the xpath of rename button in the context menu of the chosen playlist
    create_playlist_btn_xpath : string
          A string containing the xpath of create playlist button in home menu
    playlist_name_textbox_xpath : string
          A string containing the xpath of the textbox that appear at creation of new playlist to write the name
    create_btn_xpath : string
          A string containing the xpath of create button in the modal that appear at creation of new playlist to confirm creation action
    cancel_creation_btn_xpath : string
          A string containing the xpath of cancel button in the modal that appear at creation of new playlist to cancel creation action
    cancel_deletion_btn_xpath : string
          A string containing the xpath of cancel button in the modal that appear at deletion of playlist to cancel deletion action
    playlists_cards_xpath : string
          A string containing the xpath of the list that contain all playlist
    your_library_btn_xpath : string
          A string containing the xpath of your library button in home menu
    first_playlist_xpath : string
         A sting containing the xpath of the first playlist in home menu
    delete_btn_xpath : string
         A sting containing the xpath of delete button in the context menu of the chosen playlist
    modal_delete_btn : string
         A string containing the xpath of delete button in the modal that appear at deletion of playlist to confirm deletion action
    playlist_name : string
         A string containing the name of the new playlist
    rename_textbox_class_name : string
            A string containing the class name of the textbox that appear at rename of existing playlist to write the name
    playlist_name_xpath : string
            A sting containing the xpath of span containing name of the playlist

    Methods
    -------
    get_no_of_playlist()
        get number of playlist before any action
    create_playlist()
        create new playlist
    cancel_creation()
        cancel creation of new playlist
    delete_playlist()
        delete playlist
    cancel_deletion()
        cancel deletion of playlist
    name_overview()
        get name before any action
    rename_playlist()
        rename existing playlist

    """

    three_dots_xpath = "//*[@id='main']/div/div[2]/div[4]/div[1]/div/div[2]/section[1]/div[3]/div/div/button"
    context_menu_xpath = "// *[ @ id = 'main'] / div / nav[3]"
    home_context_menu_xpath= "// *[ @ id = 'main'] / div / nav[4]"
    rename_btn_xpath = "//*[@id='main']/div/nav[4]/div[6]"
    create_playlist_btn_xpath = "//*[@id='main']/div/div[2]/div[2]/nav/div[2]/div/div/div[1]/button"
    playlist_name_textbox_xpath = "//*[@id='main']/div/div[3]/div/div[1]/div/div/input"
    create_btn_xpath = "//*[@id='main']/div/div[3]/div/div[2]/div[2]/button"
    cancel_creation_btn_xpath = "//*[@id='main']/div/div[3]/div/div[2]/div[1]/button"
    cancel_deletion_btn_xpath = "// *[ @ id = 'main'] / div / div[3] / div / div / div[1] / button"
    your_library_btn_xpath = "//*[@id='main']/div/div[2]/div[2]/nav/ul/li[3]/div/a"
    playlists_cards_xpath = "//*[@id='main']/div/div[2]/div[4]/div[1]/div/div[2]/section[1]/div[1]/div"
    first_playlist_xpath = "//*[@id='main']/div/div[2]/div[2]/nav/div[2]/div/div/ul/div[1]/li/div/div/div/a"
    delete_btn_xpath = "//*[@id='main']/div/nav[3]/div[3]"
    modal_delete_btn = "//*[@id='main']/div/div[3]/div/div/div[2]/button"
    playlist_name = "playlist test"
    rename_textbox_class_name = "TextInput__input"
    playlist_name_xpath = "//*[@id='main']/div/div[2]/div[2]/nav/div[2]/div/div/ul/div[1]/li/div/div/div/a/div/span"


    def __init__(self, driver):
        """
        Initializes the driver

        :param driver : the driver to which the super class' driver is to be set
        :type driver: WebDriver
        """
        super().__init__(driver)

    def get_no_of_playlist(self):
        """get number of playlist before any action"""
        self.driver.find_element_by_xpath(self.your_library_btn_xpath).click()
        time.sleep(3)
        self.no_of_playlists_before_add = (len(self.driver.find_elements(By.XPATH, self.playlists_cards_xpath))) - 1

    def create_playlist(self):
        """
                create new playlist

                :return: boolean true if no. of playlist before creation is smaller than no. of playlist after creation
                :rtype: bool
        """
        self.driver.find_element_by_xpath(self.create_playlist_btn_xpath).click()
        self.driver.find_element_by_xpath(self.playlist_name_textbox_xpath).send_keys(self.playlist_name)
        self.driver.find_element_by_xpath(self.create_btn_xpath).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(self.your_library_btn_xpath).click()
        time.sleep(3)
        no_of_playlists_after_add = (len(self.driver.find_elements(By.XPATH, self.playlists_cards_xpath))) - 1
        if self.no_of_playlists_before_add < no_of_playlists_after_add:
            return True
        else:
            return False

    def cancel_creation(self):
        """
                cancel creation of new playlist

                :return: boolean true if no. of playlist before cancel creation is equal no. of playlist after cancel creation
                :rtype: bool
        """
        self.driver.find_element_by_xpath(self.create_playlist_btn_xpath).click()
        self.driver.find_element_by_xpath(self.playlist_name_textbox_xpath).send_keys(self.playlist_name)
        self.driver.find_element_by_xpath(self.cancel_creation_btn_xpath).click()
        self.driver.find_element_by_xpath(self.your_library_btn_xpath).click()
        time.sleep(3)
        no_of_playlists_after_add = (len(self.driver.find_elements(By.XPATH, self.playlists_cards_xpath))) - 1
        if self.no_of_playlists_before_add == no_of_playlists_after_add:
            return True
        else:
            return False

    def delete_playlist(self):
        """
                delete playlist

                :return: boolean true if no. of playlist before deletion is greater than no. of playlist after deletion
                :rtype: bool
        """
        self.driver.find_element_by_xpath(self.first_playlist_xpath).click()
        time.sleep(10)
        ActionChains(self.driver).click_and_hold(self.driver.find_element_by_xpath(self.three_dots_xpath)).perform()
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(self.context_menu_xpath))
        time.sleep(5)
        ActionChains(self.driver).move_to_element(
            self.driver.find_element_by_xpath(self.delete_btn_xpath)).click().click().perform()
        time.sleep(10)
        self.driver.find_element_by_xpath(self.modal_delete_btn).click()
        self.driver.find_element_by_xpath(self.your_library_btn_xpath).click()
        time.sleep(3)
        no_of_playlists_after_add = (len(self.driver.find_elements(By.XPATH, self.playlists_cards_xpath))) - 1
        if self.no_of_playlists_before_add > no_of_playlists_after_add:
            return True
        else:
            return False

    def cancel_deletion(self):
        """
                cancel deletion of playlist

                :return: boolean true if no. of playlist before cancel deletion is equal no. of playlist after cancel deletion
                :rtype: bool
        """
        self.driver.find_element_by_xpath(self.first_playlist_xpath).click()
        time.sleep(5)
        ActionChains(self.driver).click_and_hold(self.driver.find_element_by_xpath(self.three_dots_xpath)).perform()
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(self.context_menu_xpath))
        time.sleep(5)
        ActionChains(self.driver).move_to_element(
            self.driver.find_element_by_xpath(self.delete_btn_xpath)).click().click().perform()
        time.sleep(10)
        self.driver.find_element_by_xpath(self.cancel_deletion_btn_xpath).click()
        self.driver.find_element_by_xpath(self.your_library_btn_xpath).click()
        time.sleep(3)
        no_of_playlists_after_add = (len(self.driver.find_elements(By.XPATH, self.playlists_cards_xpath))) - 1
        if self.no_of_playlists_before_add == no_of_playlists_after_add:
            return True
        else:
            return False

    def name_overview(self):
        """get name before any action"""
        self.driver.find_element_by_xpath(self.first_playlist_xpath).click()
        self.playlist_name_before = self.driver.find_element_by_xpath(self.playlist_name_xpath).text

    def rename_playlist(self):
        """
                rename existing playlist

                :return: integer 0 if playlist's name before rename is not equal playlist's name after rename and playlist's name after rename is equal desired name,
                1 if playlist's name before rename is equal playlist's name after rename, 2 if playlist's name after rename is not equal desired name and not equal playlist's name before rename
                :rtype: int
        """
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(self.first_playlist_xpath)).context_click().context_click().perform()
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(self.home_context_menu_xpath))
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(self.rename_btn_xpath)).click().perform()
        self.driver.find_element_by_class_name(self.rename_textbox_class_name).send_keys(self.playlist_name)
        self.driver.find_element_by_class_name(self.rename_textbox_class_name).send_keys(Keys.ENTER)
        playlist_name_after = self.driver.find_element_by_xpath(self.playlist_name_xpath).text
        if self.playlist_name_before != playlist_name_after and playlist_name_after == self.playlist_name:
            return 0
        else:
            if self.playlist_name_before == playlist_name_after:
                return 1
            elif playlist_name_after != self.playlist_name and self.playlist_name_before != playlist_name_after:
                return 2

