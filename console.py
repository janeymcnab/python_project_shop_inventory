import pdb 

from models.product import *
import repositories.product_repository as product_repository

from models.manufacturer import Manufacturer
import repositories.manufacturer_repository as manufacturer_repository

from models.detail import Detail
import repositories.detail_repository as detail_repository

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




product1 = Product('Alp Blossom', 'Semi-hard Cheese. Nutty, floral and sweet. Unpasteurised.', 1000, 2.50, 5.00, 'Austria', manufacturer4)
product_repository.save(product1)

product2 = Product('Auld Reekie', 'Hard Smoked Cheese. Smoked over Whiskey. Unpasteurised.', 5000, 2.00, 4.50, 'Scotland', manufacturer1)
product_repository.save(product2)

product3 = Product('Gouda', 'Nutty, creamy with salt crystallisation. Pasteurised', 3000, 2.40, 5.50, 'Scotland', manufacturer1)
product_repository.save(product3)

product4 = Product('Brie de Meux', 'Soft and creamy cheese. Unpasteurised.', 0, 3.00, 6.00, 'France', manufacturer5)
product_repository.save(product4)

product5 = Product('Comte', 'Aged for 22 months. Nutty and creamy hard cheese. Unpasteurised', 2000, 5.00, 8.00, 'France', manufacturer5)
product_repository.save(product5)

product6 = Product('Campoveja Trufado', 'Hard cheese with a delicate truffle flavour. Unpasteurised', 500, 3.00, 5.50, 'Spain', manufacturer3)
product_repository.save(product6)

product7 = Product('Blue Stilton', 'Creamy texture with mellow aromatic finish. Pasteurised', 3500, 2.00, 4.00, 'England', manufacturer2)
product_repository.save(product7)


detail1 = Detail(product1, manufacturer4)
detail_repository.save(detail1)

detail2 = Detail(product2, manufacturer1)
detail_repository.save(detail2)

detail3 = Detail(product3, manufacturer1)
detail_repository.save(detail3)

detail4 = Detail(product4, manufacturer5)
detail_repository.save(detail4)

detail5 = Detail(product5, manufacturer5)
detail_repository.save(detail5)

detail6 = Detail(product5, manufacturer3)
detail_repository.save(detail6)

detail7 = Detail(product7, manufacturer2)
detail_repository.save(detail7)
    

# print(product4.stock_level_check())
# print(product6.stock_level_check())


pdb.set_trace()