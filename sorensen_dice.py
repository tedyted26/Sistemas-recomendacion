from Noticia import Noticia
import os
from tratamientoDatos import leerNoticia

def sorensen_dice(noticia:Noticia, top:int):
    listaPeriodicos = ["/El Mundo/","/El Pais/", "/20Minutos/"]
    lista_ratings = {} # diccionario donde vamos a guardar la ruta de la noticia y su rating como parejas de clave valor

    # si no hay etiquetas devolvemos el diccionario vacio
    if noticia.tags == 0:
        return lista_ratings

    #Recorro todos los periodicos
    for periodico in listaPeriodicos:
        rutaPeriodico = os.getcwd() + periodico
        listaTemas = os.listdir(rutaPeriodico)
        #Recorro todos los temas de cada periodico
        for tema in listaTemas:
            rutaTema = rutaPeriodico + tema + "/"
            noticias = os.listdir(rutaTema)
            #Recorro todas las noticias de cada tema
            for nombre_noticia in noticias:
                ruta_noticia2 = periodico + tema + "/" + nombre_noticia
                noticia2 = leerNoticia(os.getcwd() + ruta_noticia2)
                if noticia.url != noticia2.url and len(noticia2.tags) != 0:
                    #Algoritmo
                    tags_en_comun = [value for value in noticia.tags if value in noticia2.tags]
                    numerador_funcion = 2*len(tags_en_comun)
                    denominador_funcion = len(noticia.tags) + len(noticia2.tags)
                    rating = numerador_funcion/denominador_funcion
                    rating = round(rating * 100, 2)

                    if rating != 0:
                        lista_ratings[ruta_noticia2] = rating
    
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