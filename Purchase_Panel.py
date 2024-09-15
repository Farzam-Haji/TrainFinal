from Wallet_test import Payment
from TrainEmployee import employee, TrainEmployee, Train

#---------------------------------------------------------------------------------------
class Train_Order:
    def __init__(self,name, price , num):
        self.name = name
        self.price = price
        self.number_of_tickets = num

    def __str__(self):
        return f"Ticket: {self.name} x {self.number_of_tickets}\t\t{self.price*self.number_of_tickets} Toman"
    


Shopping_Cart = []
Wallet = 0
total_cost = sum(i.price * i.number_of_tickets for i in Shopping_Cart)
#---------------------------------------------------------------------------------------




def purchase_panel_2():
    global Wallet
    while True:

        print ("\n\tWallet Managment")
        print (f"Total Cost:{total_cost}\nCurrent Wallet Balance :{Wallet}\n")
        print ("1. Charge Your Wallet")
        print ("2. Return to Previous Menu")
        input_ = input("Choose an Option => ")

        if input_ == "1":
            print ("\n....\tRedirecting to Bank\t....")
            Wallet += Payment()
            print ("\nYour Payment Was Successful. Your Wallet Has Been Updated")
            input ("\nPress Enter to Proceed")
            
        elif input_ == "2":
            return
        
        else:
            print ("\nInvalid Input. Please Try Agin")
            input ("Press Enter to Proceed")


def ticket_manager():
    while True:

        print("\n\t.Adding Items to Shopping Cart.")
        intro = input("1. Choose The Ticket and How Many of That Ticket You Want to Add\n2. Return to Shopping Panel\n\nChoose an Option => ")

        if intro == "1":
            ticket = input("\nTicket ID: ")
            quantity = input("Quantity: ")
            exist = False
            for t in employee.trains.values():
                if str(t.train_id) == str(ticket):
                    exist = True
                    hover_train = t
                    if int(hover_train.capacity) < int(quantity):
                        print("\nThis Ticket is Not Available in This Quantity")
                        input ("\nPress Enter to Proceed")
                    else:
                        Shopping_Cart.append(Train_Order(hover_train.name , int(hover_train.ticket_price) , int(quantity)))

                        hover_train.capacity -= int(quantity)
                        print ("Your Shopping Cart Has been Updated") 
                        input ("\nPress Enter to Proceed")
       
            
            else:
                if exist == False:
                    print ("\nThis Ticket was not found")
                    input ("Press Enter to Proceed")

        elif intro == "2":
            return
        
        else:
            print ("\nInvalid Input. Please Try Agin")
            input ("Press Enter to Proceed")


def purchase_panel():
    global Wallet
    global total_cost
    while True:

        total_cost = sum(i.price * i.number_of_tickets for i in Shopping_Cart)

        print("\n\t.Shopping Panel")
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
                for i in employee.trains.values():
                    f.write (f"{i}\n----------\n")
            print ("\nYour File Has Been Created")
            input ("Press Enter to Proceed")
        
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
                with open ('Ticket.txt','w') as f:
                    for i in Shopping_Cart:
                        f.write(f"{i}\n------------\n")
                Shopping_Cart.clear()
                print ("\nYour Purchase Was Successful. A File Containing Your Ticket Details Has Been Created")
                input ("Press Enter to Return")
                continue
            else:
                print ("\nInsufficient Amount in Your Wallet. Please Charge Your Wallet to Proceed")
                input ("Press Enter to Return")

        elif input_ == "5":
            print(".You can add tickets to your shopping cart via option 3\n.In order to complete the payment process you have to choose option 4, while you have sufficient amount in your wallet\n.You can charge your wallet by choosing option 2")
            input("Press Enter to Move Back to Previous Menu")

        elif input_ == "6":
            return
        
        else:   
            print ("\nInvalid Input. Please Try Agin")
            input ("Press Enter to Proceed")