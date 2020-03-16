class LoggedOutHome:

    def __init__(self, driver):
        # tb refers to Toolbar, tb_.. refers to Toolbar elements
        self.tb_login_btn = driver.find_element_by_xpath("/html/body/div[2]/div/header/div/nav/ul/li[6]/a")
        self.tb_signup_btn = driver.find_element_by_xpath("/html/body/div[2]/div/header/div/nav/ul/li[5]/a")
        self.tb_download_btn = driver.find_element_by_xpath("/html/body/div[2]/div/header/div/nav/ul/li[3]/a")
        self.tb_help_btn = driver.find_element_by_xpath("/html/body/div[2]/div/header/div/nav/ul/li[2]/a")
        self.tb_premium_btn = driver.find_element_by_xpath("/html/body/div[2]/div/header/div/nav/ul/li[1]/a")
        # self.tb_logo = driver.find_element_by_xpath("/html/body/div[2]/div/header/div/div[1]/a/span/svg/g/path")
        self.getspotify_btn = driver.find_element_by_id("generic-btn-premium")
        self.fb_btn = driver.find_element_by_xpath("/html/body/div[3]/footer/nav/div[3]/ul/li[3]/a/span")
        self.twitter_btn = driver.find_element_by_xpath("/html/body/div[3]/footer/nav/div[3]/ul/li[2]/a/span")
        self.instagram_btn = driver.find_element_by_xpath("/html/body/div[3]/footer/nav/div[3]/ul/li[1]/a/span")
        self.subheading = driver.find_element_by_xpath("//h4[text()='Millions of songs. No credit card needed.']")
        self.heading = driver.find_element_by_xpath("//h1[text()='Music for everyone.']")
        self.for_artists_btn = driver.find_element_by_xpath("//a[text()='For Artists']")

    def getButtons(self):

        btns_arr = [self.tb_download_btn, self.tb_help_btn,
                    self.tb_login_btn,
                    self.tb_signup_btn, self.tb_premium_btn,
                    self.getspotify_btn]
        return btns_arr


