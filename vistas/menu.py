from tkinter import *
from functools import partial
from tkinter import ttk

class Menu_frame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.place()

    def set_controller(self, controller):
        self.controller = controller

    def create_widgets(self):
        self.bienvenido = Label(self, text="Bienvenido")
        self.bienvenido.place(relx=0, rely=0.4, relwidth=1)

        self.intro = Label(self, text="¿Cómo deseas buscar la noticia?")
        self.intro.place(relx=0, rely=0.5, relwidth=1)

        self.texto = Button(self, text="Búsqueda por texto", command=partial(self.cambiar, "Buscador_por_texto_frame", False))
        self.texto.place(relx=0.05, rely=0.6, relwidth=0.25)

        self.similares = Button(self, text="Búsqueda de noticias similares", command=partial(self.cambiar, "Buscador_frame", False))
        self.similares.place(relx=0.375, rely=0.6, relwidth=0.25)

        self.recomendadas = Button(self, text="Recomendación por contenido", command=partial(self.cambiar, "Buscador_frame", True))
        self.recomendadas.place(relx=0.7, rely=0.6, relwidth=0.25)

    def cambiar(self, pagina, filtros):
        self.controller.show_frame(pagina)
        if pagina=="Buscador_frame": 
            self.controller.frames[pagina].set_con_filtros(filtros)
