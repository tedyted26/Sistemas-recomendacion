from tkinter import *
from functools import partial

class Menu_frame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.place()

    def set_controller(self, controller):
        self.controller = controller

    def create_widgets(self):
        self.bienvenido = Label(self, text="Bienvenido")
        self.bienvenido.pack()

        self.imagen = Label(self, text="imagen")
        self.imagen.pack()

        self.texto = Label(self, text="¿Cómo deseas buscar la noticia?")

        self.texto = Button(self, text="Búsqueda por texto", command=partial(self.cambiar, "Buscador_por_texto_frame"))
        self.texto.pack()

        self.similares = Button(self, text="Búsqueda por noticias similares", command=partial(self.cambiar, "Buscador_frame"))
        self.similares.pack()

        self.recomendadas = Button(self, text="Búsqueda por noticias recomendadas", command=partial(self.cambiar, "Buscador_frame"))
        self.recomendadas.pack()

    def cambiar(self, pagina):
        self.controller.show_frame(pagina)
