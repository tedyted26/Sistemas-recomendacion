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
        self.bienvenido.place(relx=0, rely=0.3, relwidth=1)

        self.imagen = Label(self, text="imagen")
        self.imagen.place(relx=0, rely=0.4, relwidth=1)

        self.intro = Label(self, text="¿Cómo deseas buscar la noticia?")
        self.intro.place(relx=0, rely=0.5, relwidth=1)

        self.texto = Button(self, text="Búsqueda por texto", command=partial(self.cambiar, "Buscador_por_texto_frame"))
        self.texto.place(relx=0.05, rely=0.6, relwidth=0.25)

        self.similares = Button(self, text="Búsqueda por noticias similares", command=partial(self.cambiar, "Buscador_frame"))
        self.similares.place(relx=0.375, rely=0.6, relwidth=0.25)

        self.recomendadas = Button(self, text="Búsqueda por noticias recomendadas", command=partial(self.cambiar, "Buscador_frame"))
        self.recomendadas.place(relx=0.7, rely=0.6, relwidth=0.25)

    def cambiar(self, pagina):
        self.controller.show_frame(pagina)
