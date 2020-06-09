from selenium.common.exceptions import NoSuchElementException
from locators import AuthenticationPageLocators
from helpers import Helpers
import time


email = 'aartyszko+' + Helpers.randomString(5) + '@gmail.com'
exsisting_email = 'aartyszko@gmail.com'
invalid_email = 'aartyszko.com'

class AuthenticationPage():

    def insert_email(self):
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

    def insert_exsising_email(self):
        try:
            el = self.driver.find_element(*AuthenticationPageLocators.EMAIL_INPUT)
            el.click()
            el.send_keys(exsisting_email)
        except NoSuchElementException:
            print('EMAIL_INPUT not found')

    def expect_alert_exsisting_email(self):
        try:
            el = self.driver.find_element(*AuthenticationPageLocators.ALERT_MESSAGE)
            el.text == "An account using this email address has already been registered. Please enter a valid password or request a new one."
        except NoSuchElementException:
            print('ALERT_MESSAGE not found')
        except AssertionError:
            print('expect_alert assertion error')

    def insert_invalid_email(self):
        try:
            el = self.driver.find_element(*AuthenticationPageLocators.EMAIL_INPUT)
            el.send_keys(invalid_email)
        except NoSuchElementException:
            print('EMAIL_INPUT not found')

    def expect_alert_invalid_email(self):
        try:
            el = self.driver.find_element(*AuthenticationPageLocators.ALERT_MESSAGE)
            el.text == "Invalid email address."
        except NoSuchElementException:
            print('ALERT_MESSAGE not found')
        except AssertionError:
            print('expect_alert assertion error')


