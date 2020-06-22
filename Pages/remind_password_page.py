from selenium.common.exceptions import NoSuchElementException
from locators import RemindPasswordLocators

class RemindPasswdPage():

    def insert_email(self, email):
        try:
            el = self.driver.find_element(*RemindPasswordLocators.EMAIL_INPUT)
            el.send_keys(email)
        except NoSuchElementException:
            print('EMAIL_INPUT not found')

    def expect_page_subheading(self):
        try:
            el = self.driver.find_element(*RemindPasswordLocators.PAGE_SUBHEADING)
            assert el.text == "FORGOT YOUR PASSWORD?"
        except NoSuchElementException:
            print('PAGE_SUBHEADING not found')
        except AssertionError:
            print('assertion error')

    def submit(self):
        try:
            el = self.driver.find_element(*RemindPasswordLocators.SUBMIT)
            el.click()
        except NoSuchElementException:
            print('SUBMIT not found')

    def expect_alert_success(self):
        try:
            el = self.driver.find_element(*RemindPasswordLocators.ALERT_SUCCESS)
            assert el.text == "A confirmation email has been sent to your address: aartyszko@gmail.com"
        except NoSuchElementException:
            print('ALERT_SUCCESS not found')
        except AssertionError:
            print('assertion error')

    def expect_alert_danger(self):
        try:
            el = self.driver.find_element(*RemindPasswordLocators.ALERT_DANGER)
            assert el.text == 'There is no account registered for this email address.'
        except NoSuchElementException:
            print('ALERT_DANGER not found')
        except AssertionError:
            print('assertion error')