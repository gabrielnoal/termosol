import matplotlib.pyplot as plt
from math import *
import numpy as np


x_min = 0.000
x_max = 30.0
y_min = 0.000
y_max = 30.0
t_despejo = 2.0
t_max = 5.0
delta_x = 0.5
delta_y = delta_x
delta_t = 0.05
u = 1.0
v = 0.0
a = 15.0
b = 15.0
k = 1.0
Q = 80.0
alpha = u
tol = 1e-4

malha_x = [x for x in np.arange(x_min, x_max + delta_x, delta_x)]
malha_y = [y for y in np.arange(y_min, y_max + delta_y, delta_y)]
# print(len(malha_x), len(malha_y))
malha_atual = np.zeros(shape=(len(malha_x), len(malha_y)))
malha_atualizada = np.copy(malha_atual)


for t in np.arange(0, t_max + delta_t, delta_t):
    lista_erros = []
    for i in np.arange(1, len(malha_x) - 1, 1):
        for j in np.arange(1, len(malha_y) - 1, 1):
            t1 = v * (malha_atual[i + 1][j] - malha_atual[i - 1][j])/(2*delta_x)
            t2 = u * (malha_atual[i][j + 1] -malha_atual[i][j - 1])/(2*delta_y)
            t3 = -k * (malha_atual[i][j + 1] - 2*malha_atual[i][j] + malha_atual[i][j - 1]) / (delta_x**2)
            t4 = -k * (malha_atual[i + 1][j] - 2*malha_atual[i][j] + malha_atual[i - 1][j]) / (delta_y**2)
            soma = t1 + t2 + t3 + t4
            Qc = Q if (j == b and i == a and t <= t_despejo) else 0

            malha_atualizada[i][j] = ((delta_t * Qc) / (delta_x * delta_y)) - (delta_t * soma) + malha_atual[i, j]

            if malha_atual[i][j] != 0:
                erro = np.abs((malha_atualizada[i][j] - malha_atual[i][j]) / malha_atual[i][j])
                lista_erros.append(erro)

    # if len(lista_erros) > 0 and np.max(lista_erros) < tol:
        # print("Erro relativo máximo: ", np.max(lista_erros))

    malha_atual = np.copy(malha_atualizada)

# print("malha atualizada")
# for i in malha_atual:
#     print(i)

print("C[40][40]:\n {}".format(malha_atual[40][40]))
plt.axis((0, x_max, 0, y_max))
plt.imshow(malha_atual)
plt.colorbar()

plt.show()
