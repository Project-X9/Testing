import time
from Web_Testing.helperClasses import helper


class PremiumPage:

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
        self.helper = helper()

    def click_spotify_logo(self):
        if helper().element_exists_by_xpath(self.driver, self.spotify_logo):
            helper().find_element_by_xpath(self.driver, self.spotify_logo).click()
        else:
            helper().report_allure(self.driver, "Not Found")
            assert False

    def click_logout_button(self):
        if helper().element_exists_by_xpath(self.driver, self.spotify_logo):
            helper().find_element_by_xpath(self.driver, self.logout_button).click()
        else:
            helper().report_allure(self.driver, "Not Found")
            assert False


    def click_account_link(self):
        if helper().element_exists_by_xpath(self.driver, self.spotify_logo):
            helper().find_element_by_xpath(self.driver, self.account_link).click()
        else:
            helper().report_allure(self.driver, "Not Found")
            assert False

    def click_profile_link(self):
        if helper().element_exists_by_xpath(self.driver, self.spotify_logo):
            helper().find_element_by_xpath(self.driver, self.profile_link).click()
        else:
            helper().report_allure(self.driver, "Not Found")
            assert False

    def click_download_link(self):
        if helper().element_exists_by_xpath(self.driver, self.spotify_logo):
            helper().find_element_by_xpath(self.driver, self.download_link).click()
        else:
            helper().report_allure(self.driver, "Not Found")
            assert False

    def click_help_link(self):
        if helper().element_exists_by_xpath(self.driver, self.spotify_logo):
            helper().find_element_by_xpath(self.driver, self.help_link).click()
        else:
            helper().report_allure(self.driver, "Not Found")
            assert False

    def click_home_link(self):
        if helper().element_exists_by_xpath(self.driver, self.spotify_logo):
            helper().find_element_by_xpath(self.driver, self.home_link).click()
        else:
            helper().report_allure(self.driver, "Not Found")
            assert False

    def click_get_premium_button(self):
        if helper().element_exists_by_xpath(self.driver, self.spotify_logo):
            helper().find_element_by_xpath(self.driver, self.get_premium_button).click()
        else:
            helper().report_allure(self.driver, "Not Found")
            assert False


