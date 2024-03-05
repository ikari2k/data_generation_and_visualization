from die import Die
import plotly.express as px

# Create Die
die = Die()

# Make certain amount of rolls and store results in the list
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analyze the results
frequencies = []
poss_results = range(1, die.num_sides + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
fig = px.bar(x=poss_results, y=frequencies)
fig.show()
