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

@manufacturers_blueprint.route("/manufacturers/new")
def new_manufacturer():
    manufacturer = manufacturer_repository.select_all()
    return render_template("manufacturers/new.html", manufacturer = manufacturer)

# CREATE
# POST '/manufacturers'

@manufacturers_blueprint.route("/manufacturers", methods=["POST"])
def create_manufacturer():
    name = request.form["name"]
    address = request.form["address"]
    phone_number = request.form["phone_number"]
    new_manufacturer = Manufacturer(name, address, phone_number)
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
@manufacturers_blueprint.route("/manufacturers/<id>/edit")
def edit_manufacturer(id):
    manufacturer = manufacturer_repository.select(id)
    manufacturer = manufacturer_repository.select_all()
    return render_template('manufacturers/edit.html', manufacturer=manufacturer)

# UPDATE
# PUT '/manufacturers/<id>'
@manufacturers_blueprint.route("/manufacturers/<id>", methods=["POST"])
def update_manufacturer(id):
    name = request.form["name"]
    address = request.form["address"]
    phone_number = request.form["phone_number"]
    manufacturer = Manufacturer(name, address, phone_number)
    manufacturer_repository.update(manufacturer)
    return redirect("/manufacturers")

# DELETE
# DELETE '/manufacturers/<id>'
@manufacturers_blueprint.route("/manufacturers/<id>/delete", methods=["POST"])
def delete_manufacturer(id):
    manufacturer_repository.delete(id)
    return redirect("/manufacturers")
