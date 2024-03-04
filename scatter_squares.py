import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use("ggplot")
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10)

# Define chart title and axes labels
ax.set_title("Squares", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Values squares", fontsize=14)

# Define labels size
ax.tick_params(labelsize=14)

# Define range for axes
ax.axis([0, 1100, 0, 1_100_000])

plt.show()