from Mobile_Testing.helper import Helper


class HomePage:

    logout_button_id = "com.example.projectx:id/logOut_bt"
    playlist_button_id = "com.example.projectx:id/openPlaylist"
    play_music_button_id = "com.example.projectx:id/playMusic"

    """
    A class used to represent the Home Page
    ...
    Attributes
    ----------
    logout_button_id : string
        A string containing the id of logout button

    playlist_button_id : string
        A string containing the id of playlist button

    play_music_button_id : string
        A string containing the id of playlist button

    Methods
    -------
    click_logout_button(self)
        Clicks on the logout button

    click_playlist_button()
        Clicks on the logout button

    click_play_music_button()
        Clicks on the play music button
    """
    def __init__(self, driver):
        """
        Initializes the page elements
        :param driver : the driver to which the super class' driver is to be set
        :type driver: WebDriver
        """
        self.driver = driver

    def click_logout_button(self):
        """
        Clicks on the logout button
        """
        Helper.find_element_by_id(self.driver, self.logout_button_id).click()

    def click_playlist_button(self):
        """
        Clicks on the playlist button
        """
        Helper.find_element_by_id(self.driver, self.playlist_button_id).click()

    def click_play_music_button(self):
        """
        Clicks on the play music button
        """
        Helper.find_element_by_id(self.driver, self.play_music_button_id).click()
