import matplotlib.pyplot as plt
from math import *
import numpy as np


x_min = 0.0
x_max = 0.5
y_min = 0.0
y_max = 0.5
t_max = 10.0
delta_x = 0.1
delta_y = delta_x
delta_t = 10.0**(-2)

alpha = 0.25
f0 = alpha * (delta_t/((delta_x)**2))
#                        top    rigth  bottom   left 
temperaturas_iniciais = [100.0, 2.0, 3.0, 4.0]

malha_x = [x for x in np.arange(x_min , x_max + delta_x, delta_x)]
malha_y = [y for y in np.arange(y_min , y_max + delta_y, delta_y)]

malha = np.zeros(shape=(len(malha_x), len(malha_y)))
malha[0].fill(temperaturas_iniciais[0])
malha[-1].fill(temperaturas_iniciais[-2])
malha[:][-1] = temperaturas_iniciais[1]
malha[:][0] = temperaturas_iniciais[-1]


print("malha:\n {}\n".format(malha))
malha_atualizada = np.copy(malha)


for t in np.arange(0 , t_max + delta_t, delta_t):
  for i in np.arange(1, len(malha_x) - 1, 1):
    for j in np.arange(1, len(malha_y) - 1, 1):
      malha_atualizada[i][j] = f0 * (malha[i + 1][j] + malha[i - 1][j] + malha[i][j + 1] + malha[i][j - 1]) + (1 - 4*f0)*malha[i][j]
  malha = np.copy(malha_atualizada)

print("malha_atualizada:\n {}\n".format(malha))