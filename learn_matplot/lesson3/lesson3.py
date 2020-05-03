#!/usr/bin/env python3
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd 
from collections import Counter


# Language Popularity
slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode =  [0,0,0,0.1,0]


plt.style.use('fivethirtyeight')


plt.pie(slices, labels=labels,explode=explode,shadow=True,
        startangle=90, autopct = '%1.1f%%',
        wedgeprops={'edgecolor':'black'})

plt.title("My Awesome Pie Chart")
plt.tight_layout()
plt.show()