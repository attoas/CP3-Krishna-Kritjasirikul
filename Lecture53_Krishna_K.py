def vatCalculate(totalPrice):
    result = (totalPrice + (totalPrice*7/100))
    return result

price = int(input("Please key your price :",))
print("Your price including vat is :",vatCalculate(price))