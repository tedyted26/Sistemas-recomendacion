
class Noticia:
    def __init__(self, titulo:str, subtitulo:str, fecha,url: str,
                 categoria:str,periodico: str, tags: list, texto: str):
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
        
    def getStringTags(self):
        string = ""
        i = 0
        for i in range(len(self.tags)):
            string = string + self.tags[i]
            if i!=len(self.tags)-1:
                string = string + " - "
        return string


