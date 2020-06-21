import unittest
from ddt import ddt, data, unpack
from Tests.base_test import BaseTest
from Pages.main_page import MainPage
from Pages.authentication_page import AuthenticationPage
from Pages.registration_page import RegisterUpPage
from Pages.my_account_page import MyAccountPage
from get_data import get_csv_data
from helpers import Helpers

@ddt
class RegistrationTest(BaseTest):

    @data(*get_csv_data('../Data/test_succesfull_registration.csv'))
    @unpack
    def test_succesfull_registrarion(self, first_name, last_name, email_prefix, password, date, month, year, state, address, city, postal_code, mobile_phone, additional_inf):
        print('Test Case 1: Registration happy path')
        self.driver.implicitly_wait(10)
        mp = MainPage
        ap = AuthenticationPage
        rp = RegisterUpPage
        map = MyAccountPage
        mp.click_sign_in_btn(self)
        ap.insert_email(self, Helpers.generate_email(email_prefix))
        ap.submit(self)
        rp.click_mrs_radio_btn(self)
        rp.insert_first_name(self, first_name)
        rp.insert_last_name(self, last_name)
        rp.assert_email_value(self, email_prefix)
        rp.insert_password(self, password)
        rp.select_date_of_birth(self, date, month, year)
        rp.select_state(self, state)
        rp.insert_address(self, address)
        rp.insert_city(self, city)
        rp.insert_postal_code(self, postal_code)
        rp.insert_mobile_phone(self, mobile_phone)
        rp.insert_additional_inf(self, additional_inf)
        rp.submit_registration_form(self)
        map.expectMyAccountTitle(self)
        map.expectWelcomeText(self)

    @data(*get_csv_data('../Data/test_using_existing_email.csv'))
    @unpack
    def test_using_existing_email(self, existing_email):
        print('Test Case 2: Registration using exsisting email - expect alert saying that email is taken')
        self.driver.implicitly_wait(10)
        mp = MainPage
        ap = AuthenticationPage
        mp.click_sign_in_btn(self)
        ap.insert_email(self, existing_email)
        ap.submit(self)
        ap.expect_alert_exsisting_email(self)

    @data(*get_csv_data('../Data/test_using_invalid_email.csv'))
    @unpack
    def test_using_invalid_email(self, invalid_email):
        print('Test Case 3: Registration using invalid email - expect alert "Invalid email address" ')
        self.driver.implicitly_wait(10)
        mp = MainPage
        ap = AuthenticationPage
        mp.click_sign_in_btn(self)
        ap.insert_email(self, invalid_email)
        ap.submit(self)
        ap.expect_alert_invalid_email(self)

    @data(*get_csv_data('../Data/test_short_password.csv'))
    @unpack
    def test_short_password(self, email_prefix, short_password):
        print('Test Case 4: Inserted password is too short - expect alert "Password is invalid"')
        self.driver.implicitly_wait(10)
        mp = MainPage
        ap = AuthenticationPage
        rp = RegisterUpPage
        mp.click_sign_in_btn(self)
        ap.insert_email(self, Helpers.generate_email(email_prefix))
        ap.submit(self)
        rp.insert_short_password(self, short_password)
        rp.submit_registration_form(self)
        rp.expect_alert_invalid_password(self)


if __name__ == '__main__':
    unittest.main(verbosity=2)