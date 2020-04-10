from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Web_Testing.Pages.WebPlayerHome import WebPlayerHome
from Web_Testing.Pages.WebPlayerMenu import WebPlayerMenu
from Web_Testing.helperClasses import WebHelper
from Web_Testing.helperClasses import ConstantsClass
from Web_Testing.Pages.LoginPage import LoginPage
from Web_Testing.Pages.SignupPage import SignupPage
from Web_Testing.helperClasses import DOB
from Web_Testing.Pages.AccountOverviewPage import AccountOverviewPage
from Web_Testing.Pages.WebPlayerLibrary import WebPlayerLibrary
from collections import defaultdict
import time


def get_cards_for_header(all_cards: list, y_pos_header):
    cards_list = list()
    for card in all_cards:
        y_pos_card = card.location.get('y')
        diff = y_pos_card - y_pos_header
        if 50 <= diff <= 100:
            cards_list.append(card)

    return cards_list


def map_headers_to_cards(all_headers, all_cards):
    header_names_to_cards = dict()
    if (all_headers is None) or (all_cards is None):
        return header_names_to_cards
    for header in all_headers:
        y_pos = header.location.get('y')
        header_names_to_cards[header.text] = get_cards_for_header(all_cards, y_pos)
    return header_names_to_cards


helper = WebHelper()
driver: webdriver.Firefox = helper.firefox_driver_init()
helper.set_driver(driver)
driver.maximize_window()
time.sleep(3)
driver.get(helper.get_login_url())
time.sleep(3)
lp = LoginPage(driver)
lp.set_credentials("test1@test.com", "test123")
lp.click_login()
time.sleep(5)
driver.get(helper.base_url + "webplayer/home")
time.sleep(5)
# profile_btn = helper.find_element_by_xpath("/html/body/div/div/div/div/div[1]/div/div/div[2]/div/div/div[1]/div/div/nav/ul[2]/li/li/div[1]/button/a")
# profile_btn.click()
# logout_btn_xpath = "/html/body/div/div/div/div/div[1]/div/div/div[2]/div/div/div[1]/div/div/nav/ul[2]/li/li/div[2]/button[3]/button"
# logout_btn_element = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, logout_btn_xpath)))
# logout_btn_element.click()
lib_menu = WebPlayerMenu(driver)
# test_back = helper.find_element_by_xpath("/html/body/div/div/div/div/div[1]/div/div/div[2]/div/div/div[1]/div/div/nav/ul[1]/li[1]/button/a")
# test_back = helper.find_element_by_xpath("/html/body/div/div/div/div/div[1]/div/div/div[2]/div/div/div[1]/div/div/nav/ul[1]/li[2]/button/a")

lib_menu.click_your_library()
time.sleep(2)
lib_menu.click_liked_songs()
time.sleep(2)
songs_no_par = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div/div/div[2]/div/div/section/div/section/div/div/div[1]/div/header/div[2]/div[2]/div/p")
songs_no_arr = songs_no_par.text.split(" ")
print(songs_no_arr[0])

# test_back = helper.find_element_by_xpath("/html/body/div/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div[1]/div/nav/div/div/div/ul/li[1]/button/a")
# test_back.click()

# webplayer = WebPlayerLibrary(driver)
# webplayer.click_liked_songs()
# time.sleep(10)
# liked_songs = helper.find_element_by_class_name("LikedSongs")
# library_cards = helper.find_elements_by_class_name("CardsLibrary")
# library_cards[0].click()
# time.sleep(3)
# elements = driver.find_elements_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/section[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/header[1]/div[2]/div[1]")
# elements = helper.find_elements_by_class_name("textMenuWrapper", driver)
# for e in elements:
#     print(e.text)
#
# te = helper.find_element_by_xpath("/html/body/div/div/div/div/div[1]/div/div/div[2]/div/div/section/div/section/div/div/div[1]/div/header/div[1]/div/div[2]/div/div[1]/span")
# if te is not None:
#     print("teeeee")
#     print(te.text)





# tp = WebPlayerHome(driver)
# p1 = tp.get_playlist_card(1, 1)
# print(p1)
# all_cards = helper.find_elements_by_class_name("CardsHome")
# if all_cards is not None:
#     print(len(all_cards))
#     for card in all_cards:
#         # print(card.text)
#         print(card.location.get('y'))
#
# all_headers = helper.find_elements_by_class_name("HeaderAboveGrid")
# if all_headers is not None:
#     print(len(all_headers))
#     for header in all_headers:
#         print(header.text)
#         print(header.location.get('y'))
#
# # if all_cards is not None:
# #     all_cards[0].click()
# test_map = map_headers_to_cards(all_headers, all_cards)
# for key in test_map.keys():
#     print(test_map.get(key))
