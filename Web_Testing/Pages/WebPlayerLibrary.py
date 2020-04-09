import time

from Web_Testing.Pages.WebPlayerMenu import WebPlayerMenu
from collections import defaultdict

class WebPlayerLibrary(WebPlayerMenu):

    def __init__(self, driver):
        super().__init__(driver)

        self.artists_link = self.find_element_by_xpath("//a[text()='Artists']")
        self.playlists_link = self.find_element_by_xpath("//a[text()='Playlists']")
        self.create_your_first_playlist_heading = self.find_element_by_xpath("//h1[text()='Create your first playlist']")
        self.we_help_you_heading = self.find_element_by_xpath("//h4[text()='Weâ€™ll help you make the perfect mixtape")
        self.create_new_playlist_button = self.find_element_by_xpath("//button[text()='Create new playlist']")
        self.profile_btn = self.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div/div/div[1]/div/nav/div/div/div/ul/ul/li/li/button/a")
        self.logout_btn = self.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div/div/div[1]/div/nav/div/div/div/ul/ul/li/li/div/button[2]/button")
        self.account_btn = self.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div/div/div[1]/div/nav/div/div/div/ul/ul/li/li/div/button[1]/a")
        self.liked_songs = driver.find_element_by_class_name("LikedSongs")
        self.library_cards = driver.find_elements_by_class_name("CardsLibrary")
# TrackListHeader Body

    def click_liked_songs(self):
        self.hover_to_element(self.liked_songs)
        time.sleep(2)
        liked_songs_btn = self.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div[2]/div/div/button")
        if liked_songs_btn is not None:
            liked_songs_btn.click()

    def check_liked_songs_click(self):
        # self.liked_songs.click()
        self.click_liked_songs()
        time.sleep(4)
        return self.url_has("webplayer/likedplay", self.driver)

    def check_card_click(self, card_no, report_allure: bool):
        card = self.library_cards[card_no]
        splitted_card_text = card.text.split(" ")
        card_text = splitted_card_text[0] + " " + splitted_card_text[1]
        card.click()
        time.sleep(4)
        playlist_info_name = self.find_element_by_xpath("/html/body/div/div/div/div/div[1]/div/div/div[2]/div/div/section/div/section/div/div/div[1]/div/header/div[1]/div/div[2]/div/div[1]/span")

        if playlist_info_name is None:
            return False

        if playlist_info_name.text != card_text and report_allure:
            self.report_allure("ERROR: Playlist name is not the same as the card name. Card name = " + card_text + ", Playlist name = " + playlist_info_name.text)

        return self.url_has("webplayer/nowplay")




