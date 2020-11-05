class Customer:
    name = ""
    lastname = ""
    age = ""

    def addCart(self):
        print("Added product to " + self.name + " " + self.lastname + "'s Cart")

customer1 = Customer()
customer1.name = "Krishna"
customer1.lastname = "Kritjasirikul"
customer1.addCart()

customer2 = Customer()
customer2.name = "Peter"
customer2.lastname = "Plotter"
customer2.addCart()

customer3 = Customer()
customer3.name = "Helvica"
customer3.lastname = "Sophos"
customer3.addCart()

