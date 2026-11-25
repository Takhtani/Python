import matplotlib.pyplot as plt

marks = [45, 52, 58, 61, 63, 65, 67, 68, 70, 72, 72, 74, 75, 76, 78,
         79, 80, 82, 83, 85, 86, 88, 90, 91, 93, 55, 69, 77, 81, 95]

plt.figure(figsize=(7, 5))
plt.hist(marks, bins=[40, 50, 60, 70, 80, 90, 100],
         color="skyblue", edgecolor="black")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.title("Histogram of Student Marks")
plt.savefig("histogram.png")
plt.show()
