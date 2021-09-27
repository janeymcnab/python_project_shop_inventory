
DROP TABLE products;
DROP TABLE manufacturers;


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
    category VARCHAR,
    milk_type VARCHAR,
    stock_quantity INT,
    buying_cost INT,
    selling_price INT,
    origin VARCHAR(255) NOT NULL,
    manufacturer_id INT REFERENCES manufacturers(id) ON DELETE CASCADE
);



