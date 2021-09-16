from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.manufacturer import Manufacturer
import repositories.manufacturer_repository as manufacturer_repository

manufacturers_blueprint = Blueprint("manufacturers", __name__)


# INDEX
# GET '/manufacturers'
@manufacturers_blueprint.route('/manufacturers')
def manufacturers():
    manufacturers = manufacturer_repository.select_all()
    return render_template('manufacturers/index.html', manufacturers = manufacturers)

# NEW
# GET '/manufacturers/new'

# CREATE
# POST '/manufacturers'

# SHOW
# GET '/manufacturers/<id>'

# EDIT
# GET '/manufacturers/<id>/edit'

# UPDATE
# PUT '/manufacturers/<id>'

# DELETE
# DELETE '/manufacturers/<id>'