from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

slices = [120, 80, 30, 20]
labels = ['Sixty', 'Forty', 'Extra1', 'Extra2']
colors = ['#008fd5','#fc4f30', 'yellow','green'] #We can use Hex Color Values!

# plt.pie(slices, labels = labels, wedgeprops={'edgecolor':'black'})
plt.pie(slices, labels = labels, colors = colors, wedgeprops={'edgecolor':'black'})






plt.title("My Pie Chart")

plt.tight_layout()
plt.show()
