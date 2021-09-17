from db.run_sql import run_sql
from models.detail import Detail
from models.product import Product
from models.manufacturer import Manufacturer
import repositories.manufacturer_repository as manufacturer_repository
import repositories.product_repository as product_repository

def save(detail):
    sql = "INSERT INTO details (product_id, manufacturer_id) VALUES (%s, %s) RETURNING id"
    values =[detail.product.id, detail.manufacturer.id]

    results = run_sql(sql, values)
    id = results [0]["id"]
    detail.id = id


def select_all():
    details = []

    sql = "SELECT * FROM details"
    results = run_sql(sql)
    for row in results:
        product = product_repository.select(row['product_id'])
        manufacturer = manufacturer_repository.select(row['manufacturer_id'])
        detail = detail(product, manufacturer, row['id'])
        details.append(detail)
    return details

def select(id):
    sql = "SELECT * FROM details WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    manufacturer = manufacturer_repository.select(result["manufacturer_id"])
    product = product_repository.select(result["product_id"])
    detail = Detail(product, manufacturer, result["id"])
    return detail

def delete_all():
    sql = "DELETE  FROM details"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM details WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(detail):
    sql = "UPDATE details SET (product_id, manufacturer_id) = (%s, %s) WHERE id = %s"
    values = [detail.product.id, detail.manufacturer.id, detail.id]
    run_sql(sql, values)
 
