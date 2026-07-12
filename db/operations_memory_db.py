#1- Import
import sqlite3

#2- Create function to save the message in DB
def save_message(session_id,role,message):
    # Connect to Memory DB
    conn = sqlite3.connect("db/memory.db")
    cursor = conn.cursor()
    
    # Insert the data in DB
    cursor.execute("""
                   INSERT INTO conversation_memory
                   (session_id,role,message)
                   VALUES(?,?,?)
                   """,
                   (session_id,role,message)
                   )
    # Commit The changes
    conn.commit()
    
    # Close the coonection
    conn.close()