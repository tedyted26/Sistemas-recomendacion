#pip install -U spacy
#python -m spacy download es
from nltk import text
import spacy 

import os
from pathlib import Path
from Noticia import Noticia
import numpy
import ast


#Variables globales
listaPeriodicos = ["/El Mundo/","/El Pais/"]
rutaListaParada = "listaParada.txt"
rutaDiccionario = "diccionario.txt"
rutaFicherosTratados = "ficherosLeidos.txt"
rutaMatriz = "matriz.txt"

#Metodo de lectura de noticia
def leerNoticia(rutaFichero):
    print(rutaFichero)
    f = open (rutaFichero,'r')
    texto = f.read()
    listaTexto = texto.split(sep="####\n")
    noticia = Noticia(listaTexto[0],listaTexto[1],listaTexto[2],listaTexto[3],listaTexto[4],listaTexto[5],ast.literal_eval(listaTexto[6]),listaTexto[7])
    return noticia

#Metodos de Tratamiento de ficheros
def tokenizacion(rutaFichero):
    nlp = spacy.load('es_core_news_sm')
    
    if rutaFichero==rutaListaParada or rutaFichero==rutaDiccionario:
        f = open (rutaFichero,'r')
        texto = f.read() 
    else:
        texto = leerNoticia(rutaFichero).getTexto()

    doc = nlp(texto) # Crea un objeto de spacy tipo nlp
    tokens = [t.orth_ for t in doc] # Crea una lista con las palabras del texto
    return tokens

def tratamientoBasico(tokens):
    caracteres = "0123456789ºª!·$%&/()=|@#~€¬'?¡¿`+^*[]´¨}{,.-;:_<>\n \""
    listaTratada = []
    for token in tokens :
        for i in range (len(caracteres)):
            token = token.replace(caracteres[i],"")
        if(token != ""):
            listaTratada.append(token.lower())
    return listaTratada

def listaParada(tokens):
    listaParada = tratamientoBasico(tokenizacion(rutaListaParada))
    listaDepurada = []
    for token in tokens:
        encontrado = False
        i=0
        while (encontrado==False and i<len(listaParada)):
            if (token==listaParada[i]):
                encontrado=True
            i+=1
        if encontrado==False and len(token)>2:
            listaDepurada.append(token)
    return listaDepurada

def lematizacion(tokens):
    nlp = spacy.load('es_core_news_sm')
    texto = ""
    for token in tokens:
        texto += token + " "
    doc = nlp(texto)
    lemmas = [tok.lemma_ for tok in doc]
    return lemmas

def leerFicheros(rutaFichero):
    f = open (rutaFichero,'r')
    texto = f.read()
    fichero = texto.splitlines()
    return fichero


#Metodo para generar el diccionario
def generarDiccionario():
    diccionario = []
    ficherosTratados = []
    matriz = []
    if os.path.isfile(rutaDiccionario): #Compruebo si existe el fichero
        diccionario = leerFicheros(rutaDiccionario)
    if os.path.isfile(rutaFicherosTratados): #Compruebo si existe el fichero
        ficherosTratados = leerFicheros(rutaFicherosTratados)
    #Recorro todos los periodicos
    for periodico in listaPeriodicos:
        rutaPeriodico = os.getcwd() + periodico
        listaTemas = os.listdir(rutaPeriodico)
        #Recorro todos los temas de cada periodico
        for tema in listaTemas:
            rutaTema = rutaPeriodico + tema + "/"
            noticias = os.listdir(rutaTema)
            #Recorro todas las noticias de cada tema
            for noticia in noticias:
                #Compruebo si la noticia no la había tratado ya
                noticiaActual = periodico + tema + "/" + noticia
                if noticiaActual not in ficherosTratados:
                    #Tratamiento de la noticia
                    tokens = tokenizacion(rutaTema+noticia)
                    tokens = tratamientoBasico(tokens)
                    tokens = listaParada(tokens)
                    tokens = lematizacion(tokens)
                    
                    #Compruebo si existe el token en la lista y sino lo añado al diccionario
                    for token in tokens:
                        if token not in diccionario:
                            diccionario.append(token)
                        
                    #Guardo la noticia en los ficheros tratados para no volver a analizarlo           
                    ficherosTratados.append(noticiaActual)
    #Guardo en ficheros el diccionaro y las noticias tratadas
    #Diccionario
    f = open(rutaDiccionario, "w")
    for elemento in diccionario:
        f.write(elemento+"\n")
    f.close()

    #Noticias tratadas
    f = open(rutaFicherosTratados, "w")
    for elemento in ficherosTratados:
        f.write(elemento+"\n")
    f.close()
    
    return diccionario

#Metodo
def generarMatriz():
    #leo el diccionario
    diccionario = leerFicheros(rutaDiccionario)
    #leo el fichero de las noticias tratadas
    noticias = leerFicheros(rutaFicherosTratados)

    if os.path.isfile(rutaMatriz): #Compruebo si existe el fichero
        matriz = numpy.loadtxt(rutaMatriz)
        print(matriz)
    else:
        matriz = numpy.zeros((len(noticias),len(diccionario)),dtype=int)
        i=0
        for noticia in noticias:
            tokens = tokenizacion(os.getcwd()+noticia)
            tokens = tratamientoBasico(tokens)
            tokens = listaParada(tokens)
            tokens = lematizacion(tokens)
            for token in tokens:
                matriz[i][diccionario.index(token)] +=1
            i+=1
        print(matriz)
        numpy.savetxt(rutaMatriz,matriz,fmt='%i')

#Main
generarMatriz()
