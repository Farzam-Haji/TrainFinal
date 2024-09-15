# from TrainEmployee import TrainEmployee
employees_list = []
employees_list_as_objects = []

#---------------------------------------------------------------------add_train_employee---------------------------------------------------------------------

def add_train_employee(train_employee_example) :
    from regex_class import regex
    usernames , emails = list(i["username"] for i in employees_list) , list(i["email"] for i in employees_list)
    if train_employee_example.__dict__["username"] in usernames or train_employee_example.__dict__["email"] in emails:
        print("This train employee has already been added . ")
    elif regex.email_reg(list(train_employee_example.__dict__.values())[2]) == False or regex.password_reg(list(train_employee_example.__dict__.values())[4]) == False :
        print("your email or password is not valid.")
    #----------------------------------------------------------------------------------------------------------------------------------------
        def already_added() :
            back = input("Press ENTER to go back . \nPress A to try again\n=>")
            if back == "A" :
                from TrainEmployee import TrainEmployee
                add_train_employee(TrainEmployee(input("Firstname : "),input("Lastname : "),input("Email : "),input("Username : "),input("Password : ")))
            elif back == "" :
                Management_panel()
            else :
                print("An invalid input . Try again . ")
                already_added()
    #----------------------------------------------------------------------------------------------------------------------------------------
        already_added()
    else :
        #print("liana2828@gmail.com".email_reg)
        print(regex.password_reg(list(train_employee_example.__dict__.values())[4]))
        if regex.email_reg(list(train_employee_example.__dict__.values())[2]) == True and regex.password_reg(list(train_employee_example.__dict__.values())[4]) == True :
            employees_list.append((train_employee_example.__dict__))
            employees_list_as_objects.append(train_employee_example)
            print("Employee added succssfully")
            input("Press ENTER to go back . \n")
            Management_panel()


#---------------------------------------------------------------------delete_train_employee---------------------------------------------------------------------

def delete_train_employee() :
    #----------------------------------------------------------------------------------------------------------------------------------------
    def no_such_username() :
        back = input("Press ENTER to go back . \nPress A to try again\n=> ")
        if back == "A" :
            delete_train_employee()
        elif back == "" :
            Management_panel()
        else :
            print("An invalid input . Try again . ")
            no_such_username()
    #----------------------------------------------------------------------------------------------------------------------------------------
    if len(employees_list) == 0 :
        print("No employees have registered yet . ")
        input("Press ENTER to go back . \n")
        Management_panel()
    else :
        train_employee_username = input("Enter train employee's username : ")
        exist = False
        for i in employees_list :
            if i["username"] == train_employee_username :
                employees_list.remove(i)
                employees_list_as_objects.remove(i)
                exist = True
                print("Employee's information has been deleted . ")
                input("Press ENTER to go back . \n")
                Management_panel()
                break
        if exist == False :
            print("No such username . ")
            no_such_username()
                
#---------------------------------------------------------------------return_employees_list---------------------------------------------------------------------

def return_employees_list() :
    if len(employees_list) != 0 :
        j = 1
        print("Employees' list : ")
        for i in employees_list :
            print(f"Employee {j} : {i}")
            j += 1
    else :
        print("No employees have registered yet . ")
    input("Press ENTER to go back . \n")
    Management_panel()

#---------------------------------------------------------------------Management_panel---------------------------------------------------------------------

def Management_panel() :
    # print("\nWelcome to Management panel : ")
    user_choise = input("1. Adding train employee\n2. Deleting train employee\n3. Viewing list of employees\n4. Exit Management panel\n=> ")
    
    if user_choise == "1" :
        from TrainEmployee import TrainEmployee
        add_train_employee(TrainEmployee(input("Firstname : "),input("Lastname : "),input("Email : "),input("Username : "),input("Password : ")))
    
    elif user_choise == "2" :
        delete_train_employee()
    
    elif user_choise == "3" :
        return_employees_list()
    
    elif user_choise == "4" :
        from test1 import start_panel
        start_panel()
    
    else :
        print("An invalid input . Try again . ")
        Management_panel()
        
#Management_panel()
