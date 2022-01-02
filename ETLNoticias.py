from bs4 import BeautifulSoup
from urllib import request as rq
import datetime as dt
import ssl

import re

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

            date_regEx = re.compile(r'(\d+-\d+-\d+T\d*:\d*:\d*)')
            fecha = dt.datetime.strptime(date_regEx.search(fecha).group(), '%Y-%m-%dT%H:%M:%S')
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
    for link in listaLinks:
        n = None
        try:
            url = link
            htmlTemp = rq.urlopen(url, context=ssl.SSLContext()).read()
            soupPag = BeautifulSoup(htmlTemp, 'html.parser')

            titulo = soupPag.find(class_="a_t").text
            subtitulo = soupPag.find(class_="a_st").text
            fecha = soupPag.find(id="article_date_p")["data-date"]
            #Texto
            divCentral = soupPag.find("div", class_="a_c")
            parrafos = divCentral.findAll("p", class_="")
            textoNoticia = ""
            for p in parrafos:
                textoNoticia += " "+ p.text
            #Tags
            tags = [li.text for li in soupPag.find("ul", class_="_df _ls").findAll("li")]

            date_regEx = re.compile(r'(\d+-\d+-\d+T\d*:\d*:\d*)')
            fecha = dt.datetime.strptime(date_regEx.search(fecha).group(), '%Y-%m-%dT%H:%M:%S')
            n = Noticia(titulo, subtitulo, fecha, url, categoria, "El Pais", tags, textoNoticia)
        except Exception as e:
            print(e)
        if n is not None:
            listaNoticias.append(n)

    return listaNoticias

def get20MinutosNews(mainUrl, categoria):
    html = rq.urlopen(mainUrl, context=ssl.SSLContext()).read()
    soup = BeautifulSoup(html, 'html.parser')

    listaNoticias = []
    articulos = soup.findAll("article")
    listaLinks = []
    for a in articulos:
        listaLinks.append(a.find("a")["href"])

    for link in listaLinks:
        try:
            url = link
            htmlTemp = rq.urlopen(url, context=ssl.SSLContext()).read()
            soupPag = BeautifulSoup(htmlTemp, 'html.parser')

            titulo = soupPag.find("div", class_="title").text
            subtitulo = soupPag.find("div", class_="article-intro").text
            fecha = soupPag.find(class_="article-date").text
            tags = [t.text.strip() for t in soupPag.findAll(class_="tag")]
            textoTmp = soupPag.find(class_="article-text").text
            texto = re.sub("\s+", " ", textoTmp)

            date_regEx = re.compile(r'(\d+.\d+.\d+\s*-\s*\d*:\d*)')
            fecha = dt.datetime.strptime(date_regEx.search(fecha).group(), '%d.%m.%Y - %H:%M')

            n = Noticia(titulo, subtitulo, fecha, url, categoria, "20Minutos", tags, texto)
            listaNoticias.append(n)
        except Exception as e:
            print(e)
    return listaNoticias
def guardarNoticias(listaN: list, ruta):
    for i,n in enumerate(listaN):
        try:
            nombreArchivo = f"{n.categoria}.{n.fecha.year}-{n.fecha.month}-{n.fecha.day}.{i}.txt"
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
        except Exception as e:
            print(e)

def elMundo():
    saludElmundo = getElMundoNews("https://www.elmundo.es/ciencia-y-salud/salud.html", "Salud")
    guardarNoticias(saludElmundo, "/Salud/")
    tecnologElmundo = getElMundoNews("https://www.elmundo.es/tecnologia.html", "Tecnologia")
    cienciaElmundo = getElMundoNews("https://www.elmundo.es/ciencia-y-salud/ciencia.html", "Ciencia")
    guardarNoticias(tecnologElmundo, "/Tecnologia/")
    guardarNoticias(cienciaElmundo, "/Ciencia/")
def elPais():
    sanidadElPais = getElPaisNews("https://elpais.com/noticias/sanidad/", "Sanidad")
    guardarNoticias(sanidadElPais, "/Sanidad/")
    tecnologiaElPais = getElPaisNews("https://elpais.com/tecnologia/", "Tecnologia")
    guardarNoticias(tecnologiaElPais, "/Tecnologia/")
    cienciaElPais = getElPaisNews("https://elpais.com/ciencia/", "Ciencia")
    guardarNoticias(cienciaElPais, "/Ciencia/")
def el20Minutos():
    salud20Min = get20MinutosNews("https://www.20minutos.es/salud/", "Salud")
    guardarNoticias(salud20Min, "/Salud/")
    tecnologia20Min = get20MinutosNews("https://www.20minutos.es/tecnologia/ ", "Tecnologia")
    guardarNoticias(tecnologia20Min, "/Tecnologia/")
    ciencia20Min = get20MinutosNews("https://www.20minutos.es/ciencia/", "Ciencia")
    guardarNoticias(ciencia20Min, "/Ciencia/")





