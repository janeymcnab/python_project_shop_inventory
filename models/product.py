class Product:
    def __init__(self, name, description, stock_quantity, buying_cost, selling_price, origin, id = None):
        self.name = name
        self.description = description
        self.stock_quantity = stock_quantity
        self.buying_cost = buying_cost
        self.selling_price = selling_price
        self.origin = origin
        self.id = id


    def stock_level_check(self):
        out_of_stock = False
        low_stock = False

        if self.stock_quantity <= 10:
            out_of_stock = True
            return f"{self.name} is out of stock!"
        elif self.stock_quantity <= 500:
            low_stock = True
            return f"{self.name} is low in stock!"

    
    
    

        
