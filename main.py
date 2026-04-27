from authentication import authentication
from display_amount import display_money
from deposit_amount import deposit_money
from withdraw_money import withdraw_money


def menu():
    while True:
        print("Welcome to Bank Of CGC")  
        print("ATM Services")
        print("1. Display Money")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")


        choice = int(input("Enter Here: "))

        if choice == 1:
            display_money()
        elif choice == 2:
            deposit_money()
        elif choice == 3:
            withdraw_money()
        elif choice == 4:
            print("Thank you for visiting.")
            break
        else:
            print("ERROR!!! Enter a valid option")

if authentication():
    menu()