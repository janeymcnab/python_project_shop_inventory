from db.run_sql import run_sql

from models.manufacturer import Manufacturer

def save(manufacturer):
    sql = "INSERT INTO manufacturers (name, address, phone_number, product_list) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [manufacturer.name, manufacturer.address, manufacturer.phone_number, manufacturer.product_list]
    results = run_sql(sql, values)
    manufacturer.id = results[0]['id']
    return manufacturer

def delete_all():
    sql = "DELETE  FROM manufacturers"
    run_sql(sql)

