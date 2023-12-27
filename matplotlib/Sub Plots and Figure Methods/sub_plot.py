import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn')

data = pd.read_csv('data.csv')
ages = data['Age'].to_numpy()
dev_salaries = data['All_Devs'].to_numpy()
py_salaries = data['Python'].to_numpy()
js_salaries = data['JavaScript'].to_numpy()


fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)
# Or instead of (ax1, ax2); we can just use ax and it contains two axis indexed at 0 and 1 and can be accessed as ax[0] and ax[1]

ax1.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs')


ax2.plot(ages, py_salaries, label='Python')
ax2.plot(ages, js_salaries, label='JavaScript')


ax1.legend()
ax1.set_title('Median Salary (USD) by Age')
# ax1.set_xlabel('Ages')
ax1.set_ylabel('Median Salary (USD)')


ax2.legend()
# ax2.set_title('Median Salary (USD) by Age')
ax2.set_xlabel('Ages')
ax2.set_ylabel('Median Salary (USD)')

plt.tight_layout()

plt.show()