import time
from Web_Testing.helperClasses import WebHelper

from Web_Testing.Pages import AccountOverviewPage


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
               premium_link_txt : string
                   A string containing the link text of Premium link
               get_premium_btn_1 : string
                   A string containing the xpath of Get Premium button
               get_premium_btn_2 : string
                   A string containing the xpath of Get Premium button
               claim_btn : string
                   A string containing the xpath of Claim button in pop up window
               claim_btn : string
                   A string containing the xpath of Cancel Premium button in pop up window

               Methods
               -------
               check_claim_btn_visible()
                    check visibility of claim button
               check_cancel_premium_btn_visible()
                    check visibility of cancel premium button
               click_claim()
                     Clicks Claim button
               click_cancel_premium()
                     Clicks Cancel Premium button
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
               click_premium_link()
                    Clicks Premium button
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
    premium_link_txt = "Premium"
    get_premium_button_1 = "//*[@id='root']/div/div/div/div[2]/p/button"
    get_premium_button_2 = "//*[@id='root']/div/div/div/div[3]/p/button"
    claim_btn = "/html/body/div[2]/div/div[1]/div/div/div/div[3]/button[1]"
    cancel_premium_btn = "/html/body/div[2]/div/div[1]/div/div/div/div[3]/button[2]"

    def __init__(self, driver):
        """
               Initializes the page elements

               :param driver : the driver to which the super class' driver is to be set
               :type driver: WebDriver
               """
        self.set_driver(driver)

    def check_claim_btn_visible(self):
        """
        check visibility of claim button

        :return:True if claim button is visible
        :type: bool
        """
        if self.find_element_by_xpath(self.claim_btn).isDisplayed():
            return True
        else:
            return False

    def check_cancel_premium_btn_visible(self):
        """
                check visibility of cancel premium button

                :return:True if cancel premium button is visible
                :type: bool
        """
        if self.find_element_by_xpath(self.cancel_premium_btn).isDisplayed():
            return True
        else:
            return False

    def click_claim(self, alert):
        """Clicks Claim button"""
        if self.check_claim_premium():
            alert.click_button_safe(alert.find_element_by_xpath(self.claim_btn))

    def click_cancel_premium(self):
        """Clicks Cancel Premium button"""
        if self.check_cancel_premium_btn_visible():
            self.click_button_safe(self.find_element_by_xpath(self.cancel_premium_btn))

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

    def click_premium_link(self):
        """Clicks Home button"""
        self.click_button_safe(self.find_element_by_link_text(self.premium_link_txt))

    def click_get_premium_button_1(self):
        """Clicks Get Premium top button """
        self.click_button_safe(self.find_element_by_xpath(self.get_premium_button_1))

    def click_get_premium_button_2(self):
        """Clicks Get Premium second button"""
        self.click_button_safe(self.find_element_by_xpath(self.get_premium_button_2))

    def check_claim_premium(self):
        try:
            self.click_get_premium_button_1()
            alert = self.driver.switch_to.alert
            self.check_claim_premium(alert)
            time.sleep(4)
            acc = AccountOverviewPage(self.driver)
            self.driver.get(WebHelper().get_account_overview_url())
            if acc.premium_check(True):
                return True
            else:
                return False
        except:
            exit('Testing failed to make claim premium')
