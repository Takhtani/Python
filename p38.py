import matplotlib.pyplot as plt

subjects = ["Python", "DBMS", "Networking", "Cyber Law", "Mathematics"]
marks = [85, 78, 72, 90, 65]
explode = [0.1, 0, 0, 0, 0]

plt.figure(figsize=(6, 6))
plt.pie(marks, labels=subjects, autopct="%1.1f%%", explode=explode,
        startangle=90, shadow=True)
plt.title("Subject-wise Marks Distribution")
plt.savefig("pie_chart.png")
plt.show()
