DROP TABLE IF EXISTS details;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS manufacturers;

CREATE TABLE manufacturers(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    phone_number VARCHAR(255) NOT NULL,
    product_list VARCHAR(255) NOT NULL
);

CREATE TABLE products(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description VARCHAR(255) NOT NULL,
    stock_quantity INT,
    buying_cost INT,
    selling_price INT,
    origin VARCHAR(255) NOT NULL,
    manufacturer_id INT REFERENCES manufacturers(id) ON DELETE CASCADE
);

CREATE TABLE details(
    id SERIAL PRIMARY KEY,
    product_id INT REFERENCES products(id),
    manufacturer_id INT REFERENCES manufacturers(id)
);

INSERT INTO manufacturers (name, address, phone_number, product_list) VALUES ('McNabb and Collie', 'The Cow Shed, Achiltibuie', '01899 220 8989', 'Gouda, Auld Reekie');
INSERT INTO manufacturers (name, address, phone_number, product_list) VALUES ('Colsten Wynd', 'Basset Farms, Derbyshire', '01299 567 8989', 'Blue Stilton');
INSERT INTO manufacturers (name, address, phone_number, product_list) VALUES ('Villamayor de Calatravo', 'San Lorenzo, Toledo', '(+34) 6767 978', 'Campoveja Trufado');
INSERT INTO manufacturers (name, address, phone_number, product_list) VALUES ('Volaberg & Mapp', 'Volaberg & Mapp, Klagenfurter Strasse', '(+43) 7878 39787', 'Alp Blossom');
INSERT INTO manufacturers (name, address, phone_number, product_list) VALUES ('Haute - Loire', 'Farmier de Roque, Libourne', '(+33) 787687 90', 'Brie de Meux, Comte');


INSERT INTO products (name, description, stock_quantity, buying_cost, selling_price, origin, manufacturer_id) VALUES ('Alp Blossom', 'Semi-hard Cheese. Nutty, floral and sweet. Unpasteurised.', 1000, 2.50, 5.00, 'Austria', 4);
INSERT INTO products (name, description, stock_quantity, buying_cost, selling_price, origin, manufacturer_id) VALUES ('Auld Reekie', 'Hard Smoked Cheese. Smoked over Whiskey. Unpasteurised.', 5000, 2.00, 4.50, 'Scotland', 1);
INSERT INTO products (name, description, stock_quantity, buying_cost, selling_price, origin, manufacturer_id) VALUES ('Gouda', 'Nutty, creamy with salt crystallisation. Pasteurised', 3000, 2.40, 5.50, 'Scotland', 1);
INSERT INTO products (name, description, stock_quantity, buying_cost, selling_price, origin, manufacturer_id) VALUES ('Brie de Meux', 'Soft and creamy cheese. Unpasteurised.', 0, 3.00, 6.00, 'France', 5);
INSERT INTO products (name, description, stock_quantity, buying_cost, selling_price, origin, manufacturer_id) VALUES ('Comte', 'Aged for 22 months. Nutty and creamy hard cheese. Unpasteurised', 2000, 5.00, 8.00, 'France', 5);
INSERT INTO products (name, description, stock_quantity, buying_cost, selling_price, origin, manufacturer_id) VALUES ('Campoveja Trufado', 'Hard cheese with a delicate truffle flavour. Unpasteurised', 500, 3.00, 5.50, 'Spain', 3);
INSERT INTO products (name, description, stock_quantity, buying_cost, selling_price, origin, manufacturer_id) VALUES ('Blue Stilton', 'Creamy texture with mellow aromatic finish. Pasteurised', 3500, 2.00, 4.00, 'England', 2);
