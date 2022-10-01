import datetime
from termcolor import colored


class Base():

    url='https://doctorhead.ru/catalog/personal-audio/'

    def __init__(self, driver):
        self.driver = driver


    """Метод получения текущего url"""

    def get_current_url(self):
        current_url = self.driver.current_url
        print("\nCurrent url: " + current_url)


    """Метод проверки слова на странице"""

    def assert_word(self, word, result):
        assert word == result
        print(colored("Correct value word", 'yellow'))


    """Скрин"""
    def make_screenshot(self):
        self.driver.save_screenshot('/Users/pavelkarizskiy/PycharmProjects/dr_head_test/screen/' + 'screenshot' + str(datetime.datetime.utcnow()) + '.png')

    """Метод проверки url"""

    def assert_url(self, result):
        assert self.driver.current_url == result
        print(colored("Correct value url", 'yellow'))