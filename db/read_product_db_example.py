#1- Import
import sqlite3

#2- Connect to Product DB
connection=sqlite3.connect("db/products.db")
cursor = connection.cursor()

#3- Run the Query
cursor.execute("SELECT * FROM products")

#4- Fetch the DB Rows
db_rows=cursor.fetchall()
print("DB Rows Fetched = ", db_rows)

PRODUCT_DB ={
    name.lower():{
        "price":price,
        "stock":stock,
        "brand":brand
        } for _,name,price,stock,brand in db_rows
}
print("Fetched DB Data in JSON Format : ", PRODUCT_DB)

#5- Close the connection
connection.close()