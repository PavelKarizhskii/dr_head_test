import time
from selenium import webdriver

from pages.cart_page import Cart_page
from pages.headphones import Headphones_page
from pages.make_order import Make_order
from pages.personal_audio import Personal_audio_page



"""Тест по выбору и покупке лучших беспроводных наушников"""
def test_road_to_dream(set_up):
    driver = webdriver.Chrome(executable_path='/Users/pavelkarizskiy/PycharmProjects/dr_head_test/driver/chromedriver')
    print("start test road to dream")
    pap=Personal_audio_page(driver)
    pap.go_to_headphones()
    hp=Headphones_page(driver)
    hp.go_cart_with_new_headphones()
    cp=Cart_page(driver)
    cp.go_make_order()
    mp=Make_order(driver)
    mp.input_info_order()
    time.sleep(5)