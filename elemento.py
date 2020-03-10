import math
import numpy as np
from itertools import permutations

def retorna_K(p1,p2,E,A,L,sen,cos):
  mat_cos_sen = [
    [cos**2 , cos*sen , -cos**2 , -cos*sen],
    [cos*sen , sen**2 , -cos*sen , -sen**2],
    [-cos**2 , -cos*sen , cos**2 , cos*sen],
    [-cos*sen , -sen**2 , cos*sen , sen**2]
    ]

  matriz_result = [[] for i in range(len(mat_cos_sen))]
  produtoEA = (E*A)/L
  for element in range(len(mat_cos_sen)):
    for item in mat_cos_sen[element]:
      item = int(item)
      Ke = produtoEA * item
      matriz_result[element].append(Ke)

  return matriz_result

def retorna_matriz_global(incidencia,mb,matrizK):
    listas_graus_de_liberdade = [[] for i in range(len(incidencia) + 2)]

    listas_combinacoes_incidencia[0] = [incidencia[0],incidencia[0]]
    listas_combinacoes_incidencia[1] = [incidencia[0],incidencia[1]]
    listas_combinacoes_incidencia[2] = [incidencia[1],incidencia[0]]
    listas_combinacoes_incidencia[3] = [incidencia[1],incidencia[1]]

    # for item in range(len(listas_combinacoes_incidencia)):
    #     soma_acumulativa_matriz_geral = mb[listas_combinacoes_incidencia[item][0]][listas_combinacoes_incidencia[item][1]]
    #     soma_parcial_matriz_k = matrizK[listas_combinacoes_incidencia[item][0]][listas_combinacoes_incidencia[item][1]]
    # 
    #     soma_final_matriz_geral = soma_acumulativa_matriz_geral + soma_parcial_matriz_k
    #     mb[listas_combinacoes_incidencia[item][0]][listas_combinacoes_incidencia[item][1]] += soma_final_matriz_geral

    return mb

class Elemento(object):
  def __init__(self, numero, p1, p2, E, A, incidencia):
    self.numero = numero
    self.p1 = p1
    self.p2 = p2
    self.E = E
    self.A = A
    self.incidencia = incidencia
    [x1, y1] = p1
    [x2, y2] = p2

    self.L = math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
    self.sen = (y2-y1)/self.L
    self.cos = (x2-x1)/self.L
    self.matrizK = retorna_K(p1,p2,E,A,self.L,self.sen,self.cos)

class Ponto(object):
  def __init__(self, numero, cordenadas, gdlx, gdly):
    self.numero = numero
    [x, y] = cordenadas
    self.x = x
    self.y = y
    self.gdlx = gdlx
    self.gdly = gdly
    