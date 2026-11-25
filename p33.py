import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root",
                               password="root", database="college_db")
cursor = conn.cursor()

# Create table
cursor.execute("DROP TABLE IF EXISTS students")
cursor.execute("""CREATE TABLE students (
                    id INT PRIMARY KEY,
                    name VARCHAR(30),
                    city VARCHAR(20),
                    marks INT)""")
print("Table 'students' created.")

# Insert records
data = [(101, "Aarav", "Rajkot", 78),
        (102, "Diya", "Ahmedabad", 85),
        (103, "Rohan", "Surat", 66),
        (104, "Sneha", "Vadodara", 72),
        (105, "Kabir", "Rajkot", 90)]
cursor.executemany("INSERT INTO students VALUES (%s, %s, %s, %s)", data)
conn.commit()
print(cursor.rowcount, "records inserted.")

# Retrieve and display records
cursor.execute("SELECT * FROM students")
print("\nID    Name      City        Marks")
print("-" * 36)
for row in cursor.fetchall():
    print(f"{row[0]:<6}{row[1]:<10}{row[2]:<12}{row[3]}")

conn.close()
