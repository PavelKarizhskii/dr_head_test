import datetime
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class Vinyl_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    """Lokators"""

    vinyl_record = '//img[@alt="Виниловые пластинки"]'


    """Getters"""


    def get_vinyl_record(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.vinyl_record)))



    """Actions"""

    def click_vinyl_record(self):
        self.get_vinyl_record().click()
        print("Click to vinyl_record")


    """Metods"""


    def go_vinyl_record(self):
        self.get_current_url()
        self.click_vinyl_record()



