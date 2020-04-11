import time

from Web_Testing.Pages.WebPlayerMenu import WebPlayerMenu
from collections import defaultdict


class Artist(WebPlayerMenu):
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
    follow_btn = "//*[@id='followButton']"
    related_artist = "//*[@id='ab']"
    about = "/html/body/div[1]/div/div/div/div[1]/div/div/div[2]/div/div/div/div[3]/button[3]"
    page_left_btn = "/html/body/div/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div[1]/div/nav/div/div/div/ul/li[1]/button/a"
    page_right_btn = "/html/body/div/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div[1]/div/nav/div/div/div/ul/li[2]/button/a"
    artist_name = "Header1"
    artist_name_about = "//*[@id='bio-body']"
    artist_link = "Artists"
    artist_image = "//*[@id='root']/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div[2]/div/div/button/a/div/div[1]/div/div/div/div/img"

    def __init__(self, driver):
        """
        Initializes the page elements

        :param driver : the driver to which the super class' driver is to be set
        :type driver: WebDriver
        """
        super().__init__(driver)

    def click_artist(self):
        """Clicks artist button"""
        self.click_button_safe(self.find_element_by_link_text(self.artist_link))

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

    def click_related_artist(self):
        """Clicks Profile button"""
        self.click_button_safe(self.find_element_by_xpath(self.related_artist))

    def click_related_artist(self):
        """Clicks Profile button"""
        self.click_button_safe(self.find_element_by_xpath(self.related_artist))

    def check_follow(self):
        """
        check clicking follow button

        :return: true if follow button change to unfollow
        :type: bool
        """

        self.click_button_safe(self.find_element_by_xpath(self.artist_image))
        time.sleep(6)
        self.click_follow()
        time.sleep(3)
        print(self.find_element_by_xpath(self.follow_btn).text)
        if self.find_element_by_xpath(self.follow_btn).text == "UNFOLLOW":
            return True
        else:
            return False

    def click_follow(self):
        """Clicks upgrade button"""
        self.click_button_safe(self.find_element_by_xpath(self.follow_btn))

    def click_webplayer(self):
        self.click_button_safe(self.find_element_by_link_text("Web Player"))

    def click_page_left(self):
        """Clicks page left button"""
        self.click_button_safe(self.find_element_by_xpath(self.page_left_btn))

    def click_page_right(self):
        """Clicks page right button"""
        self.click_button_safe(self.find_element_by_xpath(self.page_right_btn))

    def click_about(self):
        self.click_button_safe(self.find_element_by_xpath(self.about))

    def check_about(self):
        self.click_button_safe(self.find_element_by_xpath(self.artist_image))
        time.sleep(6)
        self.click_about()
        time.sleep(6)
        about_split = self.find_element_by_xpath(self.artist_name_about).text.split(" ")
        name = about_split[0] + " " + about_split[1]
        print(name)
        print("\n")
        print(self.find_element_by_class_name(self.artist_name).text)
        if self.find_element_by_class_name(self.artist_name).text == name:
            return True
        else:
            return False
