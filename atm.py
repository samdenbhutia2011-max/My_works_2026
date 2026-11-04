# 21/03/26

from datetime import datetime, timedelta

saving_balance = 1000
current_balance = 1000
saving_trans = []
current_trans = []
new_account = []
main_pin = 1234
total=0



def pin():
    attempt = 0
    while attempt < 3:
        attempt += 1
        user_pin = int(input("Enter 4 digit Pin: "))
        if user_pin == main_pin:
            print("Access Granted.")
            return True
        if attempt < 3:
            print(f"Access Denied. Try again. {3 -attempt} out of 3 attempt")
        if (3 -attempt) == 0: 
            print("Your card is blocked. Try after 24 hrs.")
            return False


def cash_withdraw():
    global saving_balance
    global current_balance
    global saving_trans
    global current_trans
    

    print("-----------------------------------------------")
    # print("$$$$$$$$$$$$$$$$$  Main Menu  $$$$$$$$$$$$$$$$$")
    print("$$$$$$$$$$$$$$$ CASH WITHDRAW $$$$$$$$$$$$$$$$$")
    print("-----------------------------------------------")
    print("$ 1. Saving Account     |     2. Current Account\n"
          "$                   3. Back                   $")
    print("-----------------------------------------------")
    
    cash_user = input("Enter your choice: ")

    if cash_user == "1":
        saving_withdraw = float(input("Withdraw amount: "))
        saving_balance -= saving_withdraw
        print(f"You withdrew Rs. {saving_withdraw:.2f} and your Saving account balance is Rs. {saving_balance:.2f}")
        saving_trans.append(("Debit", saving_withdraw))

    elif cash_user == "2":
        current_withdraw = float(input("Withdraw amount: "))
        current_balance -= current_withdraw
        print(f"You withdrew Rs. {current_withdraw:.2f} and your Current account balance is Rs. {current_balance:.2f}")
        current_trans.append(("Debit", current_withdraw))
    
    else:
        print("Back to the Main Menu")
        


def cash_deposit():

    global saving_balance
    global current_balance
    global saving_trans
    global current_trans

    print("-----------------------------------------------")
    # print("$$$$$$$$$$$$$$$$$  Main Menu  $$$$$$$$$$$$$$$$$")
    print("$$$$$$$$$$$$$$$  CASH DEPOSIT $$$$$$$$$$$$$$$$$")
    print("-----------------------------------------------")
    print("$ 1. Saving Account     |     2. Current Account\n"
          "$                    3. Back                   $")
    print("-----------------------------------------------")
    cash_user = input("Enter your choice: ")

    if cash_user == "1":
        saving_deposit = float(input("Deposit amount: "))
        saving_balance += saving_deposit
        print(f"You deposited Rs. {saving_deposit:.2f} and your Saving account balance is Rs. {saving_balance:.2f}")
        saving_trans.append(("Credit:", saving_deposit))

    elif cash_user == "2":
        current_deposit = float(input("Deposit amount: "))
        current_balance += current_deposit
        print(f"You deposited Rs. {current_deposit:.2f} and your Current account balance is Rs. {current_balance:.2f}")
        current_trans.append(("Credit:", current_deposit))

    
    else:
        print("Back to the Main Menu")


def add_account():
    user = int(input("How many accounts do you want to open: "))
    for x in range(user):
        name = input("Your Full Name: ")
        account_num = int(input("Your Account Number: "))
        new_account.append("Name: ", name, "Account Number: ", account_num)
        print(new_account)


def mini_statement():
    global saving_balance
    global current_balance
    global saving_trans
    global current_trans

    print("------------------------------------------------")
    print("$$$$$$$$$$$$$$$ MINI STATEMENT $$$$$$$$$$$$$$$$$")
    print("------------------------------------------------")
    print("$                Saving Account                $")
    for transaction in saving_trans:
        print(f"INR {transaction[0]}:---{transaction[1]}      ")
    print("------------------------------------------------")


    
    print("------------------------------------------------")
    print("$$$$$$$$$$$$$$$ MINI STATEMENT $$$$$$$$$$$$$$$$$")
    print("------------------------------------------------")
    for transaction in current_trans:
        print(f"INR {transaction[0]}:---{transaction[1]}      ")
    print("------------------------------------------------")




def change_pin():
    global main_pin
    old_pin = int(input("Enter Old pin: "))
    if old_pin == main_pin:
        new_pin= int(input("Enter New pin: "))
        main_pin = new_pin
        print("You have changed your Pin.")
    else:
        print("Wrong Pin. Access Denied.")



def login_card():
   

    attempt = 0
    while attempt < 3:
        attempt += 1
        card = int(input("Enter Debit/Credit card no: "))
        if card == 456789:
            print("Access Granted.")
            return True
        
        if attempt < 3:
            print(f"Try again. {3 -attempt} attempts remaining.")
       
        if (3 -attempt) == 0:
            print("Your card has been blocked. Try after 24 hrs.")
            return False
    
        
def main():

    

    while True:
        print("-----------------------------------------------")
        print("$$$$$$$$$$$$$$$$$  Main Menu  $$$$$$$$$$$$$$$$$") 
        print("$ 1. Cash Withdraw     |      2. Cash Deposit $")
        print("$ 3. Change Pin        |      4. Mini \n" 
        "      $5. Exit               |         Statement    $")
        print("-----------------------------------------------")
            
        user = input("Enter your choice: ")

        if user == "1":
            if pin():
                cash_withdraw()
                break
            break
            
        elif user == "2":
            if pin():
                cash_deposit()
                break
            break

        elif user == "3":
            if pin():
                change_pin()
                break
            break

        elif user == "4":
            if pin():
                mini_statement()
                break
            break

        # elif user == "5":
        #     if pin():
                
        #         break
        #     break
       
        else: 
            break



while True:
    # print(datetime.now())
    now = datetime.now()
    print(now.date())
    print("-----------------------------------------------")
    print("$$$$$$$$$$$$$$$$$  WELCOME TO $$$$$$$$$$$$$$$$$")
    print("$$$$$$$$$$$$$$$$$   XYZ BANK  $$$$$$$$$$$$$$$$$")
    print("-----------------------------------------------")
    
    if login_card():
        main()
    
