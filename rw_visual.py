from matplotlib.axis import Axis
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Prepare new random walk until program is active
while True:

    # Prepare data
    rw = RandomWalk(50_000)
    rw.fill_walk()

    coordinates = tuple(zip(rw.x_values, rw.y_values))
    print(coordinates)

    # Display data points
    plt.style.use("classic")
    fig, ax = plt.subplots(figsize=(15, 9), dpi=90)
    point_numbers = range(rw.num_points)
    ax.scatter(
        rw.x_values,
        rw.y_values,
        c=point_numbers,
        cmap=plt.cm.Blues,
        edgecolor="none",
        s=1,
    )
    ax.set_aspect("equal")  # setting equal aspect ratio for each axis
    # Underline first and last point in Random Walk
    ax.scatter(0, 0, c="green", edgecolors="none", s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="none", s=100)

    # Hide the axis
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Create new random walk plot? (y/n): ")
    if keep_running == "n":
        break
