import unittest
from selenium import webdriver

class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://automationpractice.com/index.php")
        self.driver.maximize_window()

    def tearDown(self):
        for method, error in self._outcome.errors:
            if error:
                test_method_name = self._testMethodName
                file = self.driver.save_screenshot("../Screenshots/%s.png" % test_method_name)
        self.driver.quit()