import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",          # change to your MySQL password
    database="college_db"
)

if conn.is_connected():
    print("Database Connected Successfully")
    cursor = conn.cursor()
    cursor.execute("SELECT DATABASE()")
    print("Connected to database:", cursor.fetchone()[0])
    cursor.close()

conn.close()
