import matplotlib.pyplot as plt

cities = ["Rajkot", "Ahmedabad", "Surat", "Vadodara", "Gandhinagar"]
students = [45, 60, 38, 29, 22]

plt.figure(figsize=(7, 5))
plt.bar(cities, students, color=["red", "green", "blue", "orange", "purple"])
plt.xlabel("City")
plt.ylabel("Number of Students")
plt.title("City-wise Number of Students")
plt.savefig("bar_graph.png")
plt.show()
