from selenium.common.exceptions import NoSuchElementException
from locators import MyAccountPageLocators

class MyAccountPage():

    def expectMyAccountTitle(self):
        try:
            el = self.driver.find_element(*MyAccountPageLocators.TITLE)
            el.text == "MY ACCOUNT"
        except NoSuchElementException:
            print('El TITLE not found')

    def expectWelcomeText(self):
        try:
            el = self.driver.find_element(*MyAccountPageLocators.WELCOME_TEXT)
            el.text == "Welcome to your account. Here you can manage all of your personal information and orders."
        except NoSuchElementException:
            print('WELCOME_TEXT not found')
