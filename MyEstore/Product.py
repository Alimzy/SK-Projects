from Estore.ProductCategory import ProductCategory

class Product:
    def __init__(self,id,name,price,description,category:ProductCategory):
        self.id = id
        self.name = name,
        self.price = price,
        self.description = description,
        self.category = category