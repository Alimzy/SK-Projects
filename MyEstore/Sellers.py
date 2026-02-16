from Estore.Users import Users


class Sellers(Users):
    def __init__(self, name, age, email_address,password,phone,city_name, country_name,house_number,street, state):
        super().__init__(name, age, email_address, password, phone,city_name, country_name,house_number,street, state)