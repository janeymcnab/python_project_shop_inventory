from models.product import Product


class Manufacturer:

    def __init__(self, name, address, phone_number, product_list, id = None):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.product_list = product_list
        self.id = id

      
