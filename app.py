from flask import Flask, render_template
from datetime import date, datetime 

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
    now = datetime.now()
    date_time = now.strftime("%d/%m/%Y, %H:%M")
    return render_template('index.html', date_time=date_time)

if __name__ == '__main__':
    app.run(debug=True)