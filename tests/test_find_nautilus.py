import time
from selenium import webdriver

from pages.cart_page import Cart_page
from pages.headphones import Headphones_page
from pages.make_order import Make_order
from pages.personal_audio import Personal_audio_page
from pages.vinyl_page import Vinyl_page
from pages.vinyl_record_page import Vinyl_record_page

"""Тест по поиску пластинки Князь тишины группы Наутилус"""
def test_find_nautilus(set_up):
    driver = webdriver.Chrome(executable_path='/Users/pavelkarizskiy/PycharmProjects/dr_head_test/driver/chromedriver')
    print("start test find nautilus")
    pap = Personal_audio_page(driver)
    pap.go_to_vinyl()
    vp = Vinyl_page(driver)
    vp.go_vinyl_record()
    vrp=Vinyl_record_page(driver)
    vrp.select_prince_of_silence()
    time.sleep(5)
