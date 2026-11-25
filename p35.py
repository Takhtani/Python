import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root",
                               password="root", database="college_db")
cursor = conn.cursor()

def display():
    cursor.execute("SELECT * FROM students")
    print("ID    Name      City        Marks")
    print("-" * 36)
    for row in cursor.fetchall():
        print(f"{row[0]:<6}{row[1]:<10}{row[2]:<12}{row[3]}")

print("Before delete:")
display()

cursor.execute("DELETE FROM students WHERE id = 104")
print("\nDeleted", cursor.rowcount, "record(s) with id = 104")
cursor.execute("DELETE FROM students WHERE city = 'Rajkot' AND marks < 80")
print("Deleted", cursor.rowcount, "record(s) from Rajkot with marks below 80")
conn.commit()

print("\nAfter delete:")
display()

conn.close()
