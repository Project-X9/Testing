import time
from Web_Testing.helperClasses import helper


class AccountOverviewPage:
    spotify_logo = "//img[@src='https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSBmnPgQKW4JLrNcSFhPFCLHz3t8kT1pZl0PVkLYsa8FoScWYda']"
    profile_btn = "//*[@id='root']/div/div/div/div[1]/div/nav/div/ul/li[4]/li/a"
    account_btn = "Account"
    logout_btn = "//*[@id='root']/div/div/div/div[1]/div/nav/div/ul/li[4]/li/div/button[2]"
    download_link_txt = "Download"
    help_link_txt = "Help"
    premium_link_txt = "Premium"
    get_premium_btn = "// *[ @ id = 'root'] / div / div / div / div[2] / div[1] / div / div / div / div[1] / button"
    account_overview_link = "//*[@id='root']/div/div/div/div[2]/div[3]/div/div[1]/div/a[2]"
    edit_profile_link = "//*[@id='root']/div/div/div/div[2]/div[3]/div/div[1]/div/a[3]"
    change_password_link = "//*[@id='root']/div/div/div/div[2]/div[3]/div/div[1]/div/a[4]"
    recover_playlists_link = "//*[@id='root']/div/div/div/div[2]/div[3]/div/div[1]/div/a[5]"
    redeem_link = "//*[@id='root']/div/div/div/div[2]/div[3]/div/div[1]/div/a[6]"
    join_premium_btn = "JOIN PREMIUM"
    edit_profile_btn = "//*[@id='root']/div/div/div/div[2]/div[3]/div/div[2]/div[5]/button"
    sign_out_btn = "//*[@id='root']/div/div/div/div[2]/div[3]/div/div[2]/div[10]/button"

    def __init__(self, driver):
        self.driver = driver
        self.helper = helper()
        self.dob = None
        self.account_overview_elements = None

    def click_spotify_logo(self):
        self.helper.find_element_by_xpath(self.driver, self.spotify_logo).click()

    def click_profile(self):
        self.helper.find_element_by_xpath(self.driver, self.profile_btn).click()

    def click_account(self):
        self.helper.find_element_by_link_text(self.driver, self.account_btn).click()

    def click_logout(self):
        self.helper.find_element_by_xpath(self.driver, self.logout_btn).click()

    def click_download_link(self):
        self.helper.find_element_by_link_text(self.driver, self.download_link_txt).click()

    def click_help_link(self):
        self.helper.find_element_by_link_text(self.driver, self.help_link_txt).click()

    def click_premium_link(self):
        self.helper.find_element_by_link_text(self.driver, self.premium_link_txt).click()

    def click_get_premium_btn(self):
        self.helper.find_element_by_xpath(self.driver, self.get_premium_btn).click()

    def click_account_overview(self):
        self.helper.find_element_by_xpath(self.driver, self.account_overview_link).click()

    def click_edit_profile(self):
        self.helper.find_element_by_xpath(self.driver, self.edit_profile_link).click()

    def click_change_password(self):
        self.helper.find_element_by_xpath(self.driver, self.change_password_link).click()

    def click_recover_playlists(self):
        self.helper.find_element_by_xpath(self.driver, self.recover_playlists_link).click()

    def click_redeem_link(self):
        self.helper.find_element_by_xpath(self.driver, self.redeem_link).click()

    def click_edit_profile_btn(self):
        self.helper.find_element_by_xpath(self.driver, self.edit_profile_btn).click()

    def click_join_premium_btn(self):
        self.helper.find_element_by_link_text(self.driver, self.join_premium_btn).click()

    def click_signout_btn(self):
        self.helper.find_element_by_xpath(self.driver, self.sign_out_btn).click()

    def set_dob(self, dob):
        self.dob = dob

    def initialize_account_overview(self):
        try:
            self.account_overview_elements = self.driver.find_elements_by_class_name("ProfileSection__valueCell--1fz0K")
            return True
        except:
            return False

    def get_account_overview_username(self):
        account_overview_username = self.account_overview_elements[0].text
        return account_overview_username

    def get_account_overview_email(self):
        account_overview_email = self.account_overview_elements[1].text
        return account_overview_email

    def get_account_overview_dob(self):
        account_overview_dob = self.account_overview_elements[2].text.split("/")
        return account_overview_dob

    def is_correct_username(self, username):
        if self.get_account_overview_username() == username:
            return True
        else:
            return False

    def is_correct_email(self, email):
        if self.get_account_overview_email() == email:
            return True
        else:
            return False

    def is_correct_dob(self, dob):
        if dob.is_equal(self.get_account_overview_dob()):
            return True
        else:
            return False

    def check_account_overview_page(self):
        if self.driver.title == "Account overview - Spotify":
            return True
        else:
            return False

    def account_overview_check(self, email, password, dob, username):
        try:
            # if not check_account_overview_page():
            # self.helper.click_button_safe(self.account_overview_btn)

            if self.initialize_account_overview():
                if self.is_correct_email(email) and self.is_correct_dob(dob) and self.is_correct_username(username):
                    return True
                else:
                    if not self.is_correct_email(email):
                        print("wrong email")
                    if not self.is_correct_dob(dob):
                        print("wrong DOB")
                    if not self.is_correct_username(username):
                        print("wrong username")
                    return False
            else:
                print("cant't initialize account overview elements")
                return False
        except:
            exit('Testing failed in account overview with credentials : ' + email + " & " + password)
