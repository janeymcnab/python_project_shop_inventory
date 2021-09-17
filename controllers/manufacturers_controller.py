from itertools import product
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.manufacturer import Manufacturer
from models.product import Product
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

@manufacturers_blueprint.route("/manufacturers/new", methods=['GET'])
def new_manufacturer():
    manufacturers = manufacturer_repository.select_all()
    return render_template("manufacturers/new.html", manufacturers = manufacturers)

# CREATE
# POST '/manufacturers'

@manufacturers_blueprint.route("/manufacturers", methods=["POST"])
def create_manufacturer():
    name = request.form["name"]
    address = request.form["address"]
    phone_number = request.form["phone_number"]
    product_list = request.form ["product_list"]
    new_manufacturer = Manufacturer(name, address, phone_number, product_list)
    manufacturer_repository.save(new_manufacturer)     
    return redirect("/manufacturers")


# SHOW
# GET '/manufacturers/<id>'

@manufacturers_blueprint.route("/manufacturers/<id>", methods=['GET'])
def show_manufacturer(id):
    manufacturer = manufacturer_repository.select(id)
    return render_template('manufacturers/show.html', manufacturer = manufacturer)


# EDIT
# GET '/manufacturers/<id>/edit'
@manufacturers_blueprint.route("/manufacturers/<id>/edit", methods=['GET'])
def edit_manufacturer(id):
    manufacturer = manufacturer_repository.select(id)
    return render_template('manufacturers/edit.html', manufacturer=manufacturer)

# UPDATE
# PUT '/manufacturers/<id>'
@manufacturers_blueprint.route("/manufacturers/<id>", methods=['POST'])
def update_manufacturer(id):
    name = request.form["name"]
    address = request.form["address"]
    phone_number = request.form["phone_number"]
    product_list = request.form ["product_list"]
    manufacturer = Manufacturer(name, address, phone_number, product_list, id)
    manufacturer_repository.update(manufacturer)
    return redirect("/manufacturers")

# DELETE
# DELETE '/manufacturers/<id>'
@manufacturers_blueprint.route("/manufacturers/<id>/delete", methods=['POST'])
def delete_manufacturer(id):
    manufacturer_repository.delete(id)
    return redirect("/manufacturers")
