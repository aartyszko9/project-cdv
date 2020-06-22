import unittest
from ddt import ddt, data, unpack
from Tests.base_test import BaseTest
from Pages.main_page import MainPage
from Pages.authentication_page import AuthenticationPage
from get_data import get_csv_data
from Pages.remind_password_page import RemindPasswdPage

@ddt
class RemindPasswordTest(BaseTest):
    @data(*get_csv_data('./Data/test_remind_password.csv'))
    @unpack
    def test_remind_password_happy_path(self, email, incorrect_email):
        print('Test Case 5: Remind password happy path')
        self.driver.implicitly_wait(10)
        mp = MainPage
        rpp = RemindPasswdPage

        ap = AuthenticationPage
        mp.click_sign_in_btn(self)
        ap.click_remind_passwd_link(self)
        rpp.expect_page_subheading(self)
        rpp.insert_email(self, email)
        rpp.submit(self)
        rpp.expect_alert_success(self)

    @data(*get_csv_data('./Data/test_remind_password.csv'))
    @unpack
    def test_non_exsisting_email(self, email, incorrect_email):
        print('Test Case 6: Remind pasword - insert non exsisting email and expect alert "There is no account registered for this email address."')
        self.driver.implicitly_wait(10)
        ap = AuthenticationPage
        mp = MainPage
        rpp = RemindPasswdPage

        mp.click_sign_in_btn(self)
        ap.click_remind_passwd_link(self)
        rpp.expect_page_subheading(self)
        rpp.insert_email(self, incorrect_email)
        rpp.submit(self)
        rpp.expect_alert_danger(self)


if __name__ == '__main__':
    unittest.main(verbosity=2, warnings='ignore')
