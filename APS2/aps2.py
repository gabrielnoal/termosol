import matplotlib.pyplot as plt
from math import *
import numpy as np


x_min = 0.0
x_max = 0.4
y_min = 0.0
y_max = 0.4
t_max = 10.0
delta_x = 0.1
delta_y = delta_x
delta_t = 1#10.0**(-3)

# condutividade termal
k = 0.23
# densidade
p = 2.7*10.0**(-6)
# capacidade de calor especifica
cp = 897.0

alpha = k/(p*cp)
fo = round(alpha * (delta_t/((delta_x)**2)), 3)
print("alpha: {}".format(alpha))
print("fo: {}".format(fo))

#               top    rigth  bottom   left 
borda_isolada = [False, False, False, True]

#                        top    rigth  bottom   left 
temperaturas_iniciais = [150.0, 50.0, 0.0, 0.0]


malha_x = [x for x in np.arange(x_min , x_max + delta_x, delta_x)]
malha_y = [y for y in np.arange(y_min , y_max + delta_y, delta_y)]

malha = np.zeros(shape=(len(malha_x), len(malha_y)), dtype='double')
malha[0].fill(temperaturas_iniciais[0])
malha[-1].fill(temperaturas_iniciais[-2])
for i in range(len(malha)):
  malha[i][0]=temperaturas_iniciais[-1]
  malha[i][-1]=temperaturas_iniciais[1]


print("malha:\n {}\n".format(malha))
malha_atualizada = np.copy(malha)


for t in np.arange(0 , t_max + delta_t, delta_t):
  for i in np.arange(1, len(malha_x) - 1, 1):
    for j in np.arange(1, len(malha_y) - 1, 1):
      actualTemp = (1 - 4*fo)*malha[i][j]
      # if borda_isolada[0] and i == 0:
      #   malha_atualizada[i][j] = fo * (2*malha[i + 1][j]  + malha[i][j + 1] + malha[i][j - 1]) + actualTemp
      # elif borda_isolada[2] and i == len(malha_x) - 1:
      #   malha_atualizada[i][j] = fo * (2*malha[i - 1][j]  + malha[i][j + 1] + malha[i][j - 1]) + actualTemp
      # elif borda_isolada[3] and j == 0:
      #   malha_atualizada[i][j] = fo * (2*malha[i][j + 1]  + malha[i][j + 1] + malha[i][j - 1]) + actualTemp
      # elif borda_isolada[1] and j == len(malha_y) - 1:
      #   malha_atualizada[i][j] = fo * (2*malha[i][j - 1]  + malha[i][j] + malha[i][j - 1]) + actualTemp
      # else:
      malha_atualizada[i][j] = fo * (malha[i + 1][j] + malha[i - 1][j] + malha[i][j + 1] + malha[i][j - 1]) + actualTemp
      if np.isinf(malha_atualizada[i][j]):
        print("i: {} j:{}".format(i,j))
      
  malha = np.copy(malha_atualizada)

# print("malha_atualizada:\n {}".format(malha))
print ("malha atualizada")
for i in malha:
  print(i)