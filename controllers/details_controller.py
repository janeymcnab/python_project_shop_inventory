
from controllers.manufacturers_controller import manufacturers
from controllers.products_controller import products
from flask import Blueprint, Flask, redirect, render_template, request

from models.detail import Detail
from models.product import Product
from models.manufacturer import Manufacturer

import repositories.product_repository as product_repository
import repositories.manufacturer_repository as manufacturer_repository
import repositories.detail_repository as detail_repository

details_blueprint = Blueprint("details", __name__)

# INDEX
@details_blueprint.route("/details")
def details():
    details = detail_repository.select_all()
    product = product_repository.select_all()
    manufacturer = manufacturer_repository.select_all()
    return render_template ('details/index.html', details = details, product = product, manufacturer = manufacturer)
