import matplotlib.pyplot as plt
from math import *
import numpy as np

lado_quadrado = 0.03
L = 0.3
k = 200
h = 15
A = lado_quadrado**2
P = lado_quadrado * 4
T_base = 350
T_amb = 300

def calc_m():
  return sqrt((h*P)/(k*A))

def calc(x, L):
  return (cosh(calc_m()*(L-x)) + (h/(calc_m() *k)) * sinh(calc_m() * (L-x)))/(cosh(calc_m()*L) + (h/(calc_m() * k)) + sinh(calc_m() * L))




x = [x for x in np.arange(0, L, 0.001)]
y = []
for i in x:
  T = (T_base - T_amb) * calc(i, L) + T_amb
  if i == L/2:
    print("T de L/2: {} K".format(T))
  y.append(T)


plt.plot(x, y)
plt.ylabel("T [K]")
plt.xlabel("x [m]")

plt.show()
