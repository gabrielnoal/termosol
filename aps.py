from funcoesTermosol import *
import math
import numpy as np
from elemento import *
[
  numero_de_nos,
  matriz_dos_nos,
  numero_de_membros,
  matriz_de_incidencia,
  numero_de_cargas,
  vetor_carregamento,
  numero_de_restricoes,
  vetor_restricoes
] = importa('entrada.xlsx')
vetor_restricoes = [int(r[0]) for r in vetor_restricoes]
vetor_carregamento = [c[0] for c in vetor_carregamento]

# print("numero de nós: {}".format(numero_de_nos))
# print("matriz dos nos: {}".format(matriz_dos_nos))
# print("o numero de membros: {}".format(numero_de_membros))
# print("matriz de incidencia: {}".format(matriz_de_incidencia))
# print("numero de cargas: {}".format(numero_de_cargas))
# print("vetor carregamento: {}".format(vetor_carregamento))
# print("numero de restricoes: {}".format(numero_de_restricoes))
# print("vetor restricoes: {}".format(vetor_restricoes))

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

  for gdl_index in range(2*numero_de_membros):
    gdl = gdl_index + 1
    if gdl_index in vetor_restricoes:
      vetorP.append('r')
    else:
      vetorP.append(gdl)

  for i in range(numero_de_membros):
    numero_do_elemento = i + 1
    incidencia = [int(matriz_de_incidencia[i][0]), int(matriz_de_incidencia[i][1])]
    p1 = pontos[incidencia[0] - 1]
    p2 = pontos[incidencia[1] - 1]
    print("Elemento: {}".format(numero_do_elemento))

    E = matriz_de_incidencia[i][2]
    A = matriz_de_incidencia[i][3]

    elementos.append(Elemento(numero_do_elemento,p1,p2,E,A,incidencia))

  for elemento in elementos:
    print("ELEMENTO: {}".format(elemento.numero))
    print("E: {}".format(elemento.E))
    print("A: {}".format(elemento.A))
    print("incidencia: {}".format(elemento.incidencia))
    print("L: {}".format(elemento.L))
    print("sen: {}".format(elemento.sen))
    print("cos: {}".format(elemento.cos))
    print("")
    print("matrizK: {}".format(elemento.matrizK))
    print("GDL: {}".format(elemento.gdls) + "\n\n")
    matrizGlobal = retorna_matriz_global(elemento.gdls, elemento.matrizK, Matriz_base, numero_i_j)

  #contorno da matriz 
  print("Matriz Global {}x{}: {}".format(len(matrizGlobal), len(matrizGlobal[0]), matrizGlobal) + "\n")
  print("vetorP: {}".format(vetorP))
  matrizContornada , vetorContornado = AplicarContorno(matrizGlobal, vetorP, vetor_carregamento)
  print("Matriz Contornada {}x{} : {}".format(len(matrizContornada),len(matrizContornada[0]),matrizContornada)  + "\n")
  print("VetorP Contornado: {}".format(vetorContornado) + "\n")

  # vetor_deslocamento = np.linalg.solve(matrizContornada,vetorContornado)
  # print("Vetor deslocamento: {}".format(vetor_deslocamento) + "\n")




main()