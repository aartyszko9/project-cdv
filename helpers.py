import random
import string

class Helpers():

    def randomString(stringLength=8):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(stringLength))

    def generate_email(email_prefix):
        email = email_prefix + '+' + Helpers.email_number + '@gmail.com'
        return email

    email_number = randomString(5)

