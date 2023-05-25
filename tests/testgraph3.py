import matplotlib.pyplot as plt
from matplotlib import animation

x = []
y = []

with open('data.txt', 'r') as f:
	for line in f:
		x_val, y_val = line.strip().split(',')
		x.append(float(x_val))
		y.append(float(y_val))
		
plt.plot(x, y)
plt.show()
