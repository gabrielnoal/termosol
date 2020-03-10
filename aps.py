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
pontos = []

for index_do_no in range(numero_de_nos):
  numero_do_no = index_do_no + 1
  cordenadas = [matriz_dos_nos[0][index_do_no], matriz_dos_nos[1][index_do_no]]
  pontos.append(Ponto(numero_do_no, cordenadas))

for i in range(o_numero_de_membros):
  numero_do_elemento = i + 1
  incidencia = [int(matriz_de_incidencia[i][0]), int(matriz_de_incidencia[i][1])]
  p1 = pontos[incidencia[0] - 1]
  p2 = pontos[incidencia[1] - 1]
  print("Elemento: " + str(numero_do_elemento))

  E = matriz_de_incidencia[i][2]
  A = matriz_de_incidencia[i][3]

  elementos.append(Elemento(numero_do_elemento,p1,p2,E,A,incidencia))

#   print("Matriz k: ")
#   print(elementos[0].matrizK)
#   Matriz_base = retorna_matriz_global(incidencia,Matriz_base,elementos[0].matrizK)
#   print("")
#   print("Matriz Global:")
#   print(Matriz_base)
# print(elementos[0].matrizK)

for elemento in elementos:
  print("ELEMENTO: " + str(elemento.numero))
  print("E: " + str(elemento.E))
  print("A: " + str(elemento.A))
  print("incidencia: " + str(elemento.incidencia))
  print("L: " + str(elemento.L))
  print("sen: " + str(elemento.sen))
  print("cos: " + str(elemento.cos))
  print("matrizK: " + str(elemento.matrizK))
  print("GDL: " + str(elemento.gdls) + "\n")