from Pages.status import StatusPage
import time


class LoginPage:
    page_link = "https://accounts.spotify.com/en/login"
    spotify_logo = "//*[@id='app']/body/div[1]/div[1]/div/a"
    connect_with_facebook = "//*[@id='app']/body/div[1]/div[2]/div/div[1]/div/a"
    connect_with_apple = "//*[@id='app']/body/div[1]/div[2]/div/div[2]/div/a"
    email_textbox = "//input[@type='text'][@name='username']"
    password_textbox = "//input[@type='password'][@name='password']"
    remember_checkbox = "//*[@id='app']/body/div[1]/div[2]/div/form/div[3]/div[1]/div/label/span"
    login_button = "//button[text()='Log In']"
    forget_password = "//a[text()='Forgot your password?']"
    signup_button = "//a[text()='Sign up for Spotify']"
    terms_and_conditions_link = "//*[@id='app']/body/div[1]/div[2]/div/div[6]/div/p/a[1]"
    privacy_policy_link = "//*[@id='app']/body/div[1]/div[2]/div/div[6]/div/p/a[2]"
    incorrect_username_password = "//span[text()='Incorrect username or password.']"

    def __init__(self, driver):
        self.driver = driver

    def click_logo(self):
        self.driver.find_element_by_xpath(self.spotify_logo).click()

    def click_connect_with_facebook(self):
        self.driver.find_element_by_xpath(self.connect_with_facebook).click()

    def click_connect_with_apple(self):
        self.driver.find_element_by_xpath(self.connect_with_apple).click()

    def set_email(self, email):
        self.driver.find_element_by_xpath(self.email_textbox).send_keys(email)

    def set_password(self, password):
        self.driver.find_element_by_xpath(self.password_textbox).send_keys(password)

    def clear_page(self):
        self.driver.find_element_by_xpath(self.email_textbox).clear()
        self.driver.find_element_by_xpath(self.password_textbox).clear()


    def click_remember_me(self):
        self.driver.find_element_by_xpath(self.remember_checkbox).click()

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_button).click()

    def click_forget_password(self):
        self.driver.find_element_by_xpath(self.forget_password).click()

    def click_sign_up(self):
        self.driver.find_element_by_xpath(self.signup_button).click()

    def click_terms_conditions(self):
        self.driver.find_element_by_xpath(self.terms_and_conditions_link).click()

    def click_privacy_policy(self):
        self.driver.find_element_by_xpath(self.privacy_policy_link).click()

    def check_login_failure(self):
        if self.driver.find_element_by_xpath(self.incorrect_username_password).text == 'Incorrect username or password.':
            assert True
        else:
            assert False

    def check_login_page(self):
        if self.driver.title == "Login - Spotify":
            assert True
        else:
            assert False

    def login_to_spotify(self, email, password):
        sp = StatusPage(self.driver)
        self.clear_page()
        self.set_email(email)
        self.set_password(password)
        self.click_login()
        time.sleep(2)
        if sp.check_status_page():
            sp.click_web_player_link()
            return True
        else:
            return False
