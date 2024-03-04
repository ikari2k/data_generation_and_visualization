import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.style.use("ggplot")
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=100)

# Define chart title and axes labels
ax.set_title("Squares", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Values squares", fontsize=14)

# Define labels size
ax.tick_params(labelsize=14)

plt.show()
