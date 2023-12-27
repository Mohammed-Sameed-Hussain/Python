from matplotlib import pyplot as plt
import numpy as np

plt.style.use('fivethirtyeight')

dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

x_indexes = np.arange(len(dev_x))
width = 0.25

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

plt.bar(x_indexes - width, dev_y, width=width, color='#444444', label='All Devs')

# Median JavaScript Developer Salaries by Age
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]
js_dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

plt.bar(x_indexes, js_dev_y, width=width, color='#008fd5', label='JavaScript')

# Median Python Developer Salaries by age
py_dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

plt.bar(x_indexes + width, py_dev_y, width=width, color='#e5ae38', label='Python')

plt.xticks(ticks=x_indexes, labels=dev_x)  # Corrects the x axis

plt.title("Median Salary (INR) by age")
plt.xlabel("Ages")
plt.ylabel("Median Salary (INR)")

plt.legend()

plt.tight_layout()
plt.show()
