from flask import Flask, render_template

# Controllers go here -
# from controllers.name_controller import names_blueprint
from controllers.manufacturers_controller import manufacturers_blueprint
from controllers.products_controller import products_blueprint
from controllers.filters_controller import filters_blueprint 


app = Flask(__name__)

# app goes here -
# app.register(names_blueprint)
app.register_blueprint(manufacturers_blueprint)
app.register_blueprint(products_blueprint)
app.register_blueprint(filters_blueprint)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)