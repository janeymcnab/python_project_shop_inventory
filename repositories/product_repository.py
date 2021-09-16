from db.run_sql import run_sql

from models.product import Product
from models.manufacturer import Manufacturer

import repositories.manufacturer_repository as manufacturer_repository

def save(product):
    sql = "INSERT INTO products (name, description, stock_quantity, buying_cost, selling_price, origin, manufacturer_id) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id"
    values = [product.name, product.description, product.stock_quantity, product.buying_cost, product.selling_price, product.origin, product.manufacturer.id]
    results = run_sql(sql, values)
    product.id = results[0]['id']
    return product

def delete_all():
    sql = "DELETE  FROM products"
    run_sql(sql)