import math
import os

# LEER PARA USAR:
import numpy

'''
matrixToTFIDF: para transformar la matriz
listToTFIDF: para transformar una lista externa
indexListToTFIDF: para transformar solo una fila de la matriz
'''


# Devuelve la matriz entera en TFIDF
def matrixToTFIDF(matriz, listaIDFopcional = None):
    new_m = []

    if listaIDFopcional is not None:
        listaIDF = listaIDFopcional
    else:
        listaIDF = getIDFlistOfMatriz(matriz)

    for i in range(len(matriz)):
        print("Posicion de lista operandose TFIDF:", i)
        new_m.append(indexListToTFIDF(matriz, i, listaIDF))
    return new_m
#Para transformar una fila de una matriz en TFIDF
def indexListToTFIDF(matriz, index: int, listaIDF: list):
    new_list = [] # Lista a devolver

    v = matriz[index]
    if len(matriz[0]) == len(v):
        n_words = sum(v)
        for i, w in enumerate(v):
            tf = w / n_words

            idf = listaIDF[i]
            result = tf * idf
            new_list.append(result)
    return new_list
def getIDFlistOfMatriz(matriz):
    lista = []
    for i in range(len(matriz[0])):
        print("    + Columna:", i)
        w_in_docs_counter = 0
        for row in matriz:
            r = row
            if r[i] > 0:
                w_in_docs_counter += 1

        oper = len(matriz) / w_in_docs_counter

        idf = math.log10(oper)
        lista.append(idf)
    return lista
# Devuelve una lista externa a la matriz en TFIDF
def listToTFIDF(extVector: list, listaIDF: list):
    new_list = []  # Lista a devolver

    v = extVector.copy()
    lenlista = len(listaIDF)
    lenv = len(v)
    if lenv > lenlista:
        oper = lenv - lenlista
        lista0s = [0 for i in range(oper)]
        listaIDF += lista0s
    # if len(matriz[0]) == len(v):
    n_words = sum(v)
    for i, w in enumerate(v):
        tf = w / n_words

        idf = listaIDF[i]
        result = tf * idf
        new_list.append(result)

    return new_list

def testTransformMatrizToTFIDF():
    matriz = numpy.loadtxt("matriz.txt")
    m2 = matrixToTFIDF(matriz)
    print()

