from Normal_user_panel import UserPanel
user_panel = UserPanel()
#---------------------------------------------------------------------------start_panel---------------------------------------------------------------------------
def start_panel():
    user_choice = input("\n1. General admin\n2. Train employee\n3. Normal user\n4. Exit\n=> ")
#-----------------------------------------------------------------------------------------------------------------------------------------
    if user_choice == "1" :
        admin_username , admin_password = "Admin_Train" , "Pass_Train"
        def General_admin() :
            print("Press ENTER to go back . ")
            entering_username , entering_password= input("Please enter admin's username : ") , input("Please enter admin's password : ")
            if admin_username == entering_username and admin_password == entering_password :
                print("\nWelcome to Management panel : ")
                from test2 import Management_panel
                Management_panel()
            elif entering_username == "" or entering_password == "" :
                start_panel()
            else :
                print("Wrong username or password . Try again .")
                General_admin()
        General_admin()
#-----------------------------------------------------------------------------------------------------------------------------------------
    elif user_choice == "2" :
        from TrainEmployee import main
        main()
#-----------------------------------------------------------------------------------------------------------------------------------------
    elif user_choice == "3" :
        # from Normal_user_panel import UserPanel
        # user_panel = UserPanel()
        user_panel.main_menu()
        start_panel()
#-----------------------------------------------------------------------------------------------------------------------------------------
    elif user_choice == "4" :
        print("Thank you for visiting us :)")
        exit()
#-----------------------------------------------------------------------------------------------------------------------------------------
    else :
        print("This is an invalid input . Try again .")
        start_panel()
#---------------------------------------------------------------------------get_password---------------------------------------------------------------------------

import msvcrt
def get_password(prompt):
    password = ""
    print(prompt, end='', flush=True)
    while True:
        ch = msvcrt.getch()
        if ch in [b'\r', b'\n']:
            break
        elif ch == b'\x08':
            if password:
                password = password[:-1]
                print('\b \b', end='', flush=True)
        else:
            password += ch.decode('utf-8')
            print('*', end='', flush=True)
    print()
    return password

#---------------------------------------------------------------------------calling---------------------------------------------------------------------------

if __name__ == "__main__" :
    print("\n<<< Hello dear user , welcome to the rail transportation system . >>>")
    start_panel()
