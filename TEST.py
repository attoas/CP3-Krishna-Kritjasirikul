def login():
    usernameInput = input("Username :")
    passwordInput = input("Password :")
    if usernameInput == "admin" and passwordInput == "1234":
        return showMenu()
    else:
        print('Password incorrect Please try again :-(')
        return login()


def showMenu():
    print("Done !")
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    return menuSelect()


def menuSelect():
    userSelected = int(input(">>"))
    if userSelected == 1:
        print('<-----Program Vat Calculater ----->')
        priceVatCal = int(input('Input Price For VatCalculate : '))
        return vatCalculate(priceVatCal)
    elif userSelected == 2:
        return priceCaluclate()
    else:
        print('Please Select Manu 1 or 2')
        return menuSelect()


def vatCalculate(price):
    vat = 7
    result = price + (price * vat / 100)
    #print(result)
    return result


def priceCaluclate():
    print('<-----Program Price Calculater ----->')
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    # print(price1 + price2)
    return vatCalculate(price1 + price2)


print(login())