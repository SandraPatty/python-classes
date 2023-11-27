import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

data = np.loadtxt('start.dat')
E1 = np.diag(np.ones(data.size))
E2 = np.roll(-np.diag(np.ones(data.size)), 1, 0)
A = E1 + E2

fig, ax = plt.subplots()
ln, = ax.plot(data)


def update(_):
    global data
    data = data - 0.5 * np.matmul(A, data)
    ln.set_ydata(data)
    return ln,


anim = FuncAnimation(fig, update, 255, interval=30)

anim.save('котята.gif')
plt.show()
