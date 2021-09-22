import unittest
from models.product import *

class TestProduct(unittest.TestCase):
    def setUp(self):
        self.product1 = Product('Alp Blossom', 'Semi-hard Cheese. Nutty, floral and sweet', 'Unpasteurised.','Cow', 1000, 2.50, 5.00, 'Austria', 'Volaberg & Mapp')
        self.product2 = Product('Auld Reekie', 'Hard Smoked Cheese. Smoked over Whiskey', 'Unpasteurised.', 'Cow', 5000, 2.00, 4.50, 'Scotland', 'McNabb and Collie')
        self.product3 = Product('Gouda', 'Nutty, creamy with salt crystallisation', 'Pasteurised', 'Cow', 500, 2.40, 5.50, 'Scotland', 'McNabb and Collie')
        self.product4 = Product('Brie de Meux', 'Soft and creamy cheese', 'Unpasteurised.','Cow', 1700, 3.00, 6.00, 'France', 'Haute - Loire')
        self.product5 = Product('Comte', 'Aged for 22 months. Nutty and creamy hard cheese', 'Unpasteurised', 'Cow', 0, 5.00, 8.00, 'France', 'Haute - Loire')
        self.product6 = Product('Campoveja Trufado', 'Hard cheese with a delicate truffle flavour', 'Unpasteurised', 'Sheep', 2500, 3.00, 5.50, 'Spain', 'Villamayor de Calatravo')
        self.product7 = Product('Blue Stilton', 'Creamy texture with mellow aromatic finish', 'Pasteurised', 'Cow', 3500, 2.00, 4.00, 'England', 'Colsten Wynd')

    
    def test_product_has_name(self):
        self.assertEqual('Alp Blossom', self.product1.name)
    
    def test_product_origin(self):
        self.assertEqual('France', self.product4.origin)


    def test_check_if_low(self):
        self.assertFalse(self.product1.check_if_low())

    def test_decrease_stock(self):
        self.assertEqual(None, self.product5.decrease_stock(100))