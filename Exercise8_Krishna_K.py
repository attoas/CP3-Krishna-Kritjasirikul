usernameInput = input("Username :")
passwordInput = input("Password :")
if usernameInput == "Shopee" and passwordInput == "4321":
    print("----- Welcome to Shopee -----")
    print("----- PET LOVER - DOGGY  -----")
    product1 = "Zerra 40 Gram (Box) | 100 Bath/Box"
    product2 = "JerryHihg Milk | 50 Bath/Pack"
    product3 = "Gum Stickky | 70 Bath/Pack"
    product4 = "Gummy Chewing | 65 Bath/Pack"
    product5 = "Teeth Brusher | 150 Bath/Pack"
    print("Item 1 : " + product1)
    print("Item 2 : " + product2)
    print("Item 3 : " + product3)
    print("Item 4 : " + product4)
    print("Item 5 : " + product5)

    userSelected = int(input("Please select an Items >>"))
    if userSelected == 1:
        SelectProduct = product1
        Price = 100
    if userSelected == 2:
       SelectProduct = product2
       Price = 50
    if userSelected == 3:
       SelectProduct = product3
       Price = 70
    if userSelected == 4:
       SelectProduct = product4
       Price = 65
    if userSelected == 5:
       SelectProduct = product5
       Price = 150
    print("Your order :" + SelectProduct)
    userAmount = input("How many do you want? : ")
    print("Your Order is : " + SelectProduct + "Amount : " + userAmount + " ea")
    print("Totally price : " + str(Price*int(userAmount)) + " Bahts")
else:
    print("Your login Failed")