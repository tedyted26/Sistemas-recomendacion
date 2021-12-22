#pip install -U spacy
#python -m spacy download es
import spacy 
#pip install --user -U nltk
import nltk
from nltk import SnowballStemmer
import os
from pathlib import Path

def tokenizacion(rutaFichero):
    nlp = spacy.load('es_core_news_sm')
    
    f = open (rutaFichero,'r')
    texto = f.read() 

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
    listaParada = tratamientoBasico(tokenizacion("lista1.txt"))
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

def listaVocabulario():
    listaFicheros = ["/El Mundo/Ciencia/","/El Mundo/Salud/","/El Mundo/Tecnologia/","/El Pais/Ciencia/","/El Pais/Sanidad/","/El Pais/Tecnologia/"]
    listaPalabras = []
    for carpeta in listaFicheros:
        ruta = os.getcwd() + carpeta
        noticias = os.listdir(ruta)
        for noticia in noticias:
            tokens = tokenizacion(ruta+noticia)
            tokens = tratamientoBasico(tokens)
            tokens = listaParada(tokens)
            tokens = stemming(tokens)

        for token in tokens:
            encontrado = False
            i = 0
            while (encontrado==False and i < len(listaPalabras) ):
                if token == listaPalabras[i]:
                    encontrado = True
                i+=1
            if encontrado==False:
                listaPalabras.append(token)
    return listaPalabras

lista = listaVocabulario()
print(lista)
f = open("lista.txt", "w")
for elemento in lista:
    f.write(elemento+"\n")
f.close()