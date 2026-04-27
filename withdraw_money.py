import bank_vault
def withdraw_money():
    amount = int(input("Enter amount to withdraw: "))
    if amount <= bank_vault.balance:
        bank_vault.balance -= amount
        print("Please collect your cash.")
    else:
        print("Opps! You have Insufficient balance.")