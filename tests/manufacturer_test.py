import unittest
from models.manufacturer import *

class TestManufacturer(unittest.TestCase):
    def setUp(self):
        product_list1 = ['Gouda', 'Auld Reekie']
        product_list2 = ['Blue Stilton']
        product_list3 = ['Campoveja Trufado']
        product_list4 = ['Alp Blossom']
        product_list5 = ['Brie de Meux', 'Comte']

        self.manufacturer1 = Manufacturer('McNabb and Collie', 'The Cow Shed, Achiltibuie', '01899 220 8989', product_list1)
        self.manufacturer2 = Manufacturer('Colsten Wynd', 'Basset Farms, Derbyshire', '01299 567 8989', product_list2 )
        self.manufacturer3 = Manufacturer('Villamayor de Calatravo', 'San Lorenzo, Toledo', '(+34) 6767 978', product_list3)
        self.manufacturer4 = Manufacturer('Volaberg & Mapp', 'Volaberg & Mapp, Klagenfurter Strasse', '(+43) 7878 39787', product_list4)
        self.manufacturer5 = Manufacturer('Haute - Loire', 'Farmier de Roque, Libourne', '(+33) 787687 90', product_list5)

    def test_manufacturer_name(self):
        self.assertEqual('McNabb and Collie', self.manufacturer1.name)
    
    def test_product_list(self):
        self.assertEqual(['Alp Blossom'], self.manufacturer4.product_list)
    
    def test_manufacturer(self):
        self.assertEqual('Basset Farms, Derbyshire', self.manufacturer2.address)
    
    