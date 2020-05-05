#!/usr/bin/env python3
import matplotlib.pyplot as plt

plt.style.use("fivethirtyeight")

minutes = [i for i in range(1,10)]

player1 = [1,2,3,3,4,4,4,4,5]
player2 = [1,1,1,1,2,2,2,3,4]
player3 = [1,1,1,2,2,2,3,3,3]

labels = ['player1', 'player2', 'player3']
colors = ['#008fd5', 'fc4f30', '6d904f']

plt.stackplot(minutes,player1, player2, player3, labels=labels, colors=colors)

plt.legend(loc='lower left')

plt.title("My awesome stack plot")
plt.tight_layout()
plt.show()