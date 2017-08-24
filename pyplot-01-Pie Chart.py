from matplotlib import pyplot as plt

sizes = [25, 25, 25, 25]
labels = '00', '01', '10', '11'

plt.pie(sizes,
        labels=labels,
        autopct='%1.1f%%',
        startangle=90)
plt.axis('equal')

plt.show()
