import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('data.csv')
ages = data['Age'].to_numpy()
dev_salaries = data['All_Devs'].to_numpy()
py_salaries = data['Python'].to_numpy()
js_salaries = data['JavaScript'].to_numpy()

print(data)
print(py_salaries)
plt.plot(ages, dev_salaries, color='#444444', linestyle='--', label='All Devs')

plt.plot(ages, py_salaries, label='Python')

overall_median = 57287

# plt.fill_between(ages, y1=py_salaries, y2= overall_median , alpha= 0.25)

plt.fill_between(ages, y1=py_salaries, y2= overall_median , where=(py_salaries > overall_median), interpolate = True, alpha= 0.25, label='Above Avg')


plt.fill_between(ages, y1=py_salaries, y2= overall_median , where=(py_salaries <= overall_median), interpolate = True, color='red', alpha= 0.25, label='Below Avg')


plt.legend()

plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')

plt.tight_layout()

plt.show()