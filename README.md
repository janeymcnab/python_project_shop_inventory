The technologies used in this project:
python  
FLASK   
POSTGRESQL  
psycopg2    
HTML/CSS    
jinja


To run first install the following:
Enter the following commands into your terminal
pip install psycopg2
pip install FLASK
To use Jinja - in VS Code, In the command palette ( cmd-shift-p ) select Install Extension and choose Jinja Snippets


Clone the repository to your own directory:
git clone git@github.com:janeymcnab/python_project_shop_inventory.git

Create the database by entering the following command in the console:
createdb products_manufacturers

From the cloned repository, run the following command in the terminal:
psql -d products_manufacturers -f products_manufacturers.sql

In the terminal run the following command to populate:
python3 console.py

Make sure you are in the correct directory and then run the following command in the terminal:
flask run


Open your browser and enter the following URL: http://localhost:5000/
