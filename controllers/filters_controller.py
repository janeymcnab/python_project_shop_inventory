from itertools import product
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.product import Product
from models.manufacturer import Manufacturer
import repositories.manufacturer_repository as manufacturer_repository
import repositories.product_repository as product_repository
from controllers.manufacturers_controller import Manufacturer
from controllers.products_controller import Product

filters_blueprint = Blueprint("filters", __name__)

@filters_blueprint.route('/filters')
def filters():
    return render_template("products/filter.html")

@filters_blueprint.route('/results/<cheese_type>', methods=["GET"])
def filter_results(cheese_type):
    products = product_repository.select_all()
    return render_template("products/results.html", cheese_type = cheese_type, products = products)

@filters_blueprint.route('/results/perform_filter', methods=["POST"])
def perform_filter():
    cheese_type = request.form['cheese_type']
    url = "/results/"+cheese_type
    return redirect(url)


@filters_blueprint.route('/milk_type_results/<milk_type>', methods=["GET"])
def milk_filter_results(milk_type):
    products = product_repository.select_all()
    return render_template("products/milk_type_results.html", milk_type = milk_type, products = products)

@filters_blueprint.route('/results/milk_perform_filter', methods=["POST"])
def milk_perform_filter():
    milk_type = request.form['milk_type']
    url = "/milk_type_results/"+milk_type
    return redirect(url)

