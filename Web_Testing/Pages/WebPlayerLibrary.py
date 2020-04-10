import time

from Web_Testing.Pages.WebPlayerMenu import WebPlayerMenu
from collections import defaultdict


class WebPlayerLibrary(WebPlayerMenu):

    """
    A class representing the Web Player's Your Library Page
    ...

    Attributes
    ----------
    create_new_playlist_button : WebDriverElement
         a Web driver element representing the Create new playlist button
    profile_btn : WebDriverElement
         a Web driver element representing the profile drop down button button
    logout_btn : WebDriverElement
         a Web driver element representing the logout button
    account_btn : WebDriverElement
         a Web driver element representing the Account button
    liked_songs : WebDriverElement
         a Web driver element representing the Liked Songs button
    library_cards : WebDriverElement
         a Web driver element representing the Library cards button
    page_left_btn : WebDriverElement
         a Web driver element representing the Page left button
    page_right_btn : WebDriverElement
         a Web driver element representing the Page right button

    Methods
    -------
    click_liked_songs()
        Clicks the Liked Songs card
    check_liked_songs_click()
        Checks if clicking the Liked Songs card goes to the right page
    check_card_click(card_no, report_allure)
        Checks if clicking a playlist card goes to the right page

    """

    def __init__(self, driver):
        """
        Initializes the page elements

        :param driver : the driver to which the super class' driver is to be set
        :type driver: WebDriver
        """
        super().__init__(driver)
        self.create_new_playlist_button = self.find_element_by_xpath("//button[text()='Create new playlist']")
        self.profile_btn = self.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div/div/div[1]/div/nav/div/div/div/ul/ul/li/li/button/a")
        self.logout_btn = self.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div/div/div[1]/div/nav/div/div/div/ul/ul/li/li/div/button[2]/button")
        self.account_btn = self.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div/div/div[1]/div/nav/div/div/div/ul/ul/li/li/div/button[1]/a")
        self.liked_songs = self.find_element_by_class_name("LikedSongs")
        self.library_cards = self.find_elements_by_class_name("CardsLibrary")
        self.page_left_btn = self.find_element_by_xpath("/html/body/div/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div[1]/div/nav/div/div/div/ul/li[1]/button/a")
        self.page_right_btn = self.find_element_by_xpath("/html/body/div/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div[1]/div/nav/div/div/div/ul/li[2]/button/a")
# TrackListHeader Body

    def click_liked_songs(self):
        """
        Clicks the Liked Songs card
        """
        self.hover_to_element(self.liked_songs)
        time.sleep(2)
        liked_songs_btn = self.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div[2]/div/div/button")
        if liked_songs_btn is not None:
            liked_songs_btn.click()

    def check_liked_songs_click(self):
        """
        Checks if clicking the Liked Songs card goes to the right page

        :returns: a boolean True if clicking the Liked Songs card goes to the right page, False otherwise
        :rtype: bool
        """
        self.click_liked_songs()
        time.sleep(4)
        return self.url_has("webplayer/likedplay", self.driver)

    def check_card_click(self, card_no, report_allure: bool):
        """
        Checks if clicking a playlist card goes to the right page

        :param card_no: the playlist's card number
        :type card_no: int

        :param report_allure: a boolean that represents whether or not to report the result to allure
        :type report_allure: bool

        :returns: a boolean True if clicking the Playlist card goes to the right page, False otherwise
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
        card_text = splitted_card_text[0] + " " + splitted_card_text[1]
        card.click()
        time.sleep(4)
        playlist_info_name = self.find_element_by_xpath("/html/body/div/div/div/div/div[1]/div/div/div[2]/div/div/section/div/section/div/div/div[1]/div/header/div[1]/div/div[2]/div/div[1]/span")

        if playlist_info_name is None:
            return False

        if playlist_info_name.text != card_text and report_allure:
            self.report_allure("ERROR: Playlist name is not the same as the card name. Card name = " + card_text + ", Playlist name = " + playlist_info_name.text)

        return self.url_has("webplayer/nowplay")




