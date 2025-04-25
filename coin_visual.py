import plotly.express as px
from coin import Coin

coin = Coin()

flip_count = 50
results = []

for flip in range(flip_count):
    result = coin.flip()
    results.append(result)

frequencies = {}

possible_outcomes = ['Heads', 'Tails']

for outcome in possible_outcomes:
    frequency = results.count(outcome)
    frequencies[outcome] = frequency

# print(frequencies)

title = f'Results of {flip_count} Coin Tosses'
labels = {'x': 'Outcome', 'y': 'Number of Times'}
fig = px.bar(x=possible_outcomes, y=frequencies, title=title, labels=labels)
fig.show()
