from user import User
#-----------------------------------------------------------------------
User_list = []
PendingUser = ''
#------------------------------------------------------------------------
class UserPanel:
    def __init__(self):
        self.users = []

    def main_menu(self):
        global User_list # edit
        if len(User_list) != 0 : #edit
            self.users = User_list[:] #edit
        while True:
            print("\n      Normal User Panel      ")
            print("1. Sign Up")
            print("2. Login")
            print("3. Back to Start Menu")
            choice = input("Please select an option: ")

            if choice == "1":
                self.signup()
            elif choice == "2":
                self.login()
            elif choice == "3":
                print("Returning to start menu.")
                User_list = self.users[:] #edit
                break
            else:
                print("Invalid option. Please try again.")

    def signup(self):
        while True:
            print("\n       Sign Up        ")
            print("1. sign up")
            print("2. Back to User Panel")
            choice = input("Please select an option: ")

            if choice == "1":
                name = input("Name: ")
                email = input("Email: ")
                username = input("Username: ")
                password = input("Password: ")

                if self.is_email_taken(email) and self.is_username_taken(username) :
                    print("This username and email are already used.")
                elif self.is_email_taken(email):
                    print("This email is already sign up.")
                elif self.is_username_taken(username):
                    print("This username is already used.")
                else:
                    new_user = User(name, email, username, password)
                    self.users.append(new_user)
                    print("Sign up successful!")
                    return  
            elif choice == "2":
                print("Returning to User Panel.")
                return  
            else:
                print("Invalid option. Please try again.")

    def is_email_taken(self, email):
        return any(user.email == email for user in self.users)

    def is_username_taken(self, username):
        return any(user.username == username for user in self.users)

    def login(self):
        while True:
            print("\n       Login       ")
            print("1. Login")
            print("2. Back to User Panel")
            choice = input("Please select an option: ")

            if choice == "1":
                username = input("Username: ")
                password = input("Password: ")

                user = self.find_user(username, password)

                if user:
                    print(f"Welcome {user.name}! You have successfully logged in.")
                    # self.purchase_panel()
                    #--------------------------------------------------------------------------------------------
                    global User_list
                    User_list = self.users [:]
                    global PendingUser
                    PendingUser = username 
                    from User_Profile import user_profile 
                    user_profile() 
                    self.users = User_list [:]
                    #---------------------------------------------------------------------------------------------
                    return  
                else:
                    print("Invalid username or password. Please try again.")
            elif choice == "2":
                print("Returning to User Panel.")
                return  
            else:
                print("Invalid option. Please try again.")

    def find_user(self, username, password):
        return next((user for user in self.users if user.username == username and user.password == password), None)

    def purchase_panel(self):
        print("\n       Purchase Panel      ")
        print("This Section is not Complete")
        input("Press Enter to return to the user panel.")
