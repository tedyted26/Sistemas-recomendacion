from tkinter import *
from functools import partial

class Buscador_por_texto_frame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.pack()

    def set_controller(self, controller):
        self.controller = controller

    def create_widgets(self):
        self.volver = Button(self, text="Volver", command=partial(self.volver, "Menu_frame"))
        self.volver.pack()
        self.bienvenido = Label(self, text="Esto es el buscador por texto")
        self.bienvenido.pack()

    def volver(self, pagina):
        self.controller.show_frame(pagina)
