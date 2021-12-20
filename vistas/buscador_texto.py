from tkinter import *
from functools import partial

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

        self.boton_buscar = Button(self.frame_buscador, text="Buscar", command=self.boton_buscar)
        self.boton_buscar.place(relx=0.45, rely=0.5, relwidth=0.1)

    def volver(self, pagina):
        self.controller.show_frame(pagina)
        self.borrar_contenido()
    
    def boton_buscar(self): 
        texto_buscado = self.input_buscador.get()       
        self.buscar()
        self.controller.show_frame("Resultados_frame")
        self.controller.frames["Resultados_frame"].rellenar(False)
        self.controller.frames["Resultados_frame"].set_origin("Buscador_por_texto_frame")
        self.controller.frames["Resultados_frame"].set_titulo_noticia(texto_buscado)
        self.borrar_contenido()

    def borrar_contenido(self):
        self.input_buscador.delete(0,"end")

    def buscar(self):
        #TODO aqui va la funcion de buscar
        print("Buscando")