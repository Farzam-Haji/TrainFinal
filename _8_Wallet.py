from _11_BANK import API
import datetime
import os
from _4_Normal_user_panel import UserPanel, User_list, PendingUser

user_LoggedIn =  next(u for u in User_list if u.username == PendingUser) 

class transaction_history:
    def __init__(self, user, amount, payID, time):
        self.user = user
        self.amount = amount
        self.payID = payID
        self.time = time
        
    def __str__(self):
        return f" Successful Transaction. Amount: {self.amount}       Transaction ID: {self.payID}              Date And Time: {self.time}"
all_transactions = []


def Payment():
    from _4_Normal_user_panel import User_list, PendingUser
    global user_LoggedIn
    user_LoggedIn =  next(u for u in User_list if u.username == PendingUser) 

    def Receive_Card_info():
        card = input("16 digits card number => ")
        password = input("6 digits card's password => ")
        xp_month = input("2 digits card's expiry month => ")
        xp_year = input("4 digits card's expiry year => ")
        cvv2 = input("3 digits cvv2 => ")
        amount = input("please write how much you want to add to your wallet => ")
        return card , xp_month , xp_year , password , cvv2 , amount
            
    User_card, Card_xp_month, Card_xp_year, Card_password, Card_cvv2, Intended_amount = Receive_Card_info()
    
    try :
        card = API()
        payment = API.pay(card,User_card,int(Card_xp_month),int(Card_xp_year),Card_password, Card_cvv2, int(Intended_amount))
        Payment_ID = payment
        time_date = datetime.datetime.now()
        all_transactions.append(transaction_history(user_LoggedIn, int(Intended_amount) , Payment_ID, time_date))
        return int(Intended_amount)
    except ValueError as e :
        e = input('\nInvalid payment details.\nInput E to Exit\nOtherwise Enter to Try Again\n=>')
        if e == "E":
            return 0
        else:
            return Payment()
