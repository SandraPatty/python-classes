import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import sympy as sm
from sympy.abc import x


y = sm.Function('y')
eq = sm.Eq(sm.Derivative(y(x), x), -2 * y(x))
solution1 = sm.dsolve(eq, ics={y(0): sm.sqrt(2)})
solution1 = sm.lambdify(x, solution1.rhs, 'numpy')

solution2 = sp.integrate.solve_ivp(lambda t, y: -2 * y, [0, 10], [np.sqrt(2)])

fig, ax = plt.subplots(2, 1, figsize=(10, 8))

xrange = np.linspace(0, 10, 1000)
ax[0].plot(xrange, solution1(xrange))
ax[0].plot(solution2.t, solution2.y[0])
ax[0].legend(['sympy', 'scipy'])
ax[0].set_title('Solutions')
ax[1].plot(solution2.t, solution2.y[0] - solution1(solution2.t))
ax[1].set_title('Difference')

plt.savefig('differential-equations.png')
plt.show()
