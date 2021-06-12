# -*- coding: utf-8 -*-
"""lagrange.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1q8PWZ7HK6Oll_cyrYFqs8C46JVkBZ1SQ
"""

import numpy as np
import matplotlib.pyplot as plt

"""Inputs"""

x = np.array([20, 21, 23, 24, 25, 27, 29, 30],float)
y = np.array([346, 362, 343, 339, 347, 346, 339, 394],float)

def langrange (x, y, predict):
  yp = 0
  for i in range(len(x)):
    p = 1
    for j in range(len(x)):
      if j != i:
        p *= (predict - x[j]) / (x[i] - x[j])
    yp += y[i] * p
  return yp

result = langrange(x, y, 26)
print("Result is " + str(result))

"""Ploting"""

xplt = np.linspace(x[0], x[-1])
yplt = np.array([], float)

for xp in xplt:
  yp = langrange(x, y, xp)
  yplt = np.append(yplt, yp)

plt.plot(x, y, "ro", xplt, yplt, "b-")
plt.show()