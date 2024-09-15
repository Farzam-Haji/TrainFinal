from Normal_user_panel import UserPanel, User_list, PendingUser
from user import User
from regex_class import regex
from test1 import user_panel

#----------------------------------------------------------------------
class extended_UserPanel(UserPanel):
    def find_user_info(self, username):
        user = next((u for u in User_list if u.username == username), None)
        if user:
            user_info =  (user.__dict__)
            return user, user_info
        else:
            print("This Username does not exist.")

def get_user():
    obj = extended_UserPanel()
    logged_in_user = PendingUser
    global user_, user_info
    user_, user_info = obj.find_user_info(logged_in_user)
#----------------------------------------------------------------------




def edit_info_panel2():
    while True:
        print("\n\t.Edit Information Panel.\nSelect The Attribute You Want to Change:")
        print ("1. Name")
        print ("2. Password")
        print ("3. Email")
        print ("4. Back to Preivous Menu\n#You Can Not Change Your Username")
        atr = input ("\nSelect an Option => ")


        if atr == "1":
            suggested_name = input("New Name: ")
            User.name_setter(user_, suggested_name)
            print ("\nYour Name Changed Successfully")
            input ("Press Enter to Proceed")


        elif atr == "2":
            suggested_password = input("New Password: ")
            if regex.password_reg(suggested_password):
                User.password_setter(user_, suggested_password)
                print ("\nYour Password Changed Successfully")
                input ("Press Enter to Proceed")

            else:
                print("\nThis Password Cannot be Set")
                password_help = input ("Input H to Show Help or Press Enter to Proceed =>")
                if password_help == "H":
                    print("\n. Your Password Should Have At Least < One Letter And One Number And One of The Charachters & Or @ >")
                    input ("Press Enter to Proceed")
                    continue
                else:
                    continue
                    

        elif atr == "3":
            suggested_email = input("New Email: ")
            if not user_panel.is_email_taken(suggested_email):
                if regex.email_reg(suggested_email):
                    User.email_setter(user_, suggested_email)
                    print ("\nYour Email Changed Successfully")
                    input ("Press Enter to Proceed")

                else:
                    print("\nThis Email Cannot be Set")
                    email_help = input ("Press H to Show Help or Press Enter to Proceed => ")
                    if email_help == "H":
                        print ("\n. Your Email Should Have < One @ And One . Followed By At Least One Charachter >")
                        input ("Press Enter to Proceed")
                        continue
                    else:
                        continue

            else:
                print ("\nThis Email is Already Taken")
                input ("Press Enter to Proceed")


        elif atr == "4":
            return
        
        else:
            print("Invalid Input. Please Try Again")
            input ("Press Enter to Proceed")



def edit_info_panel():
    while True:
        get_user()
        print ("\n\t.Edit Information Panel.")
        print (f"Your Information: {user_info}")
        print ("1. Change Your Information")
        print ("2. Return to Previous Menu")
        choice = input("Select an Option => ")

        if choice == "1":
            edit_info_panel2()

        elif choice == '2':
            return

        else:
            print ("\nInvalid Input. Please Try Agin")
            input ("Press Enter to Proceed")

