from die import Die
import plotly.express as px

# Create Dies
die_1 = Die()
die_2 = Die()

# Make certain amount of rolls and store results in the list
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results
frequencies = []
max_results = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_results + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
title = "Result of rolling two D6 dice 1000 times"
labels = {"x": "Result", "y": "Frequency"}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.show()
