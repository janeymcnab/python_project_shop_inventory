import pdb 

from models.product import *
import repositories.product_repository as product_repository

from models.manufacturer import Manufacturer
import repositories.manufacturer_repository as manufacturer_repository

product_repository.delete_all()
manufacturer_repository.delete_all()

manufacturer1 = Manufacturer('McNabb and Collie', 'The Cow Shed, Achiltibuie', '01899 220 8989', 'Gouda, Auld Reekie')
manufacturer_repository.save(manufacturer1)

manufacturer2 = Manufacturer('Colsten Wynd', 'Basset Farms, Derbyshire', '01299 567 8989', 'Blue Stilton')
manufacturer_repository.save(manufacturer2)

manufacturer3 = Manufacturer('Villamayor de Calatravo', 'San Lorenzo, Toledo', '(+34) 6767 978', 'Campoveja Trufado')
manufacturer_repository.save(manufacturer3)

manufacturer4 = Manufacturer('Volaberg & Mapp', 'Volaberg & Mapp, Klagenfurter Strasse', '(+43) 7878 39787', 'Alp Blossom')
manufacturer_repository.save(manufacturer4)

manufacturer5 = Manufacturer('Haute - Loire', 'Farmier de Roque, Libourne', '(+33) 787687 90', 'Brie de Meux, Comte')
manufacturer_repository.save(manufacturer5)




product1 = Product('Alp Blossom', 'Semi-hard Cheese. Nutty, floral and sweet', 'Unpasteurised','Cow', 1000, 2.50, 5.00, 'Austria', manufacturer4)
product_repository.save(product1)

product2 = Product('Auld Reekie', 'Hard Smoked Cheese. Smoked over Whiskey.', 'Unpasteurised', 'Cow', 5000, 2.00, 4.50, 'Scotland', manufacturer1)
product_repository.save(product2)

product3 = Product('Gouda', 'Nutty, creamy with salt crystallisation.', 'Pasteurised','Cow', 3000, 2.40, 5.50, 'Scotland', manufacturer1)
product_repository.save(product3)

product4 = Product('Brie de Meux', 'Soft and creamy cheese.', 'Unpasteurised', 'Cow', 0, 3.00, 6.00, 'France', manufacturer5)
product_repository.save(product4)

product5 = Product('Comte', 'Aged for 22 months. Nutty and creamy hard cheese.', 'Unpasteurised', 'Cow', 2000, 5.00, 8.00, 'France', manufacturer5)
product_repository.save(product5)

product6 = Product('Campoveja Trufado', 'Hard cheese with a delicate truffle flavour.', 'Unpasteurised', 'Sheep', 500, 3.00, 5.50, 'Spain', manufacturer3)
product_repository.save(product6)

product7 = Product('Blue Stilton', 'Creamy texture with mellow aromatic finish.', 'Pasteurised', 'Cow', 3500, 2.00, 4.00, 'England', manufacturer2)
product_repository.save(product7)


# print(product4.stock_level_check())
# print(product6.stock_level_check())


pdb.set_trace()