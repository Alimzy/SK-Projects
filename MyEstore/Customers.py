from Estore.Users import Users
from Estore.BillingInformation import BillingInformation
from Estore.ShoppingCart import ShoppingCart
class Customers(Users):
    def __init__(self,name,age,email_address,password,phone,city_name,country_name,house_number,street,state):
        super().__init__(name, age, email_address, password, phone,city_name,country_name,house_number,street,state)
        self.billingInformation = BillingInformation(phone,name,city_name,country_name,house_number,street,state)
        self.shoppingCart = ShoppingCart()






