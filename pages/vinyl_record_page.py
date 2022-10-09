
import datetime
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from utilites.logger import Logger

"""Страница Виниловые пластинки"""
class Vinyl_record_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    """Lokators"""

    executor = '//input[@name="2562936554"]'
    executor_nautilus = '//*[@id="filter-section_2702"]/div[1]/div[2]/div/div/div/label[1022]/span[2]/span[1]'
    vinyl_prince_of_silence = '//img[@title="Фото - Nautilus Pompilius - Князь Тишины"]'
    album_name_locator = '//h1[@data-element-id="88752"]'


    """Getters"""


    def get_executor(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.executor)))

    def get_executor_nautilus(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, '//span[contains(text(), "Наутилус Помпилиус")]')))


    def get_vinyl_prince_of_silence(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.vinyl_prince_of_silence)))

    def get_album_name(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.album_name_locator))).text

    """Actions"""

    def input_executor(self, test_executor):
        self.get_executor().send_keys(test_executor)
        print("Input executor")

    def click_executor_nautilus(selfs):
        selfs.get_executor_nautilus().click()
        print("Click executor nautilus")


    def click_vinyl_prince_of_silence(selfs):
        selfs.get_vinyl_prince_of_silence().click()
        print("Click vinyl prince of silence")




    """Metods"""


    def select_prince_of_silence(self):
        Logger.add_start_step(method='select_prince_of_silence')
        self.get_current_url()
        self.input_executor(test_executor="Наутилус")
        self.click_executor_nautilus()
        self.driver.execute_script("window.scrollTo(0, 400)")
        self.click_vinyl_prince_of_silence()
        self.assert_word(word=self.get_album_name(), result='Nautilus Pompilius - Князь Тишины')
        Logger.add_end_step(url=self.driver.current_url, method='select_prince_of_silence')




