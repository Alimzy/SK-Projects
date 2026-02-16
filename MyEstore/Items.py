from Estore.alimzyEstore.Product import Product

class Items:

    def __init__(self,id,name,price,description,category, quantity_of_product):
        self.product = Product(id,name,price,description,category)
        self.quantityOfProduct = quantity_of_product
