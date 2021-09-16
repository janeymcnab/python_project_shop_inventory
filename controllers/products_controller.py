from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.product import Product
import repositories.product_repository as product_repository

products_blueprint = Blueprint("products", __name__)

# INDEX
# GET '/products'

# NEW
# GET '/products/new'

# CREATE
# POST '/products'

# SHOW
# GET '/products/<id>'

# EDIT
# GET '/products/<id>/edit'

# UPDATE
# PUT '/products/<id>'

# DELETE
# DELETE '/products/<id>'