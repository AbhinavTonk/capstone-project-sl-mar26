#1- Imports
import sqlite3

#2- Make sqlite connection
connection=sqlite3.connect("db/memory.db")
cursor=connection.cursor()

#3- Create Tables
cursor.execute("""
               CREATE TABLE IF NOT EXISTS conversation_memory (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   session_id TEXT NOT NULL,
                   role TEXT NOT NULL,
                   message TEXT NOT NULL,
                   timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
               )
               """)

#4- Commit the changes
connection.commit()

#5- Close the Connection
connection.close()

print("Memory database is created successfully")