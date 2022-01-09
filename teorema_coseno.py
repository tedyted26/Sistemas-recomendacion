import Noticia

# pasamos un texto para buscar noticias a partir de su similitud
def texto_coseno(texto:str, top:int):
    lista_ratings = {} # diccionario donde vamos a guardar la ruta de la noticia y su rating como parejas de clave valor

    # procesar texto
    # for noticia in noticias guardarla en doc2 y hacer el teorema del coseno con texto. Guardar noticia y la similitud en el diccionario

    # Ordeno el diccionario por el valor del rating
    lista = sorted(lista_ratings.items(), key=lambda x: x[1], reverse=True)
    lista_ratings.clear()
    
    i = 0
    for key in lista:
        if i<top:
            lista_ratings[key[0]] = key[1]
            i = i+1
        else:
            break

    return lista_ratings

#pasamos una noticia para buscar otras similares
def noticias_coseno(noticia:Noticia, top:int):
    lista_ratings = {} # diccionario donde vamos a guardar la ruta de la noticia y su rating como parejas de clave valor

    # primero coger la noticia y comprobar en que index está de la lista de ficheros leidos
    # luego coger ese index y buscarlo en la matriz
    # teniendo la fila de la matriz coger la lista y guardarla en doc1
    # for noticia in noticias guardarla en doc2 y hacer el teorema del coseno con doc1. Guardar noticia y la similitud en el diccionario

    # Ordeno el diccionario por el valor del rating
    lista = sorted(lista_ratings.items(), key=lambda x: x[1], reverse=True)
    lista_ratings.clear()
    
    i = 0
    for key in lista:
        if i<top:
            lista_ratings[key[0]] = key[1]
            i = i+1
        else:
            break

    return lista_ratings

#Metodo para calcular la similitud en función del coseno
def coseno(doc1, doc2):
    numerador = 0
    cuadradosDoc1 = 0
    cuadradosDoc2 = 0
    i = 0
    for i in range(len(doc1)):
        numerador += (doc1[i] * doc2[i])
        cuadradosDoc1 += doc1[i]**2
        cuadradosDoc2 += doc2[i]**2
    raizDoc1 = cuadradosDoc1**(0.5)
    raizDoc2 = cuadradosDoc2**(0.5)
    denominador = raizDoc1 * raizDoc2
    return numerador/denominador