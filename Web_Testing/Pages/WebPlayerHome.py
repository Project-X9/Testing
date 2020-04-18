from Web_Testing.Pages.WebPlayerMenu import WebPlayerMenu
from Web_Testing.helperClasses import WebHelper
import time


class WebPlayerHome(WebPlayerMenu):
    """
    A class used to represent the Web Player Home
    ...

    Attributes
    ----------
    upgrade_link : WebDriverElement
         a Web driver element representing the upgrade button
    spotify_logo : WebDriverElement
         a Web driver element representing the spotify logo
    signup_btn : WebDriverElement
         a Web driver element representing the signup button
    login_btn : WebDriverElement
         a Web driver element representing the login button
    signup_popup_btn : WebDriverElement
         a Web driver element representing the signup button that appears in the popup window
    login_popup_btn : WebDriverElement
         a Web driver element representing the login button that appears in the popup window
    close_popup_btn : WebDriverElement
         a Web driver element representing the close button that appears in the popup window
    popup_window : WebDriverElement
         a Web driver element representing the popup window
    all_cards : list
         a list of all the cards available in the home page
    all_headers : list
         a list of all the headers/categories available in the home page
    header_names_to_cards : dict
         a dict that maps the header names/categories to the list of cards in this category


    Methods
    -------
    is_in_your_library()
        Checks if currently in Your Library Page
    is_in_liked_songs()
        Checks if currently in Liked Songs Page
    initialize_popup_window()
        Initializes the elements of the popup window
    is_popup_window_visible()
        Checks if the popup menu is visible
    map_headers_to_cards(all_headers, all_cards)
        Return a dict that maps the header names/categories to the list of cards in this category
    get_cards_for_header(all_cards, y_pos_header)
        Returns a list of cards corresponding to a header's y position
    get_cards_of(category)
        Returns a list of cards for a given category name
    check_card_click(category_name, card_no, report_allure)
        Checks if clicking a card goes to the correct page
    check_sign_out()
        Checks sign out and popup window that appears after the sign out
    click_login()
        Clicks the login button
    click_signup()
        Clicks the signup button
    """

    def __init__(self, driver):
        """
        Initializes the page elements

        :param driver : the driver to which the super class' driver is to be set
        :type driver: WebDriver
        """
        super().__init__(driver)
        self.upgrade_link = self.find_element_by_xpath("//a[text()='UPGRADE']")
        self.spotify_logo = self.find_element_by_xpath(
            "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/nav[1]/div[1]/div[1]/div[1]/ul[1]/li[5]/a[1]")

        self.signup_btn = self.find_element_by_xpath("//a[text()='SIGN UP']")
        self.login_btn = self.find_element_by_xpath("//text()[.='LOG IN']/ancestor::button[1]")
        self.signup_popup_btn = self.find_element_by_xpath("//a[text()='Sign up free']")
        self.login_popup_btn = self.find_element_by_xpath("//a[text()='Log in']")
        self.close_popup_btn = self.find_element_by_xpath("//button[text()='Close']")
        self.popup_window = self.find_element_by_xpath(
            "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]")
        self.all_cards = self.find_elements_by_class_name("CardsHome")
        self.all_headers = self.find_elements_by_class_name("HeaderAboveGrid")
        self.header_names_to_cards = self.map_headers_to_cards(self.all_headers, self.all_cards)

    def is_in_your_library(self) -> bool:
        """
        Checks if currently in Your Library Page
        :returns: a boolean True if currently in Your Library page, False otherwise
        :rtype: bool
        """
        return self.url_has("/librarypage")

    def is_in_liked_songs(self) -> bool:
        """
        Checks if currently in Liked Songs Page
        :returns: a boolean True if currently in Liked Songs page, False otherwise
        :rtype: bool
        """
        return self.url_has("/likedplay")

    def initialize_popup_window(self):
        """
        Initializes the elements of the popup window
        """
        self.signup_popup_btn = self.find_element_by_xpath("//a[text()='Sign up free']")
        self.login_popup_btn = self.find_element_by_xpath("//a[text()='Log in']")
        self.close_popup_btn = self.find_element_by_xpath("//button[text()='Close']")
        self.popup_window = self.find_element_by_xpath(
            "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]")

    def is_popup_window_visible(self):
        """
        Checks if the popup menu is visible
        :return: a boolean True if the popup menu is visible, False otherwise
        :rtype: bool
        """
        self.initialize_popup_window()
        if (self.login_popup_btn is None) or (self.close_popup_btn is None) or (self.signup_popup_btn is None):
            return False
        else:
            return True

    def map_headers_to_cards(self, all_headers, all_cards):
        """
        Gets a dict that maps the header names/categories to the list of cards in this category
        :param all_headers: list of all the header elements in the page
        :type all_headers: list

        :param all_cards: list of all the cards in the page
        :type all_cards: list

        :returns: a dict that maps the header names/categories to the list of cards in this category
        :rtype: dict

        """
        header_names_to_cards = dict()
        if (all_headers is None) or (all_cards is None):
            return header_names_to_cards
        for header in all_headers:
            y_pos = header.location.get('y')
            header_names_to_cards[header.text] = self.get_cards_for_header(all_cards, y_pos)
        return header_names_to_cards

    def get_cards_for_header(self, all_cards, y_pos_header):
        """
        Gets a list of cards corresponding to a header's y position

        :param all_cards: list of all the cards in the page
        :type all_cards: list

        :param y_pos_header: the y position of the given header to get the cards of
        :type y_pos_header: int

        :returns: a list of cards for the given header's y position
        """
        cards_list = list()
        for card in all_cards:
            y_pos_card = card.location.get('y')
            diff = y_pos_card - y_pos_header
            if 50 <= diff <= 100:
                cards_list.append(card)

        return cards_list

    def get_cards_of(self, category):
        """
        Gets a list of cards corresponding to a category name

        :param category: the category name to get the cards of
        :type category: str

        :returns: a list of cards for the given header's name/category
        """
        return self.header_names_to_cards[category]

    def check_card_click(self, category_name, card_no, report_allure: bool):
        """
        Checks if clicking a card goes to the correct page

        :param category_name: the name of the category to click a card from
        :type category_name: str

        :param card_no: the card number in the given category
        :type card_no: int

        :param report_allure: a boolean that represents whether or not to report the result to allure
        :type report_allure: bool

        :returns: a boolean True if went to the correct page, False otherwise
        :rtype: bool
        """
        cards = None
        card = None
        try:
            cards = self.header_names_to_cards[category_name]
            card = cards[card_no]
        except:
            if report_allure:
                self.report_allure("ERROR: This card number is not available", self.driver)
            return False
        splitted_card_text = card.text.split(" ")
        card_text = splitted_card_text[0] + " " + splitted_card_text[1]
        card.click()
        time.sleep(4)
        playlist_info_name = self.find_element_by_xpath(
            "/html/body/div/div/div/div/div[1]/div/div/div[2]/div/div/section/div/section/div/div/div[1]/div/header/div[1]/div/div[2]/div/div[1]/span")

        if playlist_info_name is None:
            return False

        if playlist_info_name.text != card_text and report_allure:
            self.report_allure(
                "ERROR: Playlist name is not the same as the card name. Card name = " + card_text + ", Playlist name = " + playlist_info_name.text)

        return self.url_has("webplayer/nowplay")

    def check_sign_out(self) -> bool:
        """
        Checks sign out and popup window that appears after the sign out

        :returns: a boolean True if signout is successful and popup appeared, False otherwise
        :rtype: bool
        """
        self.click_logout()
        time.sleep(2)
        self.click_your_library()
        time.sleep(2)
        return self.is_popup_window_visible()

    def click_login(self):
        """
        Clicks the login button
        """
        (self.find_element_by_xpath(
            "/html/body/div[1]/div/div/div/div[1]/div/div/div[2]/div/div/div[1]/div/div/nav/ul[2]/li[2]/button")).click()

    def click_signup(self):
        """
        Clicks the signup button
        """
        (self.find_element_by_xpath(
            "/html/body/div[1]/div/div/div/div[1]/div/div/div[2]/div/div/div[1]/div/div/nav/ul[2]/li[1]/button")).click()
