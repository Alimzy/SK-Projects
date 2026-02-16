from Estore.Address import Address
class Users:

    def __init__(self,name, age, email_address, password, phone,city_name,country_name,house_number,street,state):

        self.__name = name
        self.__age = age
        self.__address = Address(city_name,country_name,house_number,street,state)
        self.__email_address = email_address
        self.__password = password
        self.__phone = phone

