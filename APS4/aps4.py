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


def dif_central(malha, x, y, eixo):
    if eixo == 'x':
        return (malha[x + 1][y] - 2*malha[x][y] + malha[x - 1][y])/(delta_x**2)
    if eixo == 'y':
        return (malha[x][y + 1] - 2*malha[x][y] + malha[x][y - 1])/(delta_y**2)


def dif_central2(malha, x, y, eixo):
    if eixo == 'x':
        return (malha[x + 1][y] - malha[x - 1][y])/(2*delta_x)
    if eixo == 'y':
        return (malha[x][y + 1] - malha[x][y - 1])/(2*delta_y)


malha_x = [x for x in np.arange(x_min, x_max + delta_x, delta_x)]
malha_y = [y for y in np.arange(y_min, y_max + delta_y, delta_y)]

print(len(malha_x), len(malha_y))
malha = np.zeros(shape=(len(malha_x), len(malha_y)))
# for i in range(len(malha)):
#   malha[i][0] = temperaturas_iniciais[-1]
#   malha[i][-1] = temperaturas_iniciais[1]
# malha[0].fill(temperaturas_iniciais[0])
# malha[-1].fill(temperaturas_iniciais[-2])


print("malha:\n {}\n".format(malha))
malha_atualizada = np.copy(malha)


for t in np.arange(0, t_max + delta_t, delta_t):
    for x in np.arange(0, len(malha_x), 1):
        for y in np.arange(0, len(malha_y), 1):
            q = Q if (t < t_despejo and x < a and y < b) else 0
            f0 = (q * delta_t)/(delta_x * delta_y)

            f1 = (u * delta_t * (dif_central2(malha_atualizada, x, y, 'x')
                                 if (x > 0 and x < len(malha_x) - 1) else 0))

            f2 = (u * sin((pi*x)/5) * delta_t * (dif_central2(malha_atualizada, x, y, 'y') if (y > 0 and y < len(malha_y) - 1) else 0))

            f3 = (k * delta_t * (dif_central(malha_atualizada, x, y, 'x')
                                 if (x > 0 and x < len(malha_x) - 1) else 0))

            f4 = (k * delta_t * (dif_central(malha_atualizada, x, y, 'y')
                                 if (y > 0 and y < len(malha_y) - 1) else 0))
            
            c = f0 - f1 - f2 + f3 + f4 + malha[x][y]
            malha_atualizada[x][y] = 0 if c < 0 else c


    malha = np.copy(malha_atualizada)

print("malha atualizada")
for i in malha:
    print(i)

print("C[40][40]:\n {}".format(malha[40][40]))
plt.axis((0,x_max,0,y_max))
plt.imshow(malha)
plt.colorbar()

plt.show()
