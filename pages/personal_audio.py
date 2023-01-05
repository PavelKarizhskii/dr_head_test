import datetime
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from utilites.logger import Logger

"""Страница Персональное аудио"""
class Personal_audio_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    """Lokators"""


    close_city = '//div[@class="modal-close js-location-question-close"]'
    headphones = '//img[@alt="Наушники"]'
    vinyl = '/html/body/div[1]/header/div[3]/div/div[6]/a'



    """Getters"""

    def get_headphones(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.headphones)))


    def get_close_city(self):
        return self.driver.find_element(By.XPATH, self.close_city)

    def get_vinyl(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.vinyl)))


    """Actions"""


    def click_headphones(self):
        self.get_headphones().click()
        print("Click to headphones")

    def click_close_city(self):
        time.sleep(0.5)
        self.get_close_city().click()
        print("Click to close city")

    def click_vinyl(self):
        self.get_vinyl().click()
        print("Click to vinyl")

    def go_to_headphones(self):
        Logger.add_start_step(method='go_to_headphones')
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        try:
            self.click_close_city()
        except Exception:
            pass
        self.click_headphones()
        Logger.add_end_step(url=self.driver.current_url, method='go_to_headphones')


    def go_to_vinyl(self):
        Logger.add_start_step(method='go_to_vinyl')
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_close_city()
        self.click_vinyl()
        Logger.add_end_step(url=self.driver.current_url, method='go_to_vinyl')
