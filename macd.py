# 09/04/26


cart = []
import csv

def main_menu():

        while True:

            try:

                print("########## Mac Donald ##########")
                print("##### HOw MAY I SERVE YOU ######")
                print("################################\n")

                print("----------MAIN MENU-------------")
                print("1. Burger     |    2. Happy Meal")
                print("3. French     |    4. Beverages ")
                print("   Fries      |    5. Snack Wrap")
                print("6. Remove     |    7. View order")
                print("         8. Checkout"            )
                print("--------------------------------\n")

                user = int(input("Enter your choice: "))

                if user == 1:
                    burger()

                if user == 2:
                    happy_meal()

                if user == 3:
                    french_fries()

                if user == 4:
                    beverages()

                if user == 5:
                    snack_wrap()

                if user == 6:
                    remove()

                if user == 7:
                    view()

                if user == 8:
                    checkout()
                    main = input("Do you want to EXIT, Y/N: ")
                    if main == "y":
                        break                    

                else:
                    print("Invalid operation. Try again.")
                    print("****************************\n")
                    continue
    
            except ValueError:
                print("ValueError: Please Input a number between 1 - 8. Try again. \n")
                 



def burger():
    
    global cart

    while True:

        try:
            print("\n********* BURGER MENU ***********")
            print("   ITEMS          |       RATE")
            
            print("1. Big Mac        |      INR. 220")
            print("2. Classic Burger |      INR. 150")
            print("3. Bacon &        |      INR. 190")
            print("   Cheese         |              ")
            print("4. Cheese Burger  |      INR. 120")
            print("5. Back")
            print("*********************************")
            bur_user = int(input("Choose your Burger:"))
            
            if bur_user == 1:
                name ="Big Mac"
                price = 220
                quantity = int(input("Quantity: "))
                total_bur = price * quantity
                cart.append((name, quantity, price, total_bur))
                print(f"Your total price for {quantity} {name}: INR. {total_bur} ")

            elif bur_user == 2:
                name ="Classic Burger"
                price = 150
                quantity = int(input("Quantity: "))
                total_bur = price * quantity
                cart.append((name, quantity, price, total_bur))
                print(f"Your total price for {quantity} {name}: INR. {total_bur} ")

            elif bur_user == 3:
                name ="Bacon & Cheese"
                price = 190
                quantity = int(input("Quantity: "))
                total_bur = price * quantity
                cart.append((name, quantity, price, total_bur))
                print(f"Your total price for {quantity} {name}: INR. {total_bur} ")

            elif bur_user == 4:
                name ="Classis Burger"
                price = 120
                quantity = int(input("Quantity: "))
                total_bur = price * quantity
                cart.append((name, quantity, price, total_bur))
                print(f"Your total price for {quantity} {name}: INR. {total_bur} ")
                
            elif bur_user == 5:
                print("Going back to the Main Menu")
                print("***************************\n")
                break

            else:
                print("Invalid operation. Try again.")
                print("****************************\n")
                continue
                
            choice = input("Do you want to add more (Y/N): ")
            if choice != "y":
                print("********************************\n")
                break

        except ValueError:
            print("ValueError: Please Input a number between 1 - 5. Try again. \n")


            
def happy_meal():

    global cart
    
    while True:
        
        try:

            print("********* HAPPY MEAL MENU ***********")
            print("   ITEMS          |       RATE")
            
            print("1. Hamburger      |              ")
            print("   Happy Meal     |      INR. 320")
            print("2. 4 Piece        |              ")
            print("   Nuggets Happy  |              ")
            print("   Meal           |      INR. 280")
            print("              3. Back            ")
            print("*********************************")

            happy_meal_user = int(input("Choose your Burger: "))

            if happy_meal_user == 1:
                    name ="Hamburger Happy Meal"
                    price = 320
                    quantity = int(input("Quantity: "))
                    total_bur = price * quantity
                    cart.append((name, quantity, price, total_bur))
                    print(f"Your total price for {quantity} {name}: INR. {total_bur} ")

            elif happy_meal_user == 2:
                name ="4 Piece Nuggets Happy Meal"
                price = 280
                quantity = int(input("Quantity: "))
                total_bur = price * quantity
                cart.append((name, quantity, price, total_bur))
                print(f"Your total price for {quantity} {name}: INR. {total_bur} ")

            elif happy_meal_user == 3:
                print("Going back to the Main Menu")
                print("***************************\n")
                break

            else:
                print("Invalid operation. Try again.")
                print("****************************\n")
                continue
                

            choice = input("Do you want to add more (Y/N): ")
            if choice != "y":
                print("********************************\n")
                break

        except ValueError:
            print("ValueError: Please Input a number between 1 - 5. Try again. \n")


def french_fries():
    
    global cart

    while True:

        try:

            print("********* FRENCH FRIES MENU ***********")
            print("   ITEMS          |       RATE")
            
            print("1. Small Fries    |      INR. 65")
            print("2. Normal Fries   |      INR. 75")
            print("3. Large Fries    |      INR. 85")
            print("              4. Back           ")
            print("*********************************")

            french_fries_user = int(input("Choose your Fries: "))

            if french_fries_user == 1:
                    name ="Small Fries"
                    price = 65
                    quantity = int(input("Quantity: "))
                    total_bur = price * quantity
                    cart.append((name, quantity, price, total_bur))
                    print(f"Your total price for {quantity} {name}: INR. {total_bur} ")

            elif french_fries_user == 2:
                name ="Normal Fries"
                price = 75
                quantity = int(input("Quantity: "))
                total_bur = price * quantity
                cart.append((name, quantity, price, total_bur))
                print(f"Your total price for {quantity} {name}: INR. {total_bur} ")

            elif french_fries_user == 3:
                name ="Large Fries"
                price = 85
                quantity = int(input("Quantity: "))
                total_bur = price * quantity
                cart.append((name, quantity, price, total_bur))
                print(f"Your total price for {quantity} {name}: INR. {total_bur} ")

            elif french_fries_user == 4:
                print("Going back to the Main Menu")
                print("***************************\n")
                break

            else:
                print("Invalid operation. Try again.")
                print("****************************\n")
                continue
                

            choice = input("Do you want to add more (Y/N): ")
            if choice != "y":
                print("********************************\n")
                break

        except ValueError:
            print("ValueError: Please Input a number between 1 - 5. Try again. \n")


