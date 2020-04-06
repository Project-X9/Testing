from Mobile_Testing.helper import Helper


class HomePage:

    logout_button_id = "com.example.projectx:id/logOut_bt"
    playlist_button_id = "com.example.projectx:id/openPlaylist"
    play_music_button_id = "com.example.projectx:id/playMusic"

    def __init__(self, driver):
        self.driver = driver

    def click_logout_button(self):
        Helper.find_element_by_id(self.driver, self.logout_button_id).click()

    def click_playlist_button(self):
        Helper.find_element_by_id(self.driver, self.playlist_button_id).click()

    def click_play_music_button(self):
        Helper.find_element_by_id(self.driver, self.play_music_button_id).click()