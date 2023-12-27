from matplotlib import pyplot as plt


plt.style.use('fivethirtyeight')

languages = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java', 'Bash/ShellPowerShell', 'C#', 'PHP']
popularity = [59219, 55446, 47544, 36443, 35917, 31991, 27097, 23030]

languages.reverse()
popularity.reverse()

# plt.bar(languages, popularity)
plt.barh(languages,popularity)  # Gives a horizontal bar chart


plt.title("Most Popular Languages")
# plt.ylabel("Programming Languages")
plt.xlabel("Number of People Who Use")

plt.legend()

plt.tight_layout()
plt.show()
