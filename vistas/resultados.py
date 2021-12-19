from tkinter import *
from functools import partial

class Resultados_frame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.place()

    def set_controller(self, controller):
        self.controller = controller

    #funcion necesaria para poder volver luego a la página de búsqueda en vez de volver al menu principal
    #origin debe ser el nombre del frame tal cual viene en el diccionario de frames de recomendador
    def set_origin(self, origin):
        self.origin = origin

    def create_widgets(self):
        #frame superior con título y boton de atrás
        self.frame_superior = Frame(self)
        self.frame_superior.place(relx=0, rely=0, relheight=0.05, relwidth=1)

        self.boton_volver = Button(self.frame_superior, text="Volver", command=self.volver)
        self.boton_volver.place(relx=0, rely=0, relheight=1)

        self.titulo_ventana = Label(self.frame_superior, text="Resultados")
        self.titulo_ventana.place(relx=0.05, rely=0, relheight=1)

    def volver(self):
        self.controller.show_frame(self.origin)
    
    def rellenar(self, filtros=False):
        #TODO rellenar según la busqueda
        #si viene de la página de recomendaciones debe tener los campos de filtros visibles
        if filtros:
            self.show_filtros()
    
    def show_filtros(self):
        #TODO añadir frame con filtros y cambiar ligeramente la posicion del resto de contenidos
        print("sjsjj")