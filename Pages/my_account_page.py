from selenium.common.exceptions import NoSuchElementException
from locators import MyAccountLocators
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
from Pages import authentication_page

class MyAccountPage():

    def expectMyAccountTitle(self):
        try:
            el = self.driver.find_element(*MyAccountLocators.TITLE)
            el.text == "MY ACCOUNT"
        except NoSuchElementException:
            print('El TITLE not found')

    def expectWelcomeText(self):
        try:
            el = self.driver.find_element(*MyAccountLocators.WELCOME_TEXT)
            el.text == "Welcome to your account. Here you can manage all of your personal information and orders."
        except NoSuchElementException:
            print('WELCOME_TEXT not found')
