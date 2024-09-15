from BANK import API

def Payment():

    def Receive_Card_info():
        card = input("Please write your 16 digits card number: ")
        password = input("please write your 6 digits card's password: ")
        xp_month = int(input("please write your 2 digits card's expiry month: "))
        xp_year = int(input("please write your 4 digits card's expiry year: "))
        cvv2 = input("please write your 3 digits cvv2: ")
        amount = input("please write how much you want to add to your wallet: ")
        return card , xp_month , xp_year , password , cvv2 , amount
    User_card, Card_xp_month, Card_xp_year, Card_password, Card_cvv2, Intended_amount = Receive_Card_info()
    
    try :
        card = API()
        payment = API.pay(card,User_card,Card_xp_month,Card_xp_year,Card_password, Card_cvv2, Intended_amount)
        Payment_ID = payment #extra point 2
        # amount_ = re.sub(r'^\d{16}(\d+)\d{6}$', r'\1' , payment)
        return int(Intended_amount)
    except ValueError as e :
        print('Invalid payment details.\nPlease try again')
        return Payment()

    