def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        print("You logged in success!!! ==== Welcome to iShop")
        return showMenu()
    else:
        print("You logged in FAILED!!! ==== Please try again.")
        return login()

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    return menuSelect()

def menuSelect():
    userSelected = int(input(">>"))
    if userSelected == 1:
        price = int(input("Please key your price :"))
        return vatCalculator(price)
    elif userSelected == 2:
        return priceCalculator()
    else:
        print("Please Select Menu 1 or 2 ONLY")
        return menuSelect()

def vatCalculator(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return print("Total Price including VAT is :",result)

def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculator(price1 + price2)


login()

