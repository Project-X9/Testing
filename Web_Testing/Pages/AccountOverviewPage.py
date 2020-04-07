from selenium.common.exceptions import NoSuchElementException

from Web_Testing.helperClasses import WebHelper
from Web_Testing.helperClasses import DOB


class AccountOverviewPage(WebHelper):
    """
            A class used to represent Account Overview Page

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
            get_premium_btn : string
                A string containing the link text of Get Premium button
            account_overview_link : string
                A string containing the xpath of Account Overview button
            edit_profile_link : string
                A string containing the xpath of Edit Profile button
            change_password_link : string
                A string containing the xpath of Change Passwword button
            recover_playlists_link : string
                A string containing the xpath of Recover Playlist button
            redeem_link : string
                A string containing the xpath of Redeem button
            join_premium_btn : string
                A string containing the link text of Join Premium button
            edit_profile_btn : string
                A string containing the link text of Edit Profile button
            sign_out_btn : string
                A string containing the link text of Sign Out button
            username_txt_xpath : string
                A string containing the xpath of Username text
            email_txt_xpath : string
                A string containing the xpath of Email text
            age_txt_xpath : string
                A string containing the xpath of Age text
            username : string
                A string containing username of the user
            email : sting
                A string containing email of the user
            age : string
                A string containing age of the user

            Methods
            -------
            initialize_account_overview_elements()
                Initialize username, email and age with the information in the account overview page
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
            click_get_premium_btn()
                Clicks Get Premium button
            click_account_overview()
                Clicks Account Overview button
            click_edit_profile()
                Clicks Edit Profile link
            click_change_password()
                Clicks Change Password button
            click_recover_playlists()
                Clicks recover Playlists button
            click_redeem_link()
                Clicks Redeem button
            click_edit_profile_btn()
                Clicks Edit Profile button
            click_join_premium_btn()
                Clicks Join Premium button
            click_signout_btn()
                Clicks Sign Out button
            get_account_overview_username()
                get username
            get_account_overview_email()
                get email
            get_account_overview_age()
                get age
            is_correct_username(username)
                Checks if username is same as username given
            is_correct_email(email)
                Checks if email is same as email given
            is_correct_age(age)
                Checks if age is same as age given
            is_page_initialized()
                Checks if currently on Account Overview page
            is_in_account_overview()
                Checks if currently on Account Overview page
            account_overview_check(email, age, username)
                Checks if information on Account Overview page is correct
    """
    spotify_logo = "//*[@id='root']/div/div/div/div[1]/div/nav/a/img"
    profile_btn = "//*[@id='root']/div/div/div/div[1]/div/nav/div/ul/li[8]/li/a"
    account_btn = "Account"
    logout_btn = "//*[@id='root']/div/div/div/div[1]/div/nav/div/ul/li[8]/li/div/button[2]/button"
    download_link_txt = "Download"
    help_link_txt = "Help"
    premium_link_txt = "Premium"
    get_premium_btn = "GET PREMIUM"
    account_overview_link = "//*[@id='root']/div/div/div/div[2]/div[2]/div/div[1]/div/a[2]"
    edit_profile_link = "//*[@id='root']/div/div/div/div[2]/div[2]/div/div[1]/div/a[3]"
    change_password_link = "//*[@id='root']/div/div/div/div[2]/div[2]/div/div[1]/div/a[4]"
    recover_playlists_link = "//*[@id='root']/div/div/div/div[2]/div[2]/div/div[1]/div/a[5]"
    redeem_link = "//*[@id='root']/div/div/div/div[2]/div[2]/div/div[1]/div/a[6]"
    join_premium_btn = "JOIN PREMIUM"
    edit_profile_btn = "EDIT PROFILE"
    sign_out_btn = "SIGN OUT"
    username_txt_xpath = "//*[@id='root']/div/div/div/div[2]/div[2]/div/div[2]/div/div[3]/div/div[1]/div[2]"
    email_txt_xpath = "//*[@id='root']/div/div/div/div[2]/div[2]/div/div[2]/div/div[3]/div/div[2]/div[2]"
    age_txt_xpath = "//*[@id='root']/div/div/div/div[2]/div[2]/div/div[2]/div/div[3]/div/div[3]/div[2]"

    def __init__(self, driver):
        """
        Initializes the page elements

        :param driver : the driver to which the super class' driver is to be set
        :type driver: WebDriver
        """
        self.set_driver(driver)
        self.username = ""
        self.email = ""
        self.age = ""

    def initialize_account_overview_elements(self):
        """Initialize username, email and age with the information in the account overview page """
        username_txt = self.find_elements_by_xpath(self.username_txt_xpath)
        email_txt = self.find_elements_by_xpath(self.email_txt_xpath)
        age_txt = self.find_elements_by_xpath(self.age_txt_xpath)
        if (username_txt is not None) and (len(username_txt) > 0):
            self.username = username_txt[0].text

        if (email_txt is not None) and (len(email_txt) > 0):
            self.email = email_txt[0].text

        if (age_txt is not None) and (len(age_txt) > 0):
            self.age = age_txt[0].text

    def click_spotify_logo(self):
        """Clicks logo of spotify"""
        self.click_button_safe(self.find_element_by_xpath(self.spotify_logo))

    def click_profile(self):
        """Clicks Profile button"""
        self.click_button_safe(self.find_element_by_xpath(self.profile_btn))

    def click_account(self):
        """Clicks Account button in profile list"""
        self.click_profile()
        self.click_button_safe(self.find_element_by_link_text(self.account_btn))

    def click_logout(self):
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
        """Clicks Premium button"""
        self.click_button_safe(self.find_element_by_link_text(self.premium_link_txt))

    def click_get_premium_btn(self):
        """Clicks Get Premium button"""
        self.click_button_safe(self.find_element_by_link_text(self.get_premium_btn))

    def click_account_overview(self):
        """Clicks Account Overview button"""
        self.click_button_safe(self.find_element_by_xpath(self.account_overview_link))

    def click_edit_profile(self):
        """Clicks Edit Profile link"""
        self.click_button_safe(self.find_element_by_xpath(self.edit_profile_link))

    def click_change_password(self):
        """Clicks Change Password button"""
        self.click_button_safe(self.find_element_by_xpath(self.change_password_link))

    def click_recover_playlists(self):
        """Clicks Recover Playlists button"""
        self.click_button_safe(self.find_element_by_xpath(self.recover_playlists_link))

    def click_redeem_link(self):
        """Clicks Redeem button"""
        self.click_button_safe(self.find_element_by_xpath(self.redeem_link))

    def click_edit_profile_btn(self):
        """Clicks Edit Profile button"""
        self.click_button_safe(self.find_element_by_link_text(self.edit_profile_btn))

    def click_join_premium_btn(self):
        """Clicks Join Premium button"""
        self.click_button_safe(self.find_element_by_link_text(self.join_premium_btn))

    def click_signout_btn(self):
        """Clicks Sign Out button"""
        self.click_button_safe(self.find_element_by_link_text(self.sign_out_btn))

    def get_account_overview_username(self):
        """
        get username

        :return: username in the account overview page
        :rtype: str
        """
        return self.username

    def get_account_overview_email(self):
        """
        get email

        :return: email in the account overview page
        :rtype: str
        """
        return self.email

    def get_account_overview_age(self):
        """
        get age

        :return: age in the account overview page
        :rtype: str
        """
        return self.age

    def is_correct_username(self, username):
        """
        Checks if username is same as username given

        :param username : the username to be compared
        :type username: str

        :return: a boolean True if username in the account overview page is equal given username
        :rtype: bool
        """
        if self.get_account_overview_username() == username:
            return True
        else:
            return False

    def is_correct_email(self, email):
        """
        Checks if email is same as email given

        :param email : the email to be compared
        :type email: str

        :return: a boolean True if email in the account overview page is equal given email
        :rtype: bool
        """
        if self.get_account_overview_email() == email:
            return True
        else:
            return False

    def is_correct_age(self, age):
        """
        Checks if age is same as age given

        :param age : the age to be compared
        :type age: str

        :return: a boolean True if age in the account overview page is equal given age
        :rtype: bool
        """
        if self.get_account_overview_age() == age:
            return True
        else:
            return False

    def is_page_initialized(self):
        """
        Checks if currently on Account Overview page

        :return: a boolean if currently in account overview
        :rtype: bool
        """
        return self.get_account_overview_email() is not None

    def account_overview_check(self, email, age, username):
        """
        Checks if information on Account Overview page is correct

        :param email : The email used for login
        :type email: str

        :param age : age of the login user
        :type age: str

        :param username : The username of the login user
        :type username: str

        :returns: a boolean True if the information in account overview page is correct
        :rtype: bool

        :raises NoSuchElementException : If a Web Driver element cannot be found in the page
        """
        try:
            self.initialize_account_overview_elements()
            # if open account overview page successfully
            if self.is_page_initialized():
                # if all information is correct
                if self.is_correct_email(email) and self.is_correct_age(age) and self.is_correct_username(username):
                    return True
                # if all or some information is wrong
                else:
                    # if email is not the same as given mail
                    if not self.is_correct_email(email):
                        print("wrong email")
                    # if age is not the same as given age
                    if not self.is_correct_age(age):
                        print("wrong age "+age+" account "+self.age)
                    # if username is not the same as given username
                    if not self.is_correct_username(username):
                        print("wrong username")
                    return False
            # if can't open account overview page
            else:
                print("cant't initialize account overview elements")
                return False

        # any other error that cause test to fail
        except:
            exit('Testing failed in account overview with credentials : ' + email)
