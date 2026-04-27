def authentication():
    print("Welcome to CGC Bank")
    username = input("Enter your Bank Id :")
    password= input("Enter your pin :")

    if username=="admin" and password == "123" :
        print("Login Successful")
        return  True
    else: 
        print("Failed attempt")
        return False
