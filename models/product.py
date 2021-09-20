class Product:
    def __init__(self, name, description, category, milk_type, stock_quantity, buying_cost, selling_price, origin, manufacturer, id = None):
        self.name = name
        self.description = description
        self.stock_quantity = stock_quantity
        self.category = category
        self.milk_type = milk_type
        self.buying_cost = buying_cost
        self.selling_price = selling_price
        self.origin = origin
        self.manufacturer = manufacturer
        self.id = id


    def check_if_low(self):
        if self.stock_quantity > 10 and self.stock_quantity <= 500:
            return True
        else:
            return False

    def check_if_out(self):
        if self.stock_quantity <= 10:
            return True
        else:
            return False

    def decrease_stock(self, bought_amount):
        if self.stock_quantity >= bought_amount:
            self.stock_quantity -= bought_amount



    
    # def stock_level_check(self):
    #     out_of_stock = False
    #     low_stock = False

    #     if self.stock_quantity <= 10:
    #         out_of_stock = True
    #         # return f"{self.name} is out of stock!"
    #     elif self.stock_quantity <= 500:
    #         low_stock = True
    #         # return f"{self.name} is low in stock!"





    
    
    

        

