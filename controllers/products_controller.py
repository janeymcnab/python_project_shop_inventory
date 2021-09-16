from controllers.manufacturers_controller import manufacturers
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.product import Product
from models.manufacturer import Manufacturer
import repositories.manufacturer_repository as manufacturer_repository
import repositories.product_repository as product_repository


products_blueprint = Blueprint("products", __name__)

# INDEX
# GET '/products'
@products_blueprint.route('/products')
def products():
    products = product_repository.select_all()
    manufacturer = manufacturer_repository.select_all()
    return render_template('products/index.html', products = products, manufacturer = manufacturer)




# NEW
# GET '/products/new'

# CREATE
# POST '/products'

# SHOW
# GET '/products/<id>'

@products_blueprint.route('/products/<id>', methods=['GET'])
def show_product(id):
    product = product_repository.select(id)
    return render_template('products/index.html', product = product)


# EDIT
# GET '/products/<id>/edit'

# UPDATE
# PUT '/products/<id>'

# DELETE
# DELETE '/products/<id>'