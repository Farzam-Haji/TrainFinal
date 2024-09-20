
class User:
    def __init__(self, name, email, username, password):
        self.name = name
        self.email = email
        self.username = username
        self.password = password


#-------------------------------------------------------------------
    def email_setter(self,new_email):
        self.email = new_email
    def password_setter (self, new_password):
        self.password = new_password
    def name_setter(self, new_name):
        self.name = new_name


    def __str__(self):
        return f"name:{self.name}\npass:{self.password}\nemail:{self.email}\nuser:{self.username}"
#--------------------------------------------------------------------