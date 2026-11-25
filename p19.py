class Employee:
    company = "Marwadi Group"        # class variable
    count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    # 1. Instance method - works with object data (self)
    def show(self):
        print(f"{self.name} works at {Employee.company}, salary {self.salary}")

    # 2. Class method - works with class data (cls)
    @classmethod
    def change_company(cls, new_name):
        cls.company = new_name

    @classmethod
    def from_string(cls, text):
        name, salary = text.split("-")
        return cls(name, int(salary))

    # 3. Static method - no access to self or cls
    @staticmethod
    def is_workday(day):
        return day not in ("Saturday", "Sunday")

e1 = Employee("Aarav", 50000)
e2 = Employee.from_string("Diya-60000")
e1.show()
e2.show()

Employee.change_company("Marwadi University")
e1.show()

print("Total employees:", Employee.count)
print("Is Monday a workday?", Employee.is_workday("Monday"))
print("Is Sunday a workday?", Employee.is_workday("Sunday"))
