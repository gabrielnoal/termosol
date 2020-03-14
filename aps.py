from funcoesTermosol import *
import math
import numpy as np
from elemento import *
[
  numero_de_nos,
  matriz_dos_nos,
  o_numero_de_membros,
  matriz_de_incidencia,
  numero_de_cargas,
  vetor_carregamento,
  numero_de_restricoes,
  R
] = importa('entrada.xlsx')
vetor_restricoes = [int(r[0]) for r in R]

# print("numero de nós: " + str(numero_de_nos))
# print("matriz dos nos: " + str(matriz_dos_nos))
# print("o numero de membros: " + str(o_numero_de_membros))
# print("matriz de incidencia: " + str(matriz_de_incidencia))
# print("numero de cargas: " + str(numero_de_cargas))
# print("vetor carregamento: " + str(vetor_carregamento))
# print("numero de restricoes: " + str(numero_de_restricoes))
# print("vetor restricoes: " + str(R))

numero_i_j = 2 * numero_de_nos
Matriz_base = [[0 for x in range(numero_i_j)] for y in range(numero_i_j)]
elementos = []
pontos = []
vetorP = []


def main():
  for index_do_no in range(numero_de_nos):
    numero_do_no = index_do_no + 1
    cordenadas = [matriz_dos_nos[0][index_do_no], matriz_dos_nos[1][index_do_no]]
    pontos.append(Ponto(numero_do_no, cordenadas))
    if index_do_no in vetor_restricoes:
      vetorP.append(numero_do_no)
    else:
      vetorP.append('r')


  for i in range(o_numero_de_membros):
    numero_do_elemento = i + 1
    incidencia = [int(matriz_de_incidencia[i][0]), int(matriz_de_incidencia[i][1])]
    p1 = pontos[incidencia[0] - 1]
    p2 = pontos[incidencia[1] - 1]
    print("Elemento: " + str(numero_do_elemento))

    E = matriz_de_incidencia[i][2]
    A = matriz_de_incidencia[i][3]

    elementos.append(Elemento(numero_do_elemento,p1,p2,E,A,incidencia))

  for elemento in elementos:
    print("")
    print("ELEMENTO: " + str(elemento.numero))
    print("E: " + str(elemento.E))
    print("A: " + str(elemento.A))
    print("incidencia: " + str(elemento.incidencia))
    print("L: " + str(elemento.L))
    print("sen: " + str(elemento.sen))
    print("cos: " + str(elemento.cos))
    print("")
    print("matrizK: " + str(elemento.matrizK))
    print("GDL: " + str(elemento.gdls) + "\n")
    matrizGlobal = retorna_matriz_global(elemento.gdls,elemento.matrizK,Matriz_base,numero_i_j)

  #contorno da matriz 
  print("Geral: " + str(matrizGlobal) + "\n")
  print("Tamanho Matriz: " + str(len(matrizGlobal)) + "\n")  
  matrizContornada , vetorContornado = AplicarContorno(matrizGlobal, vetorP)
  print("Matriz Contornada: " + str(matrizContornada) + "\n")
  print("Tamanho Matriz Contornada: " + str(len(matrizContornada)) + "\n")  
  print("Vetor Contornado: " + str(vetorContornado) + "\n")


main()