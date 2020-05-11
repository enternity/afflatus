#!/usr/bin/env python3
import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_csv('data.csv')
ages = data['Age']
dev_salaries= data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

plt.plot(ages, dev_salaries, color='#444444', linestyle='--',
            label = 'All Devs')

plt.plot(ages, py_salaries, label='Python')

overall_median = 57287

plt.fill_between(ages, py_salaries, dev_salaries,alpha=.25,
                    where=(py_salaries > dev_salaries),
                    interpolate=True, label='Above agv')

plt.fill_between(ages, py_salaries, dev_salaries,alpha=.25,
                    where=(py_salaries <= dev_salaries),
                    interpolate=True, color='red', label='Bellow agv')                    

plt.legend()

plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Salaries')

plt.tight_layout()

plt.show()
