class StatusPage:
    spotify_logo = ("//a[@title='Spotify']")
    account_overview_link = ("//a[text()='Account Overview']")
    web_player_link = ("//*[@id='app']/body/div/div[2]/div/div/div[4]/div/a")
    log_out_button = ("//button[text()='Log Out']")


    def __init__(self, driver):
        self.driver = driver

    def click_logo(self):
        self.driver.find_element_by_xpath(self.spotify_logo).click()

    def click_account_overview_link(self):
        self.driver.find_element_by_xpath(self.account_overview_link).click()

    def click_web_player_link(self):
        self.driver.find_element_by_xpath(self.web_player_link).click()

    def click_log_out_button(self):
        self.driver.find_element_by_xpath(self.log_out_button).click()

    def check_status_page(self):
        if self.driver.title == "Status - Spotify":
            return True
        else:
            return False
