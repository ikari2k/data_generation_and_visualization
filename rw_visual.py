import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Prepare data
rw = RandomWalk()
rw.fill_walk()

coordinates = tuple(zip(rw.x_values, rw.y_values))
print(coordinates)

# Display data points
plt.style.use("classic")
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15)
ax.set_aspect("equal")  # setting equal aspect ratio for each axis
plt.show()
