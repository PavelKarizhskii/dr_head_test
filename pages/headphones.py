import datetime
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from utilites.logger import Logger

"""Страница наушники"""
class Headphones_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    """Lokators"""

    more_brands = '//span[@class="more-brands"]'
    brand_beyerdynamic = '//span[@data-role="count_brend-beyerdynamic"]'
    wireless = '//*[@id="filter-section_2763"]/div[1]/div[2]/div/div/div/label[1]/span[2]/span[1]'
    big_headphones = '//*[@id="filter-section_2761"]/div[1]/div[2]/div/div/div/label[3]/span[2]/span[1]'
    byu_beyerdynamic_amiron_wireless = '//*[@id="catalog-list"]/div[1]/div[4]/button[2]'
    go_to_cart = '//button[@class="button button_primary js-cart-btn"]'


    """Getters"""


    def get_more_brands(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.more_brands)))

    def get_brand_beyerdynamic(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.brand_beyerdynamic)))

    def get_wireless(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.wireless)))

    def get_big_headphones(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.big_headphones)))

    def get_byu_beyerdynamic_amiron_wireless(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.byu_beyerdynamic_amiron_wireless)))

    def get_go_to_cart(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.go_to_cart)))


    """Actions"""

    def click_more_brands(self):
        self.get_more_brands().click()
        print("Click to more brands")

    def click_brand_beyerdynamic(self):
        self.get_brand_beyerdynamic().click()
        print("Click to brend beyerdynamic")

    def click_wireless(self):
        self.get_wireless().click()
        print("Click to wirelessc")

    def click_big_headphones(self):
        self.get_big_headphones().click()
        print("Click to big headphones")


    def click_byu_beyerdynamic_amiron_wireless(self):
        self.get_byu_beyerdynamic_amiron_wireless().click()
        print("Click to byu beyerdynamic amiron wireless")

    def click_go_to_cart(self):
        self.get_go_to_cart().click()
        print("Click to go to cart")


    def go_cart_with_beyerdynamic_amiron_wireless(self):
        Logger.add_start_step(method='go_cart_with_beyerdynamic_amiron_wireles')
        self.get_current_url()
        self.driver.execute_script("window.scrollTo(0, 1100)")
        self.click_more_brands()
        self.driver.execute_script("window.scrollTo(0, 1400)")
        self.click_brand_beyerdynamic()
        self.driver.execute_script("window.scrollTo(0, 4400)")
        self.click_wireless()
        self.click_big_headphones()
        self.driver.execute_script("window.scrollTo(0, 500)")
        time.sleep(3)
        self.click_byu_beyerdynamic_amiron_wireless()
        self.click_go_to_cart()
        Logger.add_end_step(url=self.driver.current_url, method='go_cart_with_beyerdynamic_amiron_wireles')




