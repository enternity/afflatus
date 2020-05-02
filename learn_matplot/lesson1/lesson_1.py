#!/usr/bin/env python3

from matplotlib import pyplot as plt

#comics for fun =)))
plt.xkcd()

dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

py_dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]

ages = py_dev_x

plt.plot(ages, dev_y,label='All devs')

plt.plot(ages,py_dev_y, label='Python')
plt.plot(ages,js_dev_y, label='JS')

plt.xlabel('Ages')
plt.ylabel('Median Salary (USB)')

plt.title('Median Salary (USD) by Age')

plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig('lesson1.png')

plt.show()