import unittest
from Tests.base_test import BaseTest
from Pages.main_page import MainPage
from Pages.authentication_page import AuthenticationPage
from Pages.registration_page import RegisterUpPage
from Pages.my_account_page import MyAccountPage


class RegistrationTest(BaseTest):

    def test_succesfull_registrarion(self):
        print('Test Case 1: Registration happy path')
        self.driver.implicitly_wait(10)
        mp = MainPage
        ap = AuthenticationPage
        rp = RegisterUpPage
        map = MyAccountPage
        mp.click_sign_in_btn(self)
        ap.insert_email(self)
        ap.submit(self)
        rp.click_mrs_radio_btn(self)
        rp.insert_first_name(self)
        rp.insert_last_name(self)
        rp.assert_email_value(self)
        rp.insert_password(self)
        rp.select_date_of_birth(self)
        rp.select_state(self)
        rp.insert_address(self)
        rp.insert_city(self)
        rp.insert_postal_code(self)
        rp.insert_mobile_phone(self)
        rp.insert_additional_inf(self)
        rp.submit_registration_form(self)
        map.expectMyAccountTitle(self)
        map.expectWelcomeText(self)

    def test_using_exsisting_email(self):
        print('Test Case 2: Registration using exsisting email - expect alert saying that email is taken')
        self.driver.implicitly_wait(10)
        mp = MainPage
        ap = AuthenticationPage
        mp.click_sign_in_btn(self)
        ap.insert_exsising_email(self)
        ap.submit(self)
        ap.expect_alert_exsisting_email(self)

    def test_using_invalid_email(self):
        print('Test Case 3: Registration using invalid email - expect alert "Invalid email address" ')
        self.driver.implicitly_wait(10)
        mp = MainPage
        ap = AuthenticationPage
        mp.click_sign_in_btn(self)
        ap.insert_invalid_email(self)
        ap.submit(self)
        ap.expect_alert_invalid_email(self)

    def test_short_password(self):
        print('Test Case 4: Inserted password is too short - expect alert "Password is invalid"')
        self.driver.implicitly_wait(10)
        mp = MainPage
        ap = AuthenticationPage
        rp = RegisterUpPage
        mp.click_sign_in_btn(self)
        ap.insert_email(self)
        ap.submit(self)
        rp.insert_short_password(self)
        rp.submit_registration_form(self)
        rp.expect_alert_invalid_password(self)


if __name__ == '__main__':
    unittest.main(verbosity=2)