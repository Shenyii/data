import numpy
import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(111)
plt.xlabel('x(m)')
plt.ylabel('y(m)')

data = numpy.loadtxt('data3.dat')
x = data[:, 0]
y = data[:, 1]
plt.plot(x, y, '-')

x1 = data[:, 3]
y1 = data[:, 4]
plt.plot(x1, y1, '-.')

plt.plot(4, 4, '.')

plt.legend(['real trajectory', 'perfect trajectory'], loc = 0,ncol = 1)
plt.show()