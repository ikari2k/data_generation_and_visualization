from pathlib import Path
import matplotlib.pyplot as plt

import csv

path = Path("weather_data/sitka_weather_07-2021_simple.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Get highest temps from file

highs = []
for row in reader:
    high = int(row[4])
    highs.append(high)

# Plot data
plt.style.use("ggplot")
fig, ax = plt.subplots()
ax.plot(highs, color="red")

# Format the plot
ax.set_title("Highest temperature a day, July 2021", fontsize=24)
ax.set_xlabel("", fontsize=16)
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
