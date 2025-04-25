import plotly.express as px
from coin import Coin

# create an instance of the Coin class
coin = Coin()

# set number of times the coin is to be flipped
flip_count = 50
# initialize an empty list of results
results = []

# perform the coin flips
for flip in range(flip_count):
    result = coin.flip()
    results.append(result)

# initialize an empty dictionary to frequency of the outcomes
frequencies = {}

# define the possible outcomes
possible_outcomes = ['Heads', 'Tails']

# calculate the frequency of each outcome
for outcome in possible_outcomes:
    frequency = results.count(outcome)
    frequencies[outcome] = frequency

# define the title and labels for the bar chart and axes
title = f'Results of {flip_count} Coin Tosses'
labels = {'x': 'Outcome', 'y': 'Number of Times'}

# dictionary to map colors to outcomes
custom_colors = {'Heads': 'lightcoral', 'Tails': 'lightblue'}

# create the bar chart using ploty.express
fig = px.bar(x=possible_outcomes,
            y=[frequencies[outcome] for outcome in possible_outcomes],
            color=possible_outcomes,
            color_discrete_map=custom_colors,
            title=title,
            labels=labels)

# display the figure
fig.show()
