# Solo Python Project - Shop Inventory

### A inventory system to track individual products and manufacturers. This was a solo project built over 7 days during my 11th week of the Part-Time Software Development Course at CodeClan.

### MVP
* The inventory should track individual products, including a name, description, stock quantity, buying cost, and selling price.
* The inventory should track manufacturers, including a name and any other appropriate details.
* The shop can sell anything you like, but you should be able to create and edit manufacturers and products separately.
* Show an inventory page, listing all the details for all the products in stock in a single view.
* As well as showing stock quantity as a number, the app should visually highlight "low stock" and "out of stock" items to the user.
### My Extensions
* A markup percentage calculator
* Two product filters
* A bargraph responsive to changing data 

### Prerequisits

The technologies used in this project:

* python  
* Flask  
* PostgreSQL  
* psycopg2    
* HTML
* CSS  


To run first install the following:
Enter the following commands into your terminal:

* pip3 install psycopg2
* pip3 install Flask
* pip3 install python-dotenv


Clone the repository to your own directory:
git clone git@github.com:janeymcnab/python_project_shop_inventory.git

Create the database by entering the following command in the console:
* createdb products_manufacturers

From the cloned repository, run the following command in the terminal:
* psql -d products_manufacturers -f products_manufacturers.sql

In the terminal run the following command to populate:
* python3 console.py

Make sure you are in the correct directory and then run the following command in the terminal:
* flask run

Open your browser and enter the following URL: http://localhost:5000/
