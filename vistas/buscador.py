from tkinter import *
from functools import partial

class Buscador_frame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.pack()

    def set_controller(self, controller):
        self.controller = controller

    #importante para controlar de donde viene la ventana y cómo mostrar la ventana de resultados
    def set_con_filtros(self, filtros=False):
        self.filtros = filtros
        if self.filtros:    #dependiendo de si se utilizará para una cosa u otra se pone un titulo u otro
            self.titulo_ventana.config(text="Buscador de noticias recomendadas")
            
        else:
            self.titulo_ventana.config(text="Buscador de noticias similares")

        

    def create_widgets(self):
        #frame superior con volver y título
        self.frame_superior = Frame(self)
        self.frame_superior.place(relx=0, rely=0, relheight=0.05, relwidth=1)

        self.boton_volver = Button(self.frame_superior, text="Volver", command=self.volver)
        self.boton_volver.place(relx=0, rely=0, relheight=1)

        self.titulo_ventana = Label(self.frame_superior)
        self.titulo_ventana.place(relx=0.05, rely=0, relheight=1)

        #resto de la ventana
        self.frame_contenido = Frame(self)
        self.frame_contenido.place(relx=0, rely= 0.05, relheight=0.95, relwidth=1)

        self.boton_resultados = Button(self.frame_contenido, text="Buscar", command=self.boton_buscar)
        self.boton_resultados.place(relx=0.85, rely= 0.05, relwidth=0.1)

    def volver(self):
        self.controller.show_frame("Menu_frame")
        self.borrar_contenido()

    def borrar_contenido(self):
        #TODO funcion
        print("borrando")

    def rellenar(self):
        #TODO funcion para rellenar
        print("rellenar")

    def boton_buscar(self):
        self.buscar()
        self.controller.show_frame("Resultados_frame")
        self.controller.frames["Resultados_frame"].rellenar(self.filtros)
        self.controller.frames["Resultados_frame"].set_origin("Buscador_frame")
        self.borrar_contenido()
    
    def buscar(self):
        #TODO funcion de buscar
        print("Buscando")