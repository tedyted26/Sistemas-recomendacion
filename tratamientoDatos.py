#pip install -U spacy
#python -m spacy download es
import spacy 
#pip install --user -U nltk
import nltk
from nltk import SnowballStemmer
import os
from pathlib import Path
from Noticia import Noticia
import numpy


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
    listaTexto = texto.split(sep="####")
    noticia = Noticia(listaTexto[0],listaTexto[1],listaTexto[2],listaTexto[3],listaTexto[4],listaTexto[6],listaTexto[6],listaTexto[7])
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

def stemming(tokens):
    spanishstemmer=SnowballStemmer('spanish')
    stems = [spanishstemmer.stem(token) for token in tokens]
    return stems

#Metodo para generar el diccionario
def generarDiccionario():
    diccionario = []
    ficherosTratados = []
    if os.path.isfile(rutaDiccionario): #Compruebo si existe el fichero
        diccionario = tratamientoBasico(tokenizacion(rutaDiccionario))
    if os.path.isfile(rutaFicherosTratados): #Compruebo si existe el fichero
        f = open (rutaFicherosTratados,'r')
        texto = f.read()
        ficherosTratados = texto.splitlines()
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
                    tokens = stemming(tokens)
                    #Compruebo si existe el token en la lista
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
    
    generarMatriz()
    return diccionario

#Metodo
def generarMatriz():
    diccionario = tratamientoBasico(tokenizacion(rutaDiccionario))
    noticias = tratamientoBasico(tokenizacion(rutaFicherosTratados))

    if os.path.isfile(rutaMatriz): #Compruebo si existe el fichero
        print("Metodo leer matriz")
    else:
        matriz = numpy.zeros(5,3)


#Main
generarDiccionario()