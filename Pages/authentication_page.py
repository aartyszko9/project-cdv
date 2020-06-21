from selenium.common.exceptions import NoSuchElementException
from locators import AuthenticationPageLocators
import time

class AuthenticationPage():

    def insert_email(self, email):
        try:
            el = self.driver.find_element(*AuthenticationPageLocators.EMAIL_INPUT)
            el.send_keys(email)
        except NoSuchElementException:
            print('EMAIL INPUT not found')

    def submit(self):
        try:
            el = self.driver.find_element(*AuthenticationPageLocators.CREATE_ACCOUNT_BTN)
            el.click()
            time.sleep(2)
        except NoSuchElementException:
            print('CREATE ACCOUNT BTN not found')

    def expect_alert_exsisting_email(self):
        try:
            el = self.driver.find_element(*AuthenticationPageLocators.ALERT_MESSAGE)
            el.text == "An account using this email address has already been registered. Please enter a valid password or request a new one."
        except NoSuchElementException:
            print('ALERT_MESSAGE not found')
        except AssertionError:
            print('expect_alert assertion error')

    def expect_alert_invalid_email(self):
        try:
            el = self.driver.find_element(*AuthenticationPageLocators.ALERT_MESSAGE)
            el.text == "Invalid email address."
        except NoSuchElementException:
            print('ALERT_MESSAGE not found')
        except AssertionError:
            print('expect_alert assertion error')


