import math
import numpy as np
import copy
from itertools import permutations
from itertools import combinations_with_replacement


def retorna_matriz_global(gdl,matrizK,matrizGlobal,numero_i_j):
    lista_base_index_acumulativa = [1,2,3,4]
    lista_comb_gdl = []
    lista_final_index_acumulativa = []
    lista_soma_acumulativa = []
    lista_soma_parcial_matriz_global = []

    for item in range(len(lista_base_index_acumulativa)):
        for data in lista_base_index_acumulativa:
            lista_final_index_acumulativa.append([lista_base_index_acumulativa[item] - 1 , data - 1])

    for item in range(len(gdl)):
        for data in gdl:
            lista_comb_gdl.append([gdl[item] - 1,data - 1])

    for item in range(len(lista_final_index_acumulativa)):
        soma_matrizK_acumulativa = matrizK[lista_final_index_acumulativa[item][0]][lista_final_index_acumulativa[item][1]]
        lista_soma_acumulativa.append(float(soma_matrizK_acumulativa))

    for item in range(len(lista_final_index_acumulativa)):
        soma_matrizK_atual = matrizK[lista_final_index_acumulativa[item][0]][lista_final_index_acumulativa[item][1]]
        lista_soma_parcial_matriz_global.append(soma_matrizK_atual)

    for item in range(len(lista_comb_gdl)):
        matrizGlobal[lista_comb_gdl[item][0]][lista_comb_gdl[item][1]] += lista_soma_parcial_matriz_global[item]

    return matrizGlobal


def AplicarContorno(matrizk, vetorP, vetor_carregamento):
    matrizk_contornada = copy.deepcopy(matrizk)
    vetorP_contornada = copy.deepcopy(vetorP)
    delLista=[]
    for i in range(len(vetorP_contornada)):
      if (vetorP_contornada[i] =="r"):
        delLista.append(i)
#del linha
    contador=0
    for posD in delLista:
      del matrizk_contornada[posD-contador]
      contador+=1
    
#del coluna
    for linha in range (len(matrizk_contornada)):
      contador=0
      for item in delLista:
        del matrizk_contornada[linha][item-contador]
        contador+=1

#del vetor
    contador=0
    for posD in delLista:
      posD=posD-contador
      del vetorP_contornada[posD]
      contador+=1

    return matrizk_contornada, vetorP_contornada, delLista        

def refazerContorno(matrix_final,matrix_index,numero_de_nos):
    nova_matrix = []
    contador=0
    for i in range(2*numero_de_nos):
      if i in matrix_index:
        nova_matrix.append(0.0)
      else: 
        nova_matrix.append(matrix_final[contador])  
        contador+=1
    return nova_matrix

class Elemento(object):
  def __init__(self, numero, p1, p2, E, A, incidencia):
    self.numero = numero
    self.p1 = p1
    self.p2 = p2
    self.gdls = [p1.gdl[0],p1.gdl[1], p2.gdl[0], p2.gdl[1]]
    self.E = E
    self.A = A
    self.incidencia = incidencia

    [x1, y1] = [p1.x, p1.y]
    [x2, y2] = [p2.x, p2.y]

    self.L = math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
    self.sen = (y2-y1)/self.L
    self.cos = (x2-x1)/self.L
    self.matrizK = self.calcula_K(E,A,self.L,self.sen,self.cos)
    self.epsi = 0
    self.ti = 0
    self.fi = 0

  def calcula_K(self, E,A,L,sen,cos):
    mat_cos_sen = [
      [cos**2 , cos*sen , -(cos**2) , -(cos*sen)],
      [cos*sen , sen**2 , -(cos*sen) , -(sen**2)],
      [-(cos**2) , -(cos*sen) , cos**2 , cos*sen],
      [-(cos*sen) , -(sen**2) , cos*sen , sen**2]
      ]

    matriz_result = [[] for i in range(len(mat_cos_sen))]
    produtoEA = (E*A)/L

    for element in range(len(mat_cos_sen)):
      for item in mat_cos_sen[element]:
        item = float(item)
        Ke = produtoEA * item
        matriz_result[element].append(Ke)

    return matriz_result


  def setForces(self, epsi):
    self.ti = epsi * self.E
    self.fi = self.ti * self.A
    self.epsi = epsi
    return self.ti, self.fi


# tensões internas (ti = epsi * E)
# forcas internas (fi = ti *A)



class Ponto(object):
  def __init__(self, numero, cordenadas):
    self.numero = numero
    self.x = cordenadas[0]
    self.y = cordenadas[1]
    self.gdl = [2 * numero - 1, 2 * numero]
  
