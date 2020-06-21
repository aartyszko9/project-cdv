from selenium.common.exceptions import NoSuchElementException
from locators import CreateAnAccountPageLocators

import time
from selenium.webdriver.support.ui import Select
from Pages import authentication_page



class RegisterUpPage():

    # YOUR PERSONAL INFORMATION:
    first_name = 'testname'
    last_name = 'testsurname'
    password = 'Test123!'
    short_password = 'test'
    # DATE OF BIRTH:
    date = '7'
    month = 'February'
    year = '2000'
    # YOUR ADDRESS:
    address = '2133  Randall Drive'
    city = 'Honolulu'
    postal_code = '96815'
    mobile_phone = '534 435 432'
    additional_inf = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque tempor tempor lorem ac ornare. Nullam.'

    def click_mrs_radio_btn(self):
        try:
            el = self.driver.find_element(*CreateAnAccountPageLocators.MRS_RADIO_BTN)
            el.click()
        except NoSuchElementException:
            print('MRS RADIO BTN not found')

    def insert_first_name(self):
        try:
            el = self.driver.find_element(*CreateAnAccountPageLocators.FIRST_NAME_INPUT1)
            el.send_keys(RegisterUpPage.first_name)
        except NoSuchElementException:
            print('FIRST NAME INPUT not found')

    def insert_last_name(self):
        try:
            el = self.driver.find_element(*CreateAnAccountPageLocators.LAST_NAME_INPUT)
            el.send_keys(RegisterUpPage.last_name)
        except NoSuchElementException:
            print('LAST NAME INPUT not found')

    def insert_password(self):
        try:
            el = self.driver.find_element(*CreateAnAccountPageLocators.PASSWD_INPUT)
            el.send_keys(RegisterUpPage.password)
        except NoSuchElementException:
            print('PASSWORD INPUT not found')

    def insert_city(self):
        try:
            el = self.driver.find_element(*CreateAnAccountPageLocators.CITY_INPUT)
            el.send_keys(*RegisterUpPage.city)
        except NoSuchElementException:
            print('CITY INPUT not found')

    def insert_postal_code(self):
        try:
            el = self.driver.find_element(*CreateAnAccountPageLocators.POSTAL_CODE_INPUT)
            el.send_keys(RegisterUpPage.postal_code)
        except NoSuchElementException:
            print('POSTAL CODE not found')

    def insert_mobile_phone(self):
        try:
            el = self.driver.find_element(*CreateAnAccountPageLocators.MOBILE_PHONE_INPUT)
            el.send_keys(RegisterUpPage.mobile_phone)
        except NoSuchElementException:
            print('MOBILE PHONE INPUT not found')

    def insert_additional_inf(self):
        try:
            el = self.driver.find_element(*CreateAnAccountPageLocators.ADDITIONAL_INF_INPUT)
            el.send_keys(RegisterUpPage.additional_inf)
        except NoSuchElementException:
            print('ADDITIONAL INF INPUT not found')

    def select_date_of_birth(self):
        try:
            date = self.driver.find_element(*CreateAnAccountPageLocators.DATE)
            date.send_keys(RegisterUpPage.date)
            month = self.driver.find_element(*CreateAnAccountPageLocators.MONTH)
            month.send_keys(RegisterUpPage.month)
            year = self.driver.find_element(*CreateAnAccountPageLocators.YEAR)
            year.send_keys(RegisterUpPage.year)
            time.sleep(5)
        except NoSuchElementException:
            print('DATE OF BIRTH element not found')

    def insert_address(self):
        try:
            el = self.driver.find_element(*CreateAnAccountPageLocators.ADDRESS_INPUT)
            el.send_keys(RegisterUpPage.address)
        except NoSuchElementException:
            print('ADDRESS_INPUT not found')

    def select_state(self):
        try:
            el = Select(self.driver.find_element(*CreateAnAccountPageLocators.STATE_SELECT))
            el.select_by_value('11')
        except NoSuchElementException:
            print('STATE_SELECT not found')

    def assert_email_value(self):
        try:
            el = self.driver.find_element(*CreateAnAccountPageLocators.EMAIL_INPUT)
            el.get_attribute('value')
            assert el.get_attribute('value') == authentication_page.email
        except NoSuchElementException:
            print('EMAIL_INPUT not found')

    def submit_registration_form(self):
        try:
            el = self.driver.find_element(*CreateAnAccountPageLocators.SUBMIT_BTN)
            el.click()
        except NoSuchElementException:
            print('SUBMIT not found')

    def insert_short_password(self):
        try:
            input = self.driver.find_element(*CreateAnAccountPageLocators.PASSWD_INPUT)
            input.send_keys(RegisterUpPage.short_password)
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
