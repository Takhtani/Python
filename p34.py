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

print("Before update:")
display()

cursor.execute("UPDATE students SET marks = 82 WHERE id = 103")
cursor.execute("UPDATE students SET city = 'Gandhinagar' WHERE id = 102")
conn.commit()
print("\nUpdate done. Rows affected by last query:", cursor.rowcount)

print("\nAfter update:")
display()

conn.close()
