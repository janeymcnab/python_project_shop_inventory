import unittest
from models.product import *

class TestProduct(unittest.TestCase):
    def setUp(self):
        self.product1 = Product('Alp Blossom', 'Semi-hard Cheese. Nutty, floral and sweet. Unpasteurised.', 1000, 2.50, 5.00, 'Austria')
        self.product2 = Product('Auld Reekie', 'Hard Smoked Cheese. Smoked over Whiskey. Unpasteurised.', 5000, 2.00, 4.50, 'Scotland')
        self.product3 = Product('Gouda', 'Nutty, creamy with salt crystallisation. Pasteurised', 3000, 2.40, 5.50, 'Scotland')
        self.product4 = Product('Brie de Meux', 'Soft and creamy cheese. Unpasteurised.', 0, 3.00, 6.00, 'France')
        self.product5 = Product('Comte', 'Aged for 22 months. Nutty and creamy hard cheese. Unpasteurised', 2000, 5.00, 8.00, 'France')
        self.product6 = Product('Campoveja Trufado', 'Hard cheese with a delicate truffle flavour. Unpasteurised', 500, 3.00, 5.50, 'Spain')
        self.product7 = Product('Blue Stilton', 'Creamy texture with mellow aromatic finish. Pasteurised', 3500, 2.00, 4.00, 'England')

    
    def test_product_has_name(self):
        self.assertEqual('Alp Blossom', self.product1.name)
    
    def test_product_origin(self):
        self.assertEqual('France', self.product4.origin)
    
    # def test_low_stock(self):
    #     self.assertEqual("Campoveja Trufado is low in stock!", self.product6.stock_level_check())

    # def test_low_stock_false(self):
    #     self.assertFalse(self.product7.stock_level_check())

    # def test_out_of_stock(self):
    #     self.assertEqual("Brie de Meux is out of stock!", self.product4.stock_level_check())
    
    # def test_out_of_stock_false(self):
    #     self.assertFalse(self.product3.stock_level_check())

    


    