def beverages():

    global cart

    while True:

        try:

            print("********* BEVERAGES MENU ***********")
            print("   ITEMS          |       RATE")
            
            print("1. Coke           |      INR. 42")
            print("2. Fanta          |      INR. 33")
            print("3. Sprite         |      INR. 38")
            print("              4. Back           ")
            print("*********************************")

            beverages_user = int(input("Choose your Beverages: "))

            if beverages_user == 1:
                    name ="Coke"
                    price = 42
                    quantity = int(input("Quantity: "))
                    total_bur = price * quantity
                    cart.append((name, quantity, price, total_bur))
                    print(f"Your total price for {quantity} {name}: INR. {total_bur} ")

            elif beverages_user == 2:
                name ="Fanta"
                price = 33
                quantity = int(input("Quantity: "))
                total_bur = price * quantity
                cart.append((name, quantity, price, total_bur))
                print(f"Your total price for {quantity} {name}: INR. {total_bur} ")

            elif beverages_user == 3:
                name ="Sprite"
                price = 38
                quantity = int(input("Quantity: "))
                total_bur = price * quantity
                cart.append((name, quantity, price, total_bur))
                print(f"Your total price for {quantity} {name}: INR. {total_bur} ")

            elif beverages_user == 4:
                print("Going back to the Main Menu")
                print("***************************\n")
                break

            else:
                print("Invalid operation. Try again.")
                print("****************************\n")
                continue
                

            choice = input("Do you want to add more (Y/N): ")
            if choice != "y":
                print("********************************\n")
                break

        except ValueError:
            print("ValueError: Please Input a number between 1 - 5. Try again. \n")


def snack_wrap():
    
    global cart

    while True:

        try:

            print("********* SNACK WRAP MENU ***********")
            print("   ITEMS          |       RATE   ")
            
            print("1. Ranch Snack    |              ")
            print("   Wrap           |      INR. 110")
            print("2. Spicy Snack    |              ")
            print("   Wrap           |      INR. 120")
            print("              3. Back            ")
            print("*********************************")

            snack_wrap_user = int(input("Choose your Wrap: "))

            if snack_wrap_user == 1:
                    name ="Ranch Snack Wrap"
                    price = 110
                    quantity = int(input("Quantity: "))
                    total_bur = price * quantity
                    cart.append((name, quantity, price, total_bur))
                    print(f"Your total price for {quantity} {name}: INR. {total_bur} ")

            elif snack_wrap_user == 2:
                name ="Spicy Snack Wrap"
                price = 120
                quantity = int(input("Quantity: "))
                total_bur = price * quantity
                cart.append((name, quantity, price, total_bur))
                print(f"Your total price for {quantity} {name}: INR. {total_bur} ")

        
            elif snack_wrap_user == 3:
                print("Going back to the Main Menu")
                print("***************************\n")
                break

            else:
                print("Invalid operation. Try again.")
                print("****************************\n")
                continue
                

            choice = input("Do you want to add more (Y/N): ")
            if choice != "y":
                print("********************************\n")
                break

        except ValueError:
            print("ValueError: Please Input a number between 1 - 5. Try again. \n")

def remove():

    global cart

    view()
    
    # for item in cart()    
    #     remove_user = int(input("Which items do you want to remove: "))
    #     cart.remove(remove_user)



def view():

    global cart

    try:

        print("********* YOUR ORDER ***********\n")
        print(cart)
        for item in cart:
            print("Item:", item[0])
            print("Quantity:", item[1])
            print("Price: INR.", item[2])
            print("Total price: INR.", item[3])
            print("**************************\n")

    except ValueError:
        print("ValueError: Please Input a number between 1 - 5. Try again. \n")

        
def checkout():

    total = 0
    
    print("********* BILL SUMMARY ***********\n")
    
    print("Item",    "      |",  "Quantity",  "     |",  "Price",  "        |",  "Total Price")
    for item in cart:
        total += item[3]
        print( item[0],  "      |",    item[1],   "     |",  item[2],  "        |",     item[3])

    print(f"Your Total Bill: INR. {total}\n")

    gst = total * 0.06
    grand_total = total + gst

    print(f"GST 6%: INR. {gst:.2f}\n")
    print(f"Grand Total: INR. {grand_total}\n")
    print("Thank you. Please visit again.\n")

    


main_menu()

# print(cart)

# with open("mac.csv","a",newline="") as file:
#     writer = csv.writer(file)  
#     writer.writerow(["Item:"  ,     "Quantity:"  ,    "Price:"     ,  "Total Price"])
#     writer.writerows(cart)
#     # for item  in cart:
#     #     print("\nItem:", item[0])
#     #     print("Quantity:", item[1])
#     #     print("Price: INR.", item[2])
#     #     print("Total price: INR.", item[3])
#     #     print("**************************\n")

