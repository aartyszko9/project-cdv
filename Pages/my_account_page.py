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
