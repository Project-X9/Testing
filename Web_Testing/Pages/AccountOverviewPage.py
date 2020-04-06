from Web_Testing.helperClasses import WebHelper

class AccountOverviewPage(WebHelper):
    spotify_logo = "//*[@id='root']/div/div/div/div[1]/div/nav/a/img"
    profile_btn = "//*[@id='root']/div/div/div/div[1]/div/nav/div/ul/li[8]/li/a"
    account_btn = "Account"
    logout_btn = "//*[@id='root']/div/div/div/div[1]/div/nav/div/ul/li[8]/li/div/button[2]/button"
    download_link_txt = "Download"
    help_link_txt = "Help"
    premium_link_txt = "Premium"
    account_overview_link = "//*[@id='root']/div/div/div/div[2]/div/div/div[1]/div/a[2]"
    edit_profile_link = "//*[@id='root']/div/div/div/div[2]/div/div/div[1]/div/a[3]"
    change_password_link = "//*[@id='root']/div/div/div/div[2]/div/div/div[1]/div/a[4]"
    recover_playlists_link = "//*[@id='root']/div/div/div/div[2]/div/div/div[1]/div/a[5]"
    redeem_link = "// *[ @ id = 'root']/div/div/div/div[2]/div/div/div[1]/div/a[6]"
    join_premium_btn = "JOIN PREMIUM"
    edit_profile_btn = "EDIT PROFILE"
    sign_out_btn = "SIGN OUT"

    def __init__(self, driver):
        self.set_driver(driver)
        usernames = self.find_elements_by_xpath(
            "/html/body/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/div[3]/div/div[1]/div[2]")
        emails = self.find_elements_by_xpath(
            "/html/body/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/div[3]/div/div[2]/div[2]")
        if (usernames is not None) and (len(usernames) > 0):
            self.username = usernames[0].text
        if (emails is not None) and (len(emails) > 0):
            self.email = emails[0].text
        # self.account_overview_email = ""
        # self.account_overview_username = ""
        # self.account_overview_dob = ""

    def click_spotify_logo(self):
        self.click_button_safe(self.find_element_by_xpath(self.spotify_logo))

    def click_profile(self):
        self.click_button_safe(self.find_element_by_xpath(self.profile_btn))

    def click_account(self):
        self.click_profile()
        self.click_button_safe(self.find_element_by_link_text(self.account_btn))

    def click_logout(self):
        self.click_profile()
        self.click_button_safe(self.find_element_by_xpath(self.logout_btn))

    def click_download_link(self):
        self.click_button_safe(self.find_element_by_link_text(self.download_link_txt))

    def click_help_link(self):
        self.click_button_safe(self.find_element_by_link_text(self.help_link_txt))

    def click_premium_link(self):
        self.click_button_safe(self.find_element_by_link_text(self.premium_link_txt))

    def click_account_overview(self):
        self.click_button_safe(self.find_element_by_xpath(self.account_overview_link))

    def click_edit_profile(self):
        self.click_button_safe(self.find_element_by_xpath(self.edit_profile_link))

    def click_change_password(self):
        self.click_button_safe(self.find_element_by_xpath(self.change_password_link))

    def click_recover_playlists(self):
        self.click_button_safe(self.find_element_by_xpath(self.recover_playlists_link))

    def click_redeem_link(self):
        self.click_button_safe(self.find_element_by_xpath(self.redeem_link))

    def click_edit_profile_btn(self):
        self.click_button_safe(self.find_element_by_link_text(self.edit_profile_btn))

    def click_join_premium_btn(self):
        self.click_button_safe(self.find_element_by_link_text(self.join_premium_btn))

    def click_signout_btn(self):
        self.click_button_safe(self.find_element_by_link_text(self.sign_out_btn))

    def initialize_account_overview(self):
        try:
            username = self.find_elements_by_xpath(
                "/html/body/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/div[3]/div/div[1]/div[2]")
            email = self.find_elements_by_xpath(
                "/html/body/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/div[3]/div/div[2]/div[2]")
            dob = self.find_elements_by_xpath(
                "/html/body/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/div[3]/div/div[2]/div[2]")
            country = self.find_elements_by_xpath(
                "//*[@id='root']/div/div/div/div[2]/div/div/div[2]/div/div[4]/div[2]/h5")
            if username is not None:
                self.account_overview_username = username.text
            if email is not None:
                self.account_overview_email = email.text
            if dob is not None:
                self.account_overview_dob = dob.text.split("/")
            return True
        except NoSuchElementException:
            return False

    def get_account_overview_username(self):
        return self.account_overview_username

    def get_account_overview_email(self):
        return self.account_overview_email

    def get_account_overview_dob(self):
        return self.account_overview_dob

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

    def account_overview_check(self, email, password, dob, username):
        try:
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