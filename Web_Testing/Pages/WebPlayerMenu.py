from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Web_Testing.helperClasses import WebHelper
from selenium.webdriver.support import expected_conditions as EC


class WebPlayerMenu(WebHelper):
    """
    A class used to represent the Web Player Menu
    ...

    Attributes
    ----------
    home_xpath : str
         a string representing the home button xpath
    search_xpath : str
        a string representing the search button xpath
    your_library_xpath : str
        a string representing Your Library button xpath
    liked_songs_xpath : str
        a string representing the Liked Songs button xpath
    create_playlist_xpath : str
        a string representing the Create Playlist button xpath
    profile_menu_xpath : str
        a string representing the Profile dropdown button xpath
    logout_btn_xpath : str
        a string representing the logout button xpath
    account_btn_xpath : str
        a string representing the account button xpath
    home_link : WebDriverElement
        a Web Driver element representing the home button
    your_library_button : WebDriverElement
        a Web Driver element representing Your Library button
    liked_songs_link : WebDriverElement
        a Web Driver element representing the Liked Songs button
    profile_btn : WebDriverElement
        a Web Driver element representing the Profile button


    Methods
    -------
    click_logout()
        Clicks Logout button in profile list
    click_your_library()
        Clicks Your Library button in web player menu
    click_account()
        Clicks Account button in profile list
    click_liked_songs()
        Clicks Liked Songs button in web player menu
    click_search()
        Clicks Search button in web player menu
    click_create_playlist()
        Clicks Create playlist button in web player menu
    click_home()
        Clicks Home button in web player menu

    """

    home_xpath = "/html/body/div/div/div/div/div[1]/div/div/div[1]/div/a[2]"
    search_xpath = "/html/body/div/div/div/div/div[1]/div/div/div[1]/div/a[3]"
    your_library_xpath = "/html/body/div/div/div/div/div[1]/div/div/div[1]/div/button"
    liked_songs_xpath = "/html/body/div/div/div/div/div[1]/div/div/div[1]/div/div/a[2]"
    create_playlist_xpath = "/html/body/div/div/div/div/div[1]/div/div/div[1]/div/div/a[1]"
    profile_menu_xpath = "/html/body/div/div/div/div/div[1]/div/div/div[2]/div/div/div[1]/div/div/nav/ul[2]/li/li/div[1]/button/a"
    logout_btn_xpath = "/html/body/div/div/div/div/div[1]/div/div/div[2]/div/div/div[1]/div/div/nav/ul[2]/li/li/div[2]/button[3]/button"
    account_btn_xpath = "/html/body/div/div/div/div/div[1]/div/div/div[2]/div/div/div[1]/div/div/nav/ul[2]/li/li/div[2]/button[1]/a"

    def __init__(self, driver):
        """
        Initializes the page elements

        :param driver : the driver to which the super class' driver is to be set
        :type driver: WebDriver
        """
        super().__init__()
        self.set_driver(driver)
        self.home_link = self.find_element_by_xpath(self.home_xpath)
        self.your_library_button = self.find_element_by_xpath(self.your_library_xpath)
        self.liked_songs_link = self.find_element_by_xpath(self.liked_songs_xpath)
        self.profile_btn = self.find_element_by_xpath(self.profile_menu_xpath)

    def click_logout(self):
        """
        Clicks Logout button in profile list
        """
        self.find_element_by_xpath(self.profile_menu_xpath).click()
        logout_btn_element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.logout_btn_xpath)))
        logout_btn_element.click()

    def click_your_library(self):
        """
        Clicks Your Library button in web player menu
        """
        (self.find_element_by_xpath("/html/body/div/div/div/div/div[1]/div/div/div[1]/div/button")).click()

    def click_account(self):
        """
        Clicks Account button in profile list
        """
        self.find_element_by_xpath(self.profile_menu_xpath).click()
        element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.account_btn_xpath)))
        did_scroll = element.location_once_scrolled_into_view
        element.click()

    def click_liked_songs(self):
        """
        Clicks Liked Songs button in web player menu
        """
        self.find_element_by_xpath(self.liked_songs_xpath).click()

    def click_search(self):
        """
        Clicks Search button in web player menu
        """
        self.find_element_by_xpath(self.search_xpath).click()

    def click_create_playlist(self):
        """
        Clicks Create playlist button in web player menu
        """
        self.find_element_by_xpath(self.create_playlist_xpath).click()

    def click_home(self):
        """
        Clicks Home button in web player menu
        """
        self.find_element_by_xpath(self.home_xpath).click()
