import time

from Web_Testing.helperClasses import WebHelper


class AlbumPage(WebHelper):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver


    def add_album_to_library(self):
        menu_btn = self.find_elements_by_xpath("//div[@class='spoticon-ellipsis-32']")
        self.hover_to_element(menu_btn[0])
        menu_btn[0].click()
        time.sleep(2)
        save_to_library_btn = self.find_element_by_xpath("//span[text()='Save to Your Library']")
        save_to_library_btn.click()
        time.sleep(3)

    def remove_album_from_library(self):
        menu_btn = self.find_element_by_xpath("//div[@class='spoticon-ellipsis-32']")
        self.hover_to_element(menu_btn)
        menu_btn.click()
        time.sleep(2)
        save_to_library_btn = self.find_element_by_xpath("//span[text()='Remove from Your Library']	")
        save_to_library_btn.click()
        time.sleep(3)

    def assert_albums_has(self, name: str):
        cards = self.find_elements_by_xpath("/html[1]/body[1]/div[4]/div[1]/div[2]/div[4]/div[1]/div[1]/div[2]/section[1]/div[1]")
        if cards is None or len(cards) == 0:
            return False
        for card in cards:
            cards_splitted = card.text.split("\n")
            card_text = cards_splitted[0]
            if card_text.lower() == name.lower():
                return True

        return False

