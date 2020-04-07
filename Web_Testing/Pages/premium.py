import time
from Web_Testing.helperClasses import WebHelper


class PremiumPage(WebHelper):

    spotify_logo = "//img[@src='https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSBmnPgQKW4JLrNcSFhPFCLHz3t8kT1pZl0PVkLYsa8FoScWYda']"
    logout_button = "//button[text()='LogOut']"
    account_link = "//a[text()='Account']"
    profile_link = "//text()[.='Profile']/ancestor::a[1]"
    download_link = "//a[text()='Download']"
    help_link = "//a[text()='Help']"
    home_link = "//a[text()='Home']"
    get_premium_button = "//button[text()='Get Premium']"

    def __init__(self, driver):
        self.driver = driver

    def click_spotify_logo(self):
        if self.element_exists_by_xpath(self.spotify_logo):
            self.find_element_by_xpath(self.spotify_logo).click()
        else:
            self.report_allure("Not Found")
            assert False

    def click_logout_button(self):
        if self.element_exists_by_xpath(self.spotify_logo):
            self.find_element_by_xpath(self.logout_button).click()
        else:
            self.report_allure("Not Found")
            assert False


    def click_account_link(self):
        if self.element_exists_by_xpath(self.spotify_logo):
            self.find_element_by_xpath(self.account_link).click()
        else:
            self.report_allure("Not Found")
            assert False

    def click_profile_link(self):
        if self.element_exists_by_xpath(self.spotify_logo):
            self.find_element_by_xpath(self.profile_link).click()
        else:
            self.report_allure("Not Found")
            assert False

    def click_download_link(self):
        if self.element_exists_by_xpath(self.spotify_logo):
            self.find_element_by_xpath(self.download_link).click()
        else:
            self.report_allure("Not Found")
            assert False

    def click_help_link(self):
        if self.element_exists_by_xpath(self.spotify_logo):
            self.find_element_by_xpath(self.help_link).click()
        else:
            self.report_allure("Not Found")
            assert False

    def click_home_link(self):
        if self.element_exists_by_xpath(self.spotify_logo):
            self.find_element_by_xpath(self.home_link).click()
        else:
            self.report_allure("Not Found")
            assert False

    def click_get_premium_button(self):
        if self.element_exists_by_xpath(self.spotify_logo):
            self.find_element_by_xpath(self.get_premium_button).click()
        else:
            self.report_allure("Not Found")
            assert False


