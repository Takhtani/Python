import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [150, 180, 165, 210, 250, 275]

plt.figure(figsize=(7, 5))
plt.plot(months, sales, marker="o", color="green", linestyle="-", linewidth=2)
plt.xlabel("Month")
plt.ylabel("Sales (units)")
plt.title("Monthly Sales Trend")
plt.grid(True)
plt.savefig("line_graph.png")
plt.show()
