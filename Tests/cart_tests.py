import unittest
from Tests.base_test import BaseTest
from Pages.main_page import MainPage
from Pages.authentication_page import AuthenticationPage
from Pages.registration_page import RegisterUpPage
from Pages.my_account_page import MyAccountPage
import time

class CartTests(BaseTest):

    def test_add_to_cart(self):
        mp = MainPage
        print('Test Case 1: Add to cart happy path')
        self.driver.implicitly_wait(5)
        mp.click_tshirt_link(self)
        time.sleep(4)





if __name__ == '__main__':
    unittest.main(verbosity=2)