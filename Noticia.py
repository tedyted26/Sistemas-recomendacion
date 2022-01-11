
class Noticia:
    def __init__(self, titulo:str, subtitulo:str, fecha,url: str,
                 categoria:str,periodico: str, tags:list, texto: str):
        self.titulo = titulo
        self.subtitulo = subtitulo
        self.fecha = fecha
        self.url = url
        self.categoria = categoria
        self.periodico = periodico
        self.tags = tags
        self.texto = texto
        self.path = None

    def getStringTags(self):
        string = ""
        i = 0
        for i in range(len(self.tags)):
            string = string + self.tags[i]
            if i!=len(self.tags)-1:
                string = string + " - "
        return string
