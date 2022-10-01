import datetime
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from utilites.logger import Logger

"""Страница козцины"""
class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    """Lokators"""

    make_order = '//a[@href="/personal/order/make/"]'


    """Getters"""


    def get_make_order(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.make_order)))



    """Actions"""

    def click_make_order(self):
        self.get_make_order().click()
        print("Click to make order")


    """Metods"""


    def go_make_order(self):
        Logger.add_start_step(method='go_make_order')
        self.get_current_url()
        self.driver.execute_script("window.scrollTo(0, 500)")
        self.click_make_order()
        Logger.add_end_step(url=self.driver.current_url, method='go_make_order')



