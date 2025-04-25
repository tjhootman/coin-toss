import plotly.express as px
from coin import Coin

coin = Coin()

results = []

for flip in range(50):
    result = coin.flip()
    results.append(result)

frequencies = {}

possible_outcomes = ['Heads', 'Tails']

for outcome in possible_outcomes:
    frequency = results.count(outcome)
    frequencies[outcome] = frequency

print(frequencies)

fig = px.bar(x=possible_outcomes, y=frequencies)
fig.show()
