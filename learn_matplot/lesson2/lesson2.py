#!/usr/bin/env python3
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd 
from collections import Counter

plt.style.use('fivethirtyeight')


data = pd.read_csv('data.csv')
ids = data['Responder_id']
lang_respones = data['LanguagesWorkedWith']

language_counter = Counter()

languages = []
popularity = []

for respone in lang_respones:
    language_counter.update(respone.split(";"))

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])


#languages.reverse()
#popularity.reverse()

plt.barh(languages, popularity)

plt.title('Most popular language')
plt.xlabel('Number of People Who use')
plt.tight_layout()
plt.show()
# plt.grid(True)
# plt.tight_layout()

# plt.savefig('lesson1.png')

# plt.show()