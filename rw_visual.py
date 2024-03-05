import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Prepare new random walk until program is active
while True:

    # Prepare data
    rw = RandomWalk()
    rw.fill_walk()

    coordinates = tuple(zip(rw.x_values, rw.y_values))
    print(coordinates)

    # Display data points
    plt.style.use("classic")
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(
        rw.x_values,
        rw.y_values,
        c=point_numbers,
        cmap=plt.cm.Blues,
        edgecolor="none",
        s=15,
    )
    ax.set_aspect("equal")  # setting equal aspect ratio for each axis
    # Underline first and last point in Random Walk
    ax.scatter(0, 0, c="green", edgecolors="none", s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="none", s=100)
    plt.show()

    keep_running = input("Create new random walk plot? (y/n): ")
    if keep_running == "n":
        break
