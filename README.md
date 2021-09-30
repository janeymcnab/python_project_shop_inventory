The technologies used in this project:
python  
Flask  
PostgreSQL  
psycopg2    
HTML/CSS    


To run first install the following:
Enter the following commands into your terminal:
pip3 install psycopg2
pip3 install Flask
pip3 install python-dotenv


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
