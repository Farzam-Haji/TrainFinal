
from _4_Normal_user_panel import PendingUser


def user_profile():
    from _4_Normal_user_panel import PendingUser
    while True:

        print(f"\n\t.{PendingUser} Profile.")
        print("1. Buying Tickets")
        print("2. Edit Information Panel")
        print("3. Return to Previous Menu")
        user_input = input("\nSelect an Option => ")

        if user_input == "1":
            from _7_Purchase_Panel import purchase_panel
            purchase_panel()

        elif user_input == "2":
            from _6_Edit_info import edit_info_panel
            edit_info_panel()

        elif user_input == "3":
            return
        
        else:
            print ("Invalid option. Please try again.")
            input ("Press Enter to Go Back")

