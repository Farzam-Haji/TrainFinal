import re

class regex:
    def __init__(self):
        pass

    @staticmethod
    def email_reg(email):
        pattern = r'^.*@.+\..+$'
        return bool(re.match(pattern, email))

    @staticmethod
    def password_reg(password):
        return bool( len(password)>= 8 and all( ((re.search("[a-zA-Z]", password)), (re.search("[0-9]", password)), (re.search("[@&]", password))) ) )
