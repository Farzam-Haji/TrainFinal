from user import User
from Normal_user_panel import UserPanel, User_list, PendingUser


def user_profile():
    while True:

        print(f"\n\t.{PendingUser} Profile.")
        print("1. Buying Tickets")
        print("2. Edit Information Panel")
        print("3. Return to Previous Menu")
        user_input = input("\nSelect an Option => ")

        if user_input == "1":
            from Purchase_Panel import purchase_panel
            purchase_panel()

        elif user_input == "2":
            from Edit_info import edit_info_panel
            edit_info_panel()

        elif user_input == "3":
            return
        
        else:
            print ("Invalid option. Please try again.")
            input ("Press Enter to Proceed")

