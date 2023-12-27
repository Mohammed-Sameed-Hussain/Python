import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn')

data = pd.read_csv('data.csv')
ages = data['Age'].to_numpy()
dev_salaries = data['All_Devs'].to_numpy()
py_salaries = data['Python'].to_numpy()
js_salaries = data['JavaScript'].to_numpy()


fig1 , ax1 = plt.subplots()
fig2 , ax2 = plt.subplots()


ax1.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs')


ax2.plot(ages, py_salaries, label='Python')
ax2.plot(ages, js_salaries, label='JavaScript')


ax1.legend()
ax1.set_title('Median Salary (USD) by Age')
ax1.set_xlabel('Ages')
ax1.set_ylabel('Median Salary (USD)')


ax2.legend()
ax2.set_title('Median Salary (USD) by Age')
ax2.set_xlabel('Ages')
ax2.set_ylabel('Median Salary (USD)')

plt.tight_layout()

plt.show()

# fig1.savefig('fig1.png')  # How to save a plot from code
# fig2.savefig('fig2.png')  # How to save a plot from code