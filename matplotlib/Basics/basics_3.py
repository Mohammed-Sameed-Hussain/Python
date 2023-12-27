from matplotlib import pyplot as plt

# To access the list of available styles for plotting
print(plt.style.available)

plt.style.use('fivethirtyeight')
# plt.xkcd() # To give comic like appearance to the plots. xkcd is a comic blog


# -------******-------******--------*******------#

# Median Salary by Age
dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

plt.plot(dev_x, dev_y, color='k', linestyle='--', marker='.', label='All Devs')
# We can also use Hex Values for colors, which gives us more colour option
# plt.plot(dev_x, dev_y, color='#444444', linestyle='--', marker='.', label='All Devs')

# plt.plot(dev_x, dev_y, 'k--', label='All Devs') ## A very non-readable way of giving colors and formats to graphs

# Median JavaScript Developer Salaries by Age
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]
js_dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

plt.plot(js_dev_x, js_dev_y, color='#adad3b', linewidth='3', label='Javascript')

# Median Python Developer Salaries by age
py_dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

plt.plot(py_dev_x, py_dev_y, color='b', marker='o', linewidth='3', label='Python')

# plt.plot(py_dev_x, py_dev_y, 'b', label='Python') ## A very non-readable way of giving colors and formats to graphs


plt.title("Median Salary (INR) by age")
plt.xlabel("Ages")
plt.ylabel("Median Salary (INR)")

plt.legend()
# plt.legend(["All Devs", "Python"])  # A very naive way of adding legends to graph (very error-prone)

plt.grid(True)

plt.tight_layout()  # Use it when the padding of the graphs looks bad or not normal

# plt.savefig('plot.png')  ## A way to save the graph from the program!

plt.show()  # If this is not written, then the plot window will now show up
