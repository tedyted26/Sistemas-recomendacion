#pip install -U spacy
#python -m spacy download es
import spacy 
#pip install --user -U nltk
import nltk
from nltk import SnowballStemmer


def tokenizacion(rutaFichero):
    nlp = spacy.load('es_core_news_sm')
    
    f = open (rutaFichero,'r')
    texto = f.read() 

    doc = nlp(texto) # Crea un objeto de spacy tipo nlp
    tokens = [t.orth_ for t in doc] # Crea una lista con las palabras del texto
    tokens.sort()
    return tokens

def tratamientoBasico(tokens):
    caracteres = "0123456789ºª!·$%&/()=|@#~€¬'?¡¿`+^*[]´¨}{,.-;:_<>\n \""
    listaTratada = []
    for token in tokens :
        for i in range (len(caracteres)):
            token = token.replace(caracteres[i],"")
        if(token != ""):
            listaTratada.append(token.lower())
    tokens.sort()
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