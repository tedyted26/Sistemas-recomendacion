
class Noticia:
    def __init__(self, titulo:str, subtitulo:str, fecha,url: str,
                 categoria:str,periodico: str, tags:list, texto: str):
        self.titulo = titulo.replace("\n", "")
        self.subtitulo = subtitulo.replace("\n", "")
        try:
            self.fecha = fecha.replace("\n", "")
        except Exception as e:
            self.fecha = fecha
        self.url = url.replace("\n", "")
        self.categoria = categoria.replace("\n", "")
        self.periodico = periodico.replace("\n", "")
        self.tags = tags
        self.texto = texto

    def getTexto(self):
        return self.texto
    
    def getTitulo(self):
        return self.titulo

    def getSubtitulo(self):
        return self.subtitulo

    def getFecha(self):
        return self.fecha

    def getUrl(self):
        return self.url

    def getCategoria(self):
        return self.categoria

    def getPeriodico(self):
        return self.periodico

    def getTags(self):
        return self.tags

