import unittest
from Tests.registration_tests import RegistrationTest
from Tests.remind_password_test import RemindPasswordTest


tc1 = unittest.TestLoader().loadTestsFromTestCase(RegistrationTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(RemindPasswordTest)


sanityTestSuite = unittest.TestSuite([tc1, tc2])
unittest.TextTestRunner().run(sanityTestSuite)