from Estore.Address import Address
class BillingInformation:

    def __init__ (self, phone_number, name, city_name, country_name,house_number,street, state):
        self.__phone_number = phone_number
        self.__name = name
        self.__address = Address(city_name, country_name, house_number, street, state)