student = {"name": "Aarav", "age": 21, "course": "M.Sc. CS&CL"}
print("Dictionary      :", student)
print("Name            :", student["name"])
print("get('age')      :", student.get("age"))
print("get('city')     :", student.get("city", "Not found"))

student["city"] = "Rajkot"
print("After adding    :", student)

student.update({"age": 22, "semester": 1})
print("After update    :", student)

print("keys()          :", list(student.keys()))
print("values()        :", list(student.values()))
print("items()         :", list(student.items()))

print("pop('semester') :", student.pop("semester"))
student.setdefault("grade", "A")
print("After setdefault:", student)

del student["city"]
print("After del       :", student)
print("'name' in dict  :", "name" in student)

for key, value in student.items():
    print(key, "->", value)

backup = student.copy()
student.clear()
print("After clear     :", student, "| backup:", backup)
