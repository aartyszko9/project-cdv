from selenium.common.exceptions import NoSuchElementException
from locators import AuthenticationPageLocators
from helpers import Helpers


email = 'aartyszko+' + Helpers.randomString(5) + '@gmail.com'

class AuthenticationPage():

    def insert_email_to_input(self):
        try:
            el = self.driver.find_element(*AuthenticationPageLocators.EMAIL_INPUT)
            el.send_keys(email)
        except NoSuchElementException:
            print('EMAIL INPUT not found')

    def click_create_account_btn(self):
        try:
            el = self.driver.find_element(*AuthenticationPageLocators.CREATE_ACCOUNT_BTN)
            el.click()
        except NoSuchElementException:
            print('CREATE ACCOUNT BTN not found')
