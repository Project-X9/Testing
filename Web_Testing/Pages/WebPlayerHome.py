from Web_Testing.Pages.WebPlayerMenu import WebPlayerMenu
from Web_Testing.helperClasses import WebHelper
import time

class WebPlayerHome(WebPlayerMenu):

    def __init__(self, driver):
        super().__init__(driver)
        self.upgrade_link = self.find_element_by_xpath("//a[text()='UPGRADE']")
        self.accountoverviewfooter_div = self.find_element_by_xpath("//div[@class='AccountOverviewFooter']")
        self.spotify_logo = self.find_element_by_xpath(
            "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/nav[1]/div[1]/div[1]/div[1]/ul[1]/li[5]/a[1]")

        self.signup_btn = self.find_element_by_xpath("//a[text()='SIGN UP']")
        self.login_btn = self.find_element_by_xpath("//text()[.='LOG IN']/ancestor::button[1]")
        self.signup_popup_btn = self.find_element_by_xpath("//a[text()='Sign up free']")
        self.login_popup_btn = self.find_element_by_xpath("//a[text()='Log in']")
        self.close_popup_btn = self.find_element_by_xpath("//button[text()='Close']")
        self.popup_window = self.find_element_by_xpath(
            "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]")
        self.all_cards = self.find_elements_by_class_name("CardsHome")
        self.all_headers = self.find_elements_by_class_name("HeaderAboveGrid")
        self.header_names_to_cards = self.map_headers_to_cards(self.all_headers, self.all_cards)


    def is_in_your_library(self) -> bool:
        return self.url_has("/librarypage")

    def is_in_liked_songs(self) -> bool:
        return self.url_has("/likedplay")

    def initialize_popup_window(self):
        self.signup_popup_btn = self.find_element_by_xpath("//a[text()='Sign up free']")
        self.login_popup_btn = self.find_element_by_xpath("//a[text()='Log in']")
        self.close_popup_btn = self.find_element_by_xpath("//button[text()='Close']")
        self.popup_window = self.find_element_by_xpath(
            "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]")

    def is_pop_up_window_visible(self):
        self.initialize_popup_window()
        if (self.login_popup_btn is None) or (self.close_popup_btn is None) or (self.signup_popup_btn is None):
            return False
        else:
            return True

    def map_headers_to_cards(self, all_headers, all_cards):
        header_names_to_cards = dict()
        if (all_headers is None) or (all_cards is None):
            return header_names_to_cards
        for header in all_headers:
            y_pos = header.location.get('y')
            header_names_to_cards[header.text] = self.get_cards_for_header(all_cards, y_pos)
        return header_names_to_cards

    def get_cards_for_header(self, all_cards, y_pos_header):
        cards_list = list()
        for card in all_cards:
            y_pos_card = card.location.get('y')
            diff = y_pos_card - y_pos_header
            if 50 <= diff <= 100:
                cards_list.append(card)

        return cards_list

    def get_cards_of(self, category):
        return self.header_names_to_cards[category]

    def check_card_click(self, category_name, card_no, report_allure: bool):
        cards = self.header_names_to_cards[category_name]
        card = cards[card_no]
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

    def check_sign_out(self) -> bool:
        self.click_logout()
        time.sleep(2)
        self.click_your_library()
        time.sleep(2)
        return self.is_pop_up_window_visible()





