import matplotlib.pyplot as plt
from math import *
import numpy as np

plt.close('all')

x_min = 0.000  # m
x_max = 30.0  # m
y_min = 0.000  # m
y_max = 30.0  # m
t_despejo = 2.0  # s
t_max = 5.0  # s
delta_x = 0.5  # m
delta_y = delta_x  # m
delta_t = 0.025  # s
u = 0.50  # m/s
v = 0.50  # m/s
a = 5.0  # m
b = 15.0  # m
k = 2.0  # m²/s
Q = 120.0  # kg/m/s
alpha = u  # m
tol = 1e-4  # m

malha_x = [x for x in np.arange(x_min, x_max + delta_x, delta_x)]
malha_y = [y for y in np.arange(y_min, y_max + delta_y, delta_y)]
print(len(malha_x), len(malha_y))
malha_atual = np.zeros(shape=(len(malha_x), len(malha_y)))
malha_atualizada = np.copy(malha_atual)


for t in np.arange(0, t_max + delta_t, delta_t):
    lista_erros = []
    for y in np.arange(1, len(malha_x) - 1, 1):
        for x in np.arange(1, len(malha_y) - 1, 1):
            t1 = u * (malha_atual[y][x + 1] -
                      malha_atual[y][x - 1])/(2*delta_x)
            t2 = v * (malha_atual[y + 1][x] -
                      malha_atual[y - 1][x])/(2*delta_y)
            t3 = -k * (malha_atual[y + 1][x] - 2*malha_atual[y]
                       [x] + malha_atual[y - 1][x]) / (delta_x**2)
            t4 = -k * (malha_atual[y][x + 1] - 2*malha_atual[y]
                       [x] + malha_atual[y][x - 1]) / (delta_y**2)
            # if x*delta_x == 16 and y*delta_y == 15:
            #   print("\nT: {}".format(t))
            #   print("t1: {}".format(t1))
            #   print("t2: {}".format(t2))
            #   print("t3: {}".format(t3))
            #   print("t4: {}\n".format(t4))
            soma = t1 + t2 + t3 + t4
            Qc = Q if (x*delta_x == a and y*delta_y == b and t <= t_despejo) else 0

            malha_atualizada[y][x] = (
                (delta_t * Qc) / (delta_x * delta_y)) - (delta_t * soma) + malha_atual[y, x]

            if malha_atual[y][x] != 0:
                erro = np.abs(
                    (malha_atualizada[y][x] - malha_atual[y][x]) / malha_atual[y][x])
                lista_erros.append(erro)

    for i in range(len(malha_atualizada)):
        if(i == 0):
            malha_atualizada[i] == malha_atualizada[i+1]
        if (i == len(malha_atualizada)):
            malha_atualizada[i] == malha_atualizada[i-1]
        else:
            malha_atualizada[i][0] = malha_atualizada[i][1]
            malha_atualizada[i][-1] = malha_atualizada[i][-2]

    # if len(lista_erros) > 0 and np.max(lista_erros) < tol:
        # print("Erro relativo máximo: ", np.max(lista_erros))

    malha_atual = np.copy(malha_atualizada)

pontos = [[15,5],[26, 27.5], [11,28], [6.5,17], [7.5, 12.5], [7.5,20.5]]

for p in pontos:
  x = p[1]
  y = p[0]
  y_index = int(y/delta_y)
  x_index = int(x/delta_x)
  print("y_index: {}, x_index: {}".format(y_index, x_index))
  print("C[{}][{}]:\n {}".format(x, y, malha_atual[y_index][x_index]))
print("Velor max: {}".format(np.max(malha_atual)))
plt.imshow(malha_atual)
plt.colorbar()
plt.gca().invert_yaxis()
plt.show()
