import matplotlib.pyplot as plt
from math import *
import numpy as np


x_min = 0.000
x_max = 0.600
y_min = 0.000
y_max = 0.600
t_max = 20.0
delta_x = 0.100
delta_y = delta_x
delta_t = 26.325
print("delta_t: {}".format(delt

#               top    rigth  bottom   left 
borda_isolada = [False, False, True, False]

#                        top    rigth  bottom   left 
temperaturas_iniciais = [100.0, 50.0, 0.0, 10.0]


malha_x = [x for x in np.arange(x_min , x_max + delta_x, delta_x)]
malha_y = [y for y in np.arange(y_min , y_max + delta_y, delta_y)]

malha = np.zeros(shape=(len(malha_x), len(malha_y)))
for i in range(len(malha)):
  malha[i][0] = temperaturas_iniciais[-1]
  malha[i][-1] = temperaturas_iniciais[1]
malha[0].fill(temperaturas_iniciais[0])
malha[-1].fill(temperaturas_iniciais[-2])



print("malha:\n {}\n".format(malha))
malha_atualizada = np.copy(malha)

if fo > 0.25:
  print('Fo > 0.25; Fo = {}'.format(fo))
else:

  for t in np.arange(0 , t_max + delta_t, delta_t):
    for i in np.arange(0, len(malha_x), 1):
      for j in np.arange(0, len(malha_y), 1):
        actualTemp = (1.0 - 4.0*fo)*malha[i][j]
        soma = 0

        if borda_isolada[0] and i == 0 and not j == 0 and not j == len(malha_x) - 1:
          # print("Top")
          soma = 2*malha[i + 1][j]
          if not j == 0:
            soma += malha[i][j - 1]
          if not j == len(malha_y) - 1:
            soma += malha[i][j + 1]
          malha_atualizada[i][j] = fo * (soma) + actualTemp

        if borda_isolada[1] and j == len(malha_y) - 1 and not i == 0 and not i == len(malha_x) - 1:
          # print("Right")
          soma = 2*malha[i][j - 1]
          if not i == 0:
            soma += malha[i - 1][j]
          if not i == len(malha_y) - 1:
            soma += malha[i + 1][j]
          malha_atualizada[i][j] = fo * (soma) + actualTemp

        if borda_isolada[2] and i == len(malha_x) - 1 and not j == 0 and not j == len(malha_x) - 1:
          # print("Bottom")
          soma = 2*malha[i - 1][j]
          if not j == 0:
            soma += malha[i][j - 1]
          if not j == len(malha_y) - 1:
            soma += malha[i][j + 1]
          malha_atualizada[i][j] = fo * (soma) + actualTemp


        if borda_isolada[3] and j == 0 and not i == 0 and not i == len(malha_x) - 1:
          # print("Left")
          soma = 2*malha[i][j + 1]
          if not i == 0:
            soma += malha[i - 1][j]
          if not i == len(malha_y) - 1:
            soma += malha[i + 1][j]
          malha_atualizada[i][j] = fo * (soma) + actualTemp
            

        if (i != 0 and i != len(malha_x) - 1) and (j != 0 and j != len(malha_y) - 1):
          soma = (malha[i + 1][j] + malha[i - 1][j] + malha[i][j + 1] + malha[i][j - 1])
          malha_atualizada[i][j] = fo * (soma) + actualTemp


        
    malha = np.copy(malha_atualizada)

  # print("malha_atualizada:\n {}".format(malha))
  print ("malha atualizada")
  for i in malha:
    print(i)

  plt.imshow(malha)
  plt.colorbar()

  plt.show()
