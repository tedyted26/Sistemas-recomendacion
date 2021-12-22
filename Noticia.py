
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

    def getTexto(self):
        return self.texto
    
    def getTitulo(self):
        return self.titulo
