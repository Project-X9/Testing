import time

from Web_Testing.Pages.WebPlayerMenu import WebPlayerMenu
from collections import defaultdict


class WebPlayerPlaylist(WebPlayerMenu):
    """
    A class representing the Web Player's playlist
    ...

    Attributes
    ----------
    profile_btn : string
          A string containing the xpath of profile button
    logout_btn : string
          A string containing the xpath of log out button
    account_btn : string
          A string containing the link text of account button
    upgrade_btn : string
          A string containing the link text of upgrade button
    playlist_cards : string
          A string containing the class name of playlist cards
    no_of_songs_xpath : string
          A string containing the xpath of number of song in the playlist
    playlist_name_class_name : string
          A string containing the class name of playlist's name in the playlist page
    songs_container : string
          A string containing the class name of songs in the playlist
    no_of_songs : integer
          An integer containing the number of songs displayed in the playlist page
    playlist_name_card : string
         A sting containing the name of the play list from the playlist card
    page_left_btn : WebDriverElement
         a Web driver element representing the Page left button
    page_right_btn : WebDriverElement
         a Web driver element representing the Page right button

    Methods
    -------
    click_liked_songs()
        Clicks the Liked Songs Play button in the card
    click_liked_songs_txt()
        Clicks the Liked Songs Text button in the card
    check_liked_songs_click()
        Checks if clicking the Liked Songs card goes to the right page
    check_card_click(card_no, report_allure)
        Checks if clicking a playlist card goes to the right page

    """

    profile_btn = "//*[@id='root']/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div/nav/ul[2]/li[2]/li/div[1]/button"
    logout_btn = "//*[@id='root']/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div/nav/ul[2]/li[2]/li/div[2]/button[3]/button"
    account_btn = "Account"
    playlist_cards = "CardsLibrary"
    upgrade_btn = "UPGRADE"
    no_of_songs_xpath = "//*[@id='root']/div/div/div/div[1]/div/div/div[2]/div/div/section/div/section/div/div/div[1]/div/header/div[2]/div[2]/div/p"
    playlist_name_class_name = "TrackListHeader mo info Name"
    songs_container = "TrackListContainer"
    no_of_songs = 0
    playlist_name_card = "cardTitle row"
    page_left_btn = "/html/body/div/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div[1]/div/nav/div/div/div/ul/li[1]/button/a"
    page_right_btn = "/html/body/div/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div[1]/div/nav/div/div/div/ul/li[2]/button/a"

    def __init__(self, driver):
        """
        Initializes the page elements

        :param driver : the driver to which the super class' driver is to be set
        :type driver: WebDriver
        """
        super().__init__(driver)
        self.library_cards = self.find_elements_by_class_name("CardsLibrary")

    def click_profile(self):
        """Clicks Profile button"""
        self.click_button_safe(self.find_element_by_xpath(self.profile_btn))

    def click_account(self):
        """Clicks Account button in profile list"""
        self.click_profile()
        self.click_button_safe(self.find_element_by_link_text(self.account_btn))

    def click_logout_button(self):
        """Clicks Logout button in profile list"""
        self.click_profile()
        self.click_button_safe(self.find_element_by_xpath(self.logout_btn))

    def check_upgrade(self, premium):
        """
        check the upgrade button existence with the type of the account

        :param premium: boolean to show if this account is premium or not
        :type: bool

        :return: true if join premium button don't exist when premium is true and exist when premium is false
        :type: bool
        """
        if (premium is True and self.find_element_by_link_text(self.upgrade_btn) is None) or (
                premium is False and self.find_element_by_link_text(self.upgrade_btn) is not None):
            return True
        else:
            return False

    def click_upgrade(self):
        """Clicks upgrade button"""
        self.click_button_safe(self.find_element_by_link_text(self.upgrade_btn))

    def click_webplayer(self):
        self.click_button_safe(self.find_element_by_link_text("Web Player"))

    def click_page_left(self):
        """Clicks page left button"""
        self.click_button_safe(self.find_element_by_xpath(self.page_left_btn))

    def click_page_right(self):
        """Clicks page right button"""
        self.click_button_safe(self.find_element_by_xpath(self.page_right_btn))

    def click_playlist_play_btn(self, card_no: int = 0):
        """
        Clicks the playlist Play button in the card
        :param card_no: the card number of the playlist
        :type card_no: int
        """
        card = None
        try:
            card = self.library_cards[card_no]
        except:
            return
        if card is None:
            card.click()

    def check_playlist(self, card_no, report_allure: bool):
        """
        Checks if clicking a playlist card goes to the right playlist

        :param card_no: the playlist's card number
        :type card_no: int

        :param report_allure: a boolean that represents whether or not to report the result to allure
        :type report_allure: bool

        :returns: a boolean True if clicking the Playlist card goes to the right playlist, False otherwise
        :rtype: bool
        """
        card = None
        try:
            card = self.library_cards[card_no]
        except:
            if report_allure:
                self.report_allure("ERROR: This card number is not available", self.driver)
            return False
        splitted_card_text = card.text.split(" ")
        print(splitted_card_text)
        card_text = splitted_card_text[0] + " " + splitted_card_text[1]
        card.click()
        time.sleep(4)
        no_of_songs_txt_arr = self.find_element_by_xpath(self.no_of_songs_xpath).text.split(" ")
        no_of_songs_txt = no_of_songs_txt_arr[0]
        songs_container_arr = self.find_elements_by_class_name(self.songs_container)
        songs_container_text_arr = list()
        for item in songs_container_arr:
            songs_container_text_arr.append(item.text)

        songs_container_text_arr = list(dict.fromkeys(songs_container_text_arr))
        self.no_of_songs = len(songs_container_text_arr)
        print(songs_container_arr[0].text)
        # print(songs_container_arr[1].text)
        print(self.no_of_songs)
        print(no_of_songs_txt)
        print()
        print(songs_container_text_arr)
        if no_of_songs_txt != str(self.no_of_songs):
            return False
        else:
            return True
