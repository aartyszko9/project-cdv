import unittest
from Tests.base_test import BaseTest
import time
from Pages.main_page import MainPage
from Pages.authentication_page import AuthenticationPage
from Pages.registration_page import RegisterUp
from Pages.my_account_page import MyAccountPage


class RegistrationTest(BaseTest):

    def test_succesfull_registrarion(self):
        print('Test Case 1: Registration happy path')
        self.driver.implicitly_wait(20)
        mp = MainPage
        ap = AuthenticationPage
        rp = RegisterUp
        map = MyAccountPage
        mp.click_sign_in_btn(self)
        ap.insert_email_to_input(self)
        ap.click_create_account_btn(self)
        rp.click_mrs_radio_btn(self)
        rp.insert_first_name(self)
        rp.insert_last_name(self)
        rp.assert_email_value(self)
        rp.insert_address(self)
        rp.select_state(self)
        rp.insert_password(self)
        rp.insert_city(self)
        rp.insert_postal_code(self)
        rp.insert_mobile_phone(self)
        rp.insert_additional_inf(self)
        rp.select_date_of_birth(self)
        rp.submit_registration_form(self)
        map.expectMyAccountTitle(self)

    def test_using_exsisting_email(self):
        print('Test Case 2: Registration using exsisting email - expect message saying that email is taken')




if __name__ == '__main__':
    unittest.main(verbosity=2)