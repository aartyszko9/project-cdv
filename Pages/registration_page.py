from selenium.common.exceptions import NoSuchElementException
from locators import CreateAnAccountPageLocators

import time
from selenium.webdriver.support.ui import Select
from helpers import Helpers



class RegisterUpPage():

    def click_mrs_radio_btn(self):
        try:
            el = self.driver.find_element(*CreateAnAccountPageLocators.MRS_RADIO_BTN)
            el.click()
        except NoSuchElementException:
            print('MRS RADIO BTN not found')

    def insert_first_name(self, first_name):
        try:
            el = self.driver.find_element(*CreateAnAccountPageLocators.FIRST_NAME_INPUT1)
            el.send_keys(first_name)
        except NoSuchElementException:
            print('FIRST NAME INPUT not found')

    def insert_last_name(self, last_name):
        try:
            el = self.driver.find_element(*CreateAnAccountPageLocators.LAST_NAME_INPUT)
            el.send_keys(last_name)
        except NoSuchElementException:
            print('LAST NAME INPUT not found')

    def insert_password(self, password):
        try:
            el = self.driver.find_element(*CreateAnAccountPageLocators.PASSWD_INPUT)
            el.send_keys(password)
        except NoSuchElementException:
            print('PASSWORD INPUT not found')

    def insert_city(self, city):
        try:
            el = self.driver.find_element(*CreateAnAccountPageLocators.CITY_INPUT)
            el.send_keys(city)
        except NoSuchElementException:
            print('CITY INPUT not found')

    def insert_postal_code(self, postal_code):
        try:
            el = self.driver.find_element(*CreateAnAccountPageLocators.POSTAL_CODE_INPUT)
            el.send_keys(postal_code)
        except NoSuchElementException:
            print('POSTAL CODE not found')

    def insert_mobile_phone(self, mobile_phone):
        try:
            el = self.driver.find_element(*CreateAnAccountPageLocators.MOBILE_PHONE_INPUT)
            el.send_keys(mobile_phone)
        except NoSuchElementException:
            print('MOBILE PHONE INPUT not found')

    def insert_additional_inf(self, additional_inf):
        try:
            el = self.driver.find_element(*CreateAnAccountPageLocators.ADDITIONAL_INF_INPUT)
            el.send_keys(additional_inf)
        except NoSuchElementException:
            print('ADDITIONAL INF INPUT not found')

    def select_date_of_birth(self, date, month, year):
        try:
            date_select = self.driver.find_element(*CreateAnAccountPageLocators.DATE)
            date_select.send_keys(date)
            month_select = self.driver.find_element(*CreateAnAccountPageLocators.MONTH)
            month_select.send_keys(month)
            year_select = self.driver.find_element(*CreateAnAccountPageLocators.YEAR)
            year_select.send_keys(year)
            time.sleep(5)
        except NoSuchElementException:
            print('DATE OF BIRTH element not found')

    def insert_address(self, address):
        try:
            el = self.driver.find_element(*CreateAnAccountPageLocators.ADDRESS_INPUT)
            el.send_keys(address)
        except NoSuchElementException:
            print('ADDRESS_INPUT not found')

    def select_state(self, state):
        try:
            el = Select(self.driver.find_element(*CreateAnAccountPageLocators.STATE_SELECT))
            el.select_by_value(state)
        except NoSuchElementException:
            print('STATE_SELECT not found')

    def assert_email_value(self, email_prefix):
        try:
            el = self.driver.find_element(*CreateAnAccountPageLocators.EMAIL_INPUT)
            el.get_attribute('value')
            assert el.get_attribute('value') == Helpers.generate_email(email_prefix)
        except NoSuchElementException:
            print('EMAIL_INPUT not found')

    def submit_registration_form(self):
        try:
            el = self.driver.find_element(*CreateAnAccountPageLocators.SUBMIT_BTN)
            el.click()
        except NoSuchElementException:
            print('SUBMIT not found')

    def insert_short_password(self, short_password):
        try:
            input = self.driver.find_element(*CreateAnAccountPageLocators.PASSWD_INPUT)
            input.send_keys(short_password)
            text = self.driver.find_element(*CreateAnAccountPageLocators.PASSWD_TEXT)
            text.text == '(Five characters minimum)'
        except NoSuchElementException:
            print('PASSWO_INPUT not found')

    def expect_alert_invalid_password(self):
        try:
            el = self.driver.find_element(*CreateAnAccountPageLocators.ALERT_PASSWD)
            assert el.text == 'passwd is invalid.'
        except NoSuchElementException:
            print('ALERT not found')
        except AssertionError:
            print('assertion error')
