from bs4 import BeautifulSoup
from urllib import request as rq
import datetime as dt
import ssl

import os
from pathlib import Path

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

def getElPaisNews(mainUrl, categoria):
    html = rq.urlopen(mainUrl, context=ssl.SSLContext()).read()
    soup = BeautifulSoup(html, 'html.parser')

    listaNoticias = []
    articulos = soup.findAll("article")
    listaLinks = []
    for a in articulos:
        link = "https://elpais.com" + a.find("a")["href"]
        listaLinks.append(link)
    print(listaLinks)
    #return listaNoticias

def guardarNoticias(listaN: list, ruta):
    for i,n in enumerate(listaN):
        fecha = dt.datetime.strptime(n.fecha, '%Y-%m-%dT%H:%M:%SZ')
        nombreArchivo = f"{n.categoria}.{fecha.year}-{fecha.month}-{fecha.day}.{i}.txt"
        print(nombreArchivo)

        s = "####"
        texto = f"{n.titulo}{s}\n" \
                f"{n.subtitulo}{s}\n" \
                f"{n.fecha}{s}\n" \
                f"{n.url}{s}\n" \
                f"{n.categoria}{s}\n" \
                f"{n.periodico}{s}\n" \
                f"{n.tags}{s}\n" \
                f"{n.texto}{s}\n" \
            # Path(ruta).mkdir(parents=True, exist_ok=True)
        cd = os.getcwd() + "/"+n.periodico

        if not os.path.exists(cd):
            os.mkdir(cd)
        cd2 = cd + ruta

        if not os.path.exists(cd2):
            os.mkdir(cd2)
        f = open(os.path.join(cd2, nombreArchivo), "w")
        f.write(texto)
        f.close()

def elMundo():
    saludElmundo = getElMundoNews("https://www.elmundo.es/ciencia-y-salud/salud.html", "Salud")
    guardarNoticias(saludElmundo, "/Salud/")
    tecnologElmundo = getElMundoNews("https://www.elmundo.es/tecnologia.html", "Tecnologia")
    cienciaElmundo = getElMundoNews("https://www.elmundo.es/ciencia-y-salud/ciencia.html", "Ciencia")
    guardarNoticias(tecnologElmundo, "/Tecnologia/")
    guardarNoticias(cienciaElmundo, "/Ciencia/")


getElPaisNews("https://elpais.com/noticias/sanidad/","Sanidad")


