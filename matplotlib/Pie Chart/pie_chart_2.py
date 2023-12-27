from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')



# Language Popularity
slices = [59219, 55466, 47544, 36443, 35917,]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java',]
explode = [0,0,0,0.1,0]  # List of float to tell how much we want to emphasize the size (the value is the fraction of radius we want to explode it out)




plt.pie(slices, labels = labels, explode=explode, shadow='True', startangle=90, autopct='%1.1f%%',wedgeprops={'edgecolor':'black'})










plt.title("My Pie Chart")

plt.tight_layout()
plt.show()
