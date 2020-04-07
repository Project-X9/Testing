import time
from Web_Testing.helperClasses import WebHelper

class PremiumPage(WebHelper):
    """
               A class used to represent Premium Page

               ...

               Attributes
               ----------
               spotify_logo : string
                   A string containing the xpath of spotify's logo
               profile_btn : string
                   A string containing the xpath of Profile button
               account_btn : string
                   A string containing the link text of Account link in profile option list
               logout_btn : string
                   A string containing the xpath of Logout button
               download_link_txt : string
                    A string containing the link text of Download link
               help_link_txt : string
                    A string containing the link text of Help link
               home_link_txt : string
                   A string containing the link text of Premium link
               get_premium_btn_1 : string
                   A string containing the xpath of Get Premium button
               get_premium_btn_2 : string
                   A string containing the xpath of Get Premium button

               Methods
               -------
               click_spotify_logo()
                    Clicks logo of spotify
               click_profile()
                    Clicks Profile button
               click_account()
                    Clicks Account button in profile list
               click_logout()
                    Clicks Logout button in profile list
               click_download_link()
                    Clicks Download button
               click_help_link()
                    Clicks Help button
               click_home_link()
                    Clicks Home button
               click_get_premium_btn_1()
                    Clicks Get Premium top button
               click_get_premium_btn_2()
                    Clicks Get Premium second button
    """

    spotify_logo = "//img[@src='https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSBmnPgQKW4JLrNcSFhPFCLHz3t8kT1pZl0PVkLYsa8FoScWYda']"
    logout_btn = "//*[@id='root']/div/div/div/div[1]/div/nav/div/ul/li[8]/li/div/button[2]/button"
    account_btn = "Account"
    profile_btn = "//*[@id='root']/div/div/div/div[1]/div/nav/div/ul/li[8]/li/a"
    download_link_txt = "Download"
    help_link_txt = "Help"
    home_link_txt = "Home"
    get_premium_button_1 = "//*[@id='root']/div/div/div/div[2]/p/button"
    get_premium_button_2 = "//*[@id='root']/div/div/div/div[3]/p/button"

    def __init__(self, driver):
        """
               Initializes the page elements

               :param driver : the driver to which the super class' driver is to be set
               :type driver: WebDriver
               """
        self.set_driver(driver)

    def click_spotify_logo(self):
        """Clicks Spotify logo"""
        self.click_button_safe(self.find_element_by_xpath(self.spotify_logo))

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

    def click_download_link(self):
        """Clicks Download button"""
        self.click_button_safe(self.find_element_by_link_text(self.download_link_txt))

    def click_help_link(self):
        """Clicks Help button"""
        self.click_button_safe(self.find_element_by_link_text(self.help_link_txt))

    def click_home_link(self):
        """Clicks Home button"""
        self.click_button_safe(self.find_element_by_link_text(self.home_link_txt))

    def click_get_premium_button_1(self):
        """Clicks Get Premium top button """
        self.click_button_safe(self.find_element_by_xpath(self.get_premium_button_1))

    def click_get_premium_button_2(self):
        """Clicks Get Premium second button"""
        self.click_button_safe(self.find_element_by_xpath(self.get_premium_button_2))


