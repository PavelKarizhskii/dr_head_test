import datetime
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from utilites.logger import Logger

"""Страница оформления заказа"""
class Make_order(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    """Lokators"""

    delivery = '//span[contains(text(), "Службы доставки")]'
    address = '//input[@name="ADDRESS"]'
    my_address = '//ymaps[@class="ymaps-2-1-79-search__suggest ymaps-2-1-79-popup ymaps-2-1-79-popup_theme_ffffff ymaps-2-1-79-i-custom-scroll"]'
    flat = '//input[@name="FLAT_NUM"]'
    name = '//input[@class="field field_middle js-mask-name js-order-name"]'
    second_name = '//input[@class="field field_middle js-mask-last_name js-last-name js-order-last_name"]'
    phone = '//input[@class="field field_middle js-order-phone"]'
    mail = '//input[@class="field field_middle js-mask-email js-order-email"]'
    description = '//textarea[@name="USER_DESCRIPTION"]'
    button_no = '//button[text()="Нет"]'



    """Getters"""


    def get_delivery(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.delivery)))

    def get_address(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.address)))

    def get_flat(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.flat)))

    def get_name(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.name)))

    def get_second_name(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.second_name)))

    def get_phone(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.phone)))

    def get_mail(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.mail)))

    def get_description(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.description)))

    def get_my_address(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.my_address)))

    def get_button_no(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.button_no)))

    """Actions"""

    def click_delivery(self):
        self.get_delivery().click()
        print("Click to delivery")

    def input_address(self, test_address):
        self.get_address().send_keys(test_address)
        print("input address")

    def click_my_address(self):
        self.get_delivery().click()
        print("Click to my address")

    def input_flat(self, test_flat):
        self.get_flat().send_keys(test_flat)
        print("Input flat")

    def input_name(self, test_name):
        self.get_name().send_keys(test_name)
        print("Input name")

    def input_second_name(self, test_second_name):
        self.get_second_name().send_keys(test_second_name)
        print("Input second name")

    def input_phone(self, test_phone):
        self.get_phone().send_keys(test_phone)
        print("Input phone")

    def input_mail(self, test_mail):
        self.get_mail().send_keys(test_mail)
        print("Input e-mail")

    def click_button_no(self):
        self.get_button_no().click()
        print("Click to button no")


    def input_description(self, test_description):
        self.get_description().send_keys(test_description)
        print("Input description")



    """Metods"""


    def input_info_order(self):
        Logger.add_start_step(method='input_info_orde')
        self.get_current_url()
        self.driver.execute_script("window.scrollTo(0, 500)")
        self.click_delivery()
        self.input_address(test_address='Беларусь, Минск, улица Ленина, 50')
        self.click_my_address()
        self.input_flat(test_flat="123")
        self.driver.execute_script("window.scrollTo(0, 1600)")
        self.input_name(test_name="Павел")
        self.input_second_name(test_second_name="QA Automation Engineer (Python)")
        self.input_phone(test_phone="+79649863171")
        self.input_mail(test_mail="pavel.karizhsky@yandex.ru")
        self.input_description(test_description="Завершение автотеста по покупке беспроводных наушников Dali IO-4 Iron Black. Спасибо за внимание!")
        try:
            self.click_button_no()
        except Exception:
            pass
        self.assert_url(result='https://doctorhead.ru/personal/order/make/')
        self.make_screenshot()
        Logger.add_end_step(url=self.driver.current_url, method='input_info_order')




