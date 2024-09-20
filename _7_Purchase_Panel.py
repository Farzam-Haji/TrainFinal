from _8_Wallet import Payment, all_transactions, transaction_history
from _3_TrainEmployee import Train_list
from _4_Normal_user_panel import UserPanel, User_list, PendingUser
# from _10_user_class import User
import os
import datetime
#---------------------------------------------------------------------------------------
class Train_Order:
    def __init__(self,name, price , num, ID):
        self.name = name
        self.price = price
        self.number_of_tickets = num
        self.ID = ID

    def __str__(self):
        return f"Ticket: {self.name} x {self.number_of_tickets}\t\t{self.price*self.number_of_tickets} Toman"

user_LoggedIn = next(u for u in User_list if u.username == PendingUser)
Wallet = 0

def wallet_update():
    from _4_Normal_user_panel import User_list, PendingUser
    global user_LoggedIn
    global Wallet
    user_LoggedIn = next(u for u in User_list if u.username == PendingUser)
    Wallet = 0
    for transaction in all_transactions:
        if transaction.user == user_LoggedIn:
            Wallet += int(transaction.amount)
    return Wallet

Shopping_Cart = []
total_cost = sum(i.price * i.number_of_tickets for i in Shopping_Cart)
time_date = datetime.datetime.now()


def index_finder(file_name = f'{user_LoggedIn.name} Recent_Transaction.txt'):
    if os.path.exists(file_name):
        with open (f'{file_name}' , 'r') as f:
            lines = f.readlines()
            if lines:
                last = lines[-1]
                last_ind = last.split()[0]
                return int(last_ind.split(".")[0])
            else:
                return 0
#---------------------------------------------------------------------------------------




def purchase_panel_2():
    global Wallet
    while True:

        print ("\n\t.Wallet Managment.")
        print (f"Total Cost:{total_cost}\nCurrent Wallet Balance :{Wallet}\n")
        print ("1. Charge Your Wallet")
        print ("2. Open Recent Transaction")
        print ("3. Return to Previous Menu")
        input_ = input("Choose an Option => ")

        if input_ == "1":
            print ("\n....\tRedirecting to Bank\t....\n")
            amount = Payment()
            if amount > 0:
                Wallet += amount
                print ("\nYour Payment Was Successful. Your Wallet Has Been Updated")
                input ("Press Enter to Go Back")
            else:
                input ("\nYour Payment Was Not Successful.\nPress Enter to Go Back ")

        elif input_ == "2":
            if os.path.exists(f'{user_LoggedIn.name} Recent_Transaction.txt'):
                os.remove (f'{user_LoggedIn.name} Recent_Transaction.txt')
            for transaction in all_transactions:
                if transaction.user == user_LoggedIn:
                    with open (f'{user_LoggedIn.name} Recent_Transaction.txt' , 'a') as a:
                        ind = index_finder()
                        a.write(f"{ind+1}. {transaction}\n") 
            os.startfile(f'{user_LoggedIn.name} Recent_Transaction.txt')  
            
            if not os.path.exists(f'{user_LoggedIn.name} Recent_Transaction.txt'):
                input("\nYou Have Not Made Any Transaction Yet.\nPress Enter to Go Back")


        elif input_ == "3":
            return
        
        else:
            print ("\nInvalid Input. Please Try Agin")
            input ("Press Enter to Go Back")


def ticket_manager():
    while True:

        print("\n\t.Adding Items to Shopping Cart.")
        intro = input("1. Choose The Ticket and How Many of That Ticket You Want to Add\n2. Return to Shopping Panel\n\nChoose an Option => ")

        if intro == "1":
            ticket = input("\nTicket ID: ")
            quantity = input("Quantity: ")
            exist = False
            for t in Train_list:
                if str(t.train_id) == str(ticket):
                    exist = True
                    hover_train = t
                    if int(hover_train.capacity) < int(quantity):
                        print("\nThis Ticket is Not Available in This Quantity")
                        input ("Press Enter to Go Back")
                    else:
                        Shopping_Cart.append(Train_Order(hover_train.name , float(hover_train.ticket_price) , int(quantity) , hover_train.train_id))

                        hover_train.capacity -= int(quantity)
                        print ("\nYour Shopping Cart Has been Updated") 
                        input ("Press Enter to Go Back")
       
            
            else:
                if exist == False:
                    print ("\nThis Ticket was not found")
                    input ("Press Enter to Go Back")

        elif intro == "2":
            return
        
        else:
            print ("\nInvalid Input. Please Try Agin")
            input ("Press Enter to Go Back")


def purchase_panel():

    global Wallet
    global total_cost
    global Shopping_Cart
    Wallet = wallet_update()
    while True:

        total_cost = sum(i.price * i.number_of_tickets for i in Shopping_Cart)

        print("\n\t.Shopping Panel.")
        print(f"Your Wallet Balance: {Wallet}")
        if len(Shopping_Cart)== 0:
            print ("Your Shopping Cart: Empty")
        else:
            print (f"Your Shopping Cart: {[f'{i.name} x {i.number_of_tickets}' for i in Shopping_Cart]}")
            print (f"Total Cost of Your Cart: {total_cost}")
        print ("\n1. Receive a File of Available Tickets")
        print ("2. Manage Your Wallet")
        print ("3. Add Ticket to Your Shopping Cart")
        print ("4. Payment")
        print ("5. Help")
        print ("6. Return to User Menu")
        input_ = input("\nChoose an Option => ")
        
        if input_ == "1":
            with open ('Train_list.txt', 'w') as f:
                for i in Train_list:
                    f.write (f"{i}\n----------\n")
            print ("\nYour File Has Been Created")
            train_file = input ("1. Open The File Containing All Trains' Information.\nPress Enter to Go Back\nSelect an Option => ")
            if train_file == "1":
                os.startfile('Train_list.txt')
            else:
                continue
        
        elif input_ == "2":
            purchase_panel_2()

        elif input_ == "3":
            ticket_manager()

        elif input_ == "4":
            if len(Shopping_Cart) == 0:
                print ("\nYour Shopping Cart is Empty. Please Add At Least One Item First")
                input ("Press Enter to Return")
                continue
            elif Wallet >= total_cost:
                Wallet -= total_cost
                with open ('Ticket.txt','a') as f:
                    for i in Shopping_Cart:
                        f.write(f"{i}\n------------\n")
                all_transactions.append(transaction_history(user_LoggedIn , -total_cost , "Withdrawal" , time_date))
                Shopping_Cart.clear()
                print ("\nYour Purchase Was Successful. A File Containing Your Ticket Details Has Been Created")
                ticket_file = input ("1. Open your Ticket File.\nPress Enter to Return\n Select an Option => ")
                if ticket_file == "1":
                    os.startfile('Ticket.txt')
                else:
                    continue
            else:
                print ("\nInsufficient Amount in Your Wallet. Please Charge Your Wallet to Proceed")
                input ("Press Enter to Return")

        elif input_ == "5":
            print(".You can add tickets to your shopping cart via option 3\n.In order to complete the payment process you have to choose option 4, while you have sufficient amount in your wallet\n.You can charge your wallet by choosing option 2")
            input("Press Enter to Move Back to Previous Menu")

        elif input_ == "6":
            for order in Shopping_Cart:
                hover_train  = next(t for t in Train_list if t.train_id == order.ID)
                hover_train.capacity += order.number_of_tickets
            Shopping_Cart.clear()
            return
        
        else:   
            print ("\nInvalid Input. Please Try Agin")
            input ("Press Enter to Go Back")