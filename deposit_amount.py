import bank_vault
def deposit_money():
    amount = int(input("Enter amount to deposit: "))
    bank_vault.balance += amount
    print("Amount deposited successfully.")