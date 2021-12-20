from bs4 import BeautifulSoup
from urllib import request as rq
import datetime as dt

import os
from pathlib import Path

#pip install -U spacy
import spacy 

from Noticia import Noticia

def getElMundoNews(mainUrl, categoria):
    html = rq.urlopen(mainUrl).read()
    soup = BeautifulSoup(html, 'html.parser')

    listalinks = soup.findAll("a", class_="ue-c-cover-content__link")[:20]
    listaNoticias = []
    #print(rq.urlopen(listalinks[0]["href"]).read())
    for link in listalinks:
        n = None
        try:
            url = link["href"]
            htmlTemp = rq.urlopen(url).read()
            soupPag = BeautifulSoup(htmlTemp, 'html.parser')

            divCuerpo = soupPag.find("div", class_="ue-l-article__body ue-c-article__body")
            titulo = soupPag.find(class_="ue-c-article__headline js-headline").text
            subtitulo = soupPag.find(class_="ue-c-article__standfirst").text
            fecha = soupPag.find(class_="ue-c-article__publishdate").find("time")["datetime"]
            textoNoticia = ""
            for p in divCuerpo.find_all("p"):
                textoNoticia += " "+p.text
            tags = []
            for tag in soupPag.findAll(class_="ue-c-article__tags-item"):
                tags.append(tag.text)
            n = Noticia(titulo,subtitulo,fecha, url, categoria,"El Mundo", tags, textoNoticia)
        except Exception as e:
            pass
        if n is not None:
            listaNoticias.append(n)

    return listaNoticias


def guardarNoticias(listaN: list, ruta):
    for i,n in enumerate(listaN):
        fecha = dt.datetime.strptime(n.fecha, '%Y-%m-%dT%H:%M:%SZ')
        nombreArchivo = f"{n.categoria}.{fecha.year}-{fecha.month}-{fecha.day}.{i}.txt"
        print(nombreArchivo)

        # Path(ruta).mkdir(parents=True, exist_ok=True)
        os.mkdir(ruta)
        f = open(os.path.join(ruta, nombreArchivo), "w")
        f.write("Now the file has more content!")
        f.close()

def tokenizacion(rutaFichero):
    #python -m spacy download es
    nlp = spacy.load('es_core_news_sm')
    f = open (rutaFichero,'r')
    mensaje = f.read()  
    print(mensaje)
            

saludElmundo= getElMundoNews("https://www.elmundo.es/ciencia-y-salud/salud.html", "Salud")
# tecnologElmundo = getElMundoNews("https://www.elmundo.es/tecnologia.html", "Tecnologia")
# cienciaElmundo = getElMundoNews("https://www.elmundo.es/ciencia-y-salud/ciencia.html", "Ciencia")
tokenizacion("D:/Users/Mario/Desktop/uwu.txt")
guardarNoticias(saludElmundo, "/Salud/")