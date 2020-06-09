from selenium.common.exceptions import NoSuchElementException
from locators import MainPageLocators


class MainPage():

    def click_sign_in_btn(self):
        try:
            el = self.driver.find_element(*MainPageLocators.SIGN_IN_BTN)
            el.click()
        except NoSuchElementException:
            print('SIGN_IN_BTN not found')

    def click_tshirt_link(self):
        try:
            el = self.driver.find_element(*MainPageLocators.TSHIRT_LINK)
            el.click()
        except NoSuchElementException:
            print('TSHIRT_LINK not found')