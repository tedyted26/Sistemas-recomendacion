from tkinter import *
from functools import partial
from tkinter import ttk
import os
import sys

# código copiado de GeeksforGeeks.org para conseguir importar la clase Noticia
  
# getting the name of the directory
# where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))
  
# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)
  
# adding the parent directory to 
# the sys.path.
sys.path.append(parent)

import teorema_coseno

class Buscador_por_texto_frame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.pack()

    def set_controller(self, controller):
        self.controller = controller

    def create_widgets(self):
        #frame superior con título y boton de atrás
        self.frame_superior = Frame(self)
        self.frame_superior.place(relx=0, rely=0, relheight=0.05, relwidth=1)

        self.boton_volver = Button(self.frame_superior, text="Volver", command=partial(self.volver, "Menu_frame"))
        self.boton_volver.place(relx=0, rely=0, relheight=1)

        self.titulo_ventana = Label(self.frame_superior, text="Buscador por texto")
        self.titulo_ventana.place(relx=0.05, rely=0, relheight=1)

        #frame con los contenidos de la ventana (en este caso input para la búsqueda y boton)
        self.frame_buscador = Frame(self)
        self.frame_buscador.place(relx=0, rely= 0.05, relheight=0.95, relwidth=1)

        self.titulo_buscador = Label(self.frame_buscador, text="¿Qué desea buscar?")
        self.titulo_buscador.place(relx=0.3, rely=0.3, relwidth=0.4)

        self.input_buscador = Entry(self.frame_buscador)
        self.input_buscador.place(relx=0.3, rely=0.4, relwidth=0.4)

        periodicos = ["El Mundo", "El País", "20 Minutos"]
        top = [3, 5, 10]

        self.label_periodicos = Label(self.frame_buscador, text="Periódico:")
        self.label_periodicos.place(relx=0.3, rely=0.5)

        self.periodicos_combobox = ttk.Combobox(self.frame_buscador, values=periodicos, state="readonly")
        self.periodicos_combobox.current(0)
        self.periodicos_combobox.place(relx=0.37, rely= 0.5, relwidth=0.2)

        self.label_top = Label(self.frame_buscador, text="Top:")
        self.label_top.place(relx=0.61, rely=0.5)

        self.top_combobox = ttk.Combobox(self.frame_buscador, values=top, state="readonly")
        self.top_combobox.current(0)
        self.top_combobox.place(relx=0.65, rely= 0.5, relwidth=0.05)

        self.boton_buscar = Button(self.frame_buscador, text="Buscar", command=self.boton_buscar)
        self.boton_buscar.place(relx=0.45, rely=0.6, relwidth=0.1)

        self.label_error = Label(self.frame_buscador, text="No puede dejar el campo de texto vacío", fg="red")

    def volver(self, pagina):
        self.controller.show_frame(pagina)
        self.borrar_contenido()
    
    def boton_buscar(self): 
        texto_buscado = self.input_buscador.get()
        top = self.top_combobox.get()

        if texto_buscado=="":
            self.label_error.place(relx=0, rely=0.7, relwidth=1) 
        else:      
            noticias_similares = self.buscar(texto_buscado, top)
            self.controller.show_frame("Resultados_frame")
            self.controller.frames["Resultados_frame"].rellenar(noticias_similares, False)
            self.controller.frames["Resultados_frame"].set_origin("Buscador_por_texto_frame")
            self.controller.frames["Resultados_frame"].set_titulo_noticia(texto_buscado)
            self.borrar_contenido()

    def borrar_contenido(self):
        self.input_buscador.delete(0,"end")
        if self.label_error.winfo_ismapped:
           self.label_error.place_forget()
