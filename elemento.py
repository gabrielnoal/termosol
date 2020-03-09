import math
import numpy as np


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

class Elemento(object):
  def __init__(self, p1, p2, E, A, incidencia):
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



