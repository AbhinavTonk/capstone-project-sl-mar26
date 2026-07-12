#0- pip command : No pip command is required for using sqlite

#1- Imports
import sqlite3

#2- Write the data that we want to push to our Created DB
PRODUCT_DB={
    "iphone 15":{
        "price": "$999",
        "stock" : 12,
        "brand": "apple"
    },
    "samsung galaxy s23":{
        "price": "$899",
        "stock" : 8,
        "brand": "samsung"
    },
    "google pixel 7":{
        "price": "$799",
        "stock" : 15,
        "brand": "google"
    },
    "macbook air":{
        "price": "$1199",
        "stock" : 5,
        "brand": "apple"
    }
}

#3- Create connection for sqlite
connection=sqlite3.connect("db/products.db")
cursor=connection.cursor()

#4- Create Tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    price TEXT NON NULL,
    stock INTEGER NOT NULL,
    brand TEXT NOT NULL
)
""")

#5- Insert values into the Tables
for product_name, details in PRODUCT_DB.items():
    cursor.execute("""
                   INSERT OR REPLACE INTO products
                   (name,price,stock,brand)
                   VALUES(?,?,?,?)
                   """,
                   (
                      product_name,
                      details["price"],
                      details["stock"],
                      details["brand"] 
                   ))

#6- Commit the changes
connection.commit()

#7- Close the connection
connection.close()

print("Product DB Created Successfully")