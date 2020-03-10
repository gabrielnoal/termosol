from funcoesTermosol import *
import math
import numpy as np
from elemento import *
[nn,N,nm,Inc,nc,F,nr,R] = importa('entrada.xlsx')

print("numero de nós: " + str(nn))
print("matriz dos nos: " + str(N))
print("o numero de membros: " + str(nm))
print("matriz de incidencia: " + str(Inc))
# print("numero de cargas: " + str(nc))
# print("vetor carregamento: " + str(F))
# print("numero de restricoes: " + str(nr))
# print("vetor restricoes: " + str(R))

numero_de_nos = nn
matriz_dos_nos = N
o_numero_de_membros = nm
matriz_de_incidencia = Inc
numero_de_cargas = nc
vetor_carregamento = F
numero_de_restricoes = nr
vetor_restricoes = R
numero_i_j = 2 * numero_de_nos
Matriz_base = [[0 for x in range(numero_i_j)] for y in range(numero_i_j)]

elementos = []

for i in range(o_numero_de_membros):
  incidencia = [int(matriz_de_incidencia[i][0]), int(matriz_de_incidencia[i][1])]
  p1 = [matriz_dos_nos[0][incidencia[0] - 1], matriz_dos_nos[1][incidencia[0] - 1]]
  p2 = [matriz_dos_nos[0][incidencia[1] - 1], matriz_dos_nos[1][incidencia[1] - 1]]
  E = matriz_de_incidencia[i][2]
  A = matriz_de_incidencia[i][3]

  elementos.append(Elemento(p1,p2,E,A,incidencia))

  print("Matriz k: ")
  print(elementos[0].matrizK)
  Matriz_base = retorna_matriz_global(incidencia,Matriz_base,elementos[0].matrizK)
  print("")
  print("Matriz Global:")
  print(Matriz_base)
# print(elementos[0].matrizK)
