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
] = importa('testeFinal.xlsx')
vetor_restricoes = [int(r[0]) for r in vetor_restricoes]
vetor_carregamento = [c[0] for c in vetor_carregamento]

# print("numero de nós: {}".format(numero_de_nos))
print("matriz dos nos: {}".format(matriz_dos_nos))
# print("o numero de membros: {}".format(numero_de_membros))
# print("matriz de incidencia: {}".format(matriz_de_incidencia))
# print("numero de cargas: {}".format(numero_de_cargas))
print("vetor carregamento {}x1: {}".format(len(vetor_carregamento),vetor_carregamento))
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


  vetorP_forcas = []
  for gdl_index in range(2*numero_de_nos):
    gdl = gdl_index + 1
    if gdl_index in vetor_restricoes:
      vetorP.append('r')
      vetorP_forcas.append(0.0)
    else:
      vetorP.append(gdl)
      vetorP_forcas.append(vetor_carregamento[gdl_index])


  print("vetorP: {}".format(vetorP))
  # print("vetorP_forcas: {}".format(vetorP_forcas))

  for i in range(numero_de_membros):
    numero_do_elemento = i + 1
    incidencia = [int(matriz_de_incidencia[i][0]), int(matriz_de_incidencia[i][1])]
    p1 = pontos[incidencia[0] - 1]
    p2 = pontos[incidencia[1] - 1]
    # print("Elemento: {}".format(numero_do_elemento))

    E = matriz_de_incidencia[i][2]
    A = matriz_de_incidencia[i][3]

    elementos.append(Elemento(numero_do_elemento,p1,p2,E,A,incidencia))

  for elemento in elementos:
    # print("ELEMENTO: {}".format(elemento.numero))
    # print("E: {}".format(elemento.E))
    # print("A: {}".format(elemento.A))
    # print("incidencia: {}".format(elemento.incidencia))
    # print("L: {}".format(elemento.L))
    # print("sen: {}".format(elemento.sen))
    # print("cos: {}".format(elemento.cos))
    # print("")
    # print("matrizK: {}".format(elemento.matrizK))
    # print("GDL: {}".format(elemento.gdls) + "\n\n")
    matrizGlobal = retorna_matriz_global(elemento.gdls, elemento.matrizK, Matriz_base, numero_i_j)

  #contorno da matriz 
  print("Matriz Global {}x{}: {}".format(len(matrizGlobal), len(matrizGlobal[0]), matrizGlobal) + "\n")
  matrizContornada , vetorContornado, index_do_corte = AplicarContorno(matrizGlobal, vetorP, vetor_carregamento)
  # print("Matriz Contornada {}x{} : {}".format(len(matrizContornada),len(matrizContornada[0]),matrizContornada)  + "\n")

  for i in range(len(vetorContornado)):
    vetorContornado[i] = vetor_carregamento[vetorContornado[i] - 1]
  # print("VetorP {}x1 Contornado: {}".format(len(vetorContornado),vetorContornado) + "\n")


  vetor_deslocamento_contornado = np.linalg.solve(matrizContornada,vetorContornado)
  # print("pre_vetor_deslocamento {}x1: {}".format(len(vetor_deslocamento_contornado), vetor_deslocamento_contornado))

  vetor_deslcamento_completo = refazerContorno(vetor_deslocamento_contornado, index_do_corte, numero_de_nos)
  
  # print("Vetor deslocamento completo: {}x1 {}".format(len(vetor_deslcamento_completo),vetor_deslcamento_completo) + "\n")
  # print("Vetor deslocamento: {}".format(vetor_deslocamento_contornado) + "\n")
  ##deformação
  lista_ti = []
  lista_fi = []
  list_epsi = []


  for elemento in elementos:
    sen = elemento.sen
    cos = elemento.cos
    l = elemento.L
    matriz = [-cos, -sen, cos, sen]
    vetor_def=[]
    for gdl in elemento.gdls:
      vetor_def.append(vetor_deslcamento_completo[gdl-1])
    epsi = (1/l) * np.dot(matriz,vetor_def)
    ti, fi = elemento.setForces(epsi)
    lista_ti.append(ti)
    lista_fi.append(fi)
    list_epsi.append(epsi)

  #Reação de Apoio
  dot =  np.dot(matrizGlobal,vetor_deslcamento_completo)
  reacoes_de_apoio = []
  for i in range(len(vetorP)):
    if vetorP[i] == 'r':
      reacoes_de_apoio.append(dot[i])
  
  print("Reações de apoio: {}".format(reacoes_de_apoio))
  geraSaida("saida.txt", reacoes_de_apoio, vetor_deslcamento_completo, list_epsi, lista_fi, lista_ti)
  plota(matriz_dos_nos, matriz_de_incidencia)

    

main()