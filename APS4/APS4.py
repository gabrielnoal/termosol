# -*- Coding: UTF-8 -*-
#coding: utf-8

import math
import numpy as np
import matplotlib.pyplot as plt
import time
from math import pi, sin

grupo = 10

t1 = time.time()

dx = dy = 0.5

dx2 = dy2 = dx*dy

Lx = 30
Ly = 30

pontosX = int((Lx/dx)+1)
pontosY = int((Ly/dy)+1)

tol = 1e-4

k = 1
alpha = 1
Qponto = 80

conv = ((dx)**2)/(4*k)
print("dT conv: ", conv)

dt = conv - 0.01
print("dT utilizado: ", dt)

# tempo derramando poluente
T = 2

# pontos que derrama o poluente
a = int(15)
b = int(15)

# vel do rio
u = alpha
def v(j): return alpha * sin(pi / 5 * j)


print((a, b))


def getTemp(m, nn, t, temp1, temp2, temp3, temp4):

    n = 0

    C = np.zeros((m, nn))

    C_back = np.copy(C)

    while(n <= (t/dt)):

        lista_erros = []

        for i in range(1, m-1):
            for j in range(1, nn-1):

                t1 = v(j) * (C_back[i + 1, j] - C_back[i - 1, j]) / (2 * dx)
                t2 = u * (C_back[i, j + 1] - C_back[i, j - 1]) / (2 * dy)
                t3 = -k / dx2 * (C_back[i, j + 1] - 2 *
                                 C_back[i, j] + C_back[i, j - 1])
                t4 = -k / dy2 * (C_back[i + 1, j] - 2 *
                                 C_back[i, j] + C_back[i - 1, j])
                soma = t1 + t2 + t3 + t4

                if i == b and j == a and n*dt <= T:
                    C[i, j] = dt * Qponto / (dx * dy) - dt * soma + C_back[i, j]
                else:
                    C[i, j] = - dt * soma + C_back[i, j]

                if C[i][j] != 0:
                    erro = np.abs((C[i][j] - C_back[i][j]) / C[i][j])
                    lista_erros.append(erro)

        if np.max(lista_erros) < tol:
            print("Erro relativo máximo: ", np.max(lista_erros))
            print("\nEstabilizou após {0} segundos\n".format((n-1)*dt))

            return C

        C_back = np.copy(C)

        # if n ==2:return C

        n += 1
    print("Tempo: ", (n-1)*dt)
    print("Erro relativo máximo: ", np.max(lista_erros), '\n')

    print("C[40][40]:\n {}".format(C_back[40][40]))

    return C

# def preencheBorda(m, nn, mat):
#     for z in range(1, m-1):
#         mat[0][z] = mat[1][z]
#         mat[m-1][z] = mat[m-1][z]

#     for v in range(1, nn-1):
#         mat[v][m-1] = temp2
#         mat[v][0] = temp4


results = getTemp(pontosY, pontosX, 10*T, 100, 50, 0, 75)
print(results.round(3))

t2 = time.time()
print(f"\nFinished in {round((t2-t1), 3)} seconds")

plt.imshow(results, cmap='ocean_r', interpolation='nearest')
plt.gca().invert_yaxis()
plt.colorbar()
plt.show()
