from db.run_sql import run_sql

from models.manufacturer import Manufacturer

def save(manufacturer):
    sql = "INSERT INTO manufacturers (name, address, phone_number, product_list) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [manufacturer.name, manufacturer.address, manufacturer.phone_number, manufacturer.product_list]
    results = run_sql(sql, values)
    manufacturer.id = results[0]['id']
    return manufacturer

def select_all():
    manufacturers = []

    sql = "SELECT * FROM manufacturers"
    results = run_sql(sql)

    for row in results:
        manufacturer = Manufacturer(row['name'], row['address'], row['phone_number'], row['product_list'], row['id'])
        manufacturers.append(manufacturer)
    return manufacturers


def select(id):
    sql = "SELECT * FROM manufacturers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    manufacturer = Manufacturer(result['name'], result['address'], result['phone_number'], result['product_list'], result['id'])
    return manufacturer

def delete_all():
    sql = "DELETE  FROM manufacturers"
    run_sql(sql)



