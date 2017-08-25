from matplotlib import pyplot as plt

x = list(range(11))
y =[0, 1, 2, 1, 0, -1, 0, -1, -2, -1, 0]

plt.axes(aspect = 'equal')
plt.plot(x,y)
plt.grid(True, which='both',axis='both')

plt.plot([0, 10], [0, 0], 'k-')

plt.show()
