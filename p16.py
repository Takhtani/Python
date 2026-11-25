class Student:
    college = "Marwadi University"      # class attribute

    def __init__(self, name, roll_no, marks):
        self.name = name                # instance attributes
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print(f"Name: {self.name} | Roll No: {self.roll_no} | Marks: {self.marks}")

    def result(self):
        return "Pass" if self.marks >= 40 else "Fail"

s1 = Student("Aarav", 1, 78)
s2 = Student("Diya", 2, 35)

s1.display()
print("Result:", s1.result())
s2.display()
print("Result:", s2.result())
print("College:", Student.college)
