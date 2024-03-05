from pathlib import Path
import matplotlib.pyplot as plt
from datetime import datetime

import csv

path = Path("weather_data/sitka_weather_2021_simple.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Get highest temps from file

dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], "%Y-%m-%d")
    high = int(row[4])
    low = int(row[5])
    dates.append(current_date)
    highs.append(high)
    lows.append(low)

# Plot data
plt.style.use("ggplot")
fig, ax = plt.subplots()
ax.plot(dates, highs, color="red", alpha=0.5)  # alpha - make colors more delicate
ax.plot(dates, lows, color="blue", alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)


# Format the plot
ax.set_title("Highest and lowest temperature a day, 2021", fontsize=24)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
