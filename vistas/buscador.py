from tkinter import *
from functools import partial

class Buscador_frame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.pack()
        self.is_similar()

    def set_controller(self, controller):
        self.controller = controller

    def is_similar(self, isSimilar = True):
        self.isSimilar = isSimilar

    def create_widgets(self):
        self.frame_superior = Frame(self.master)
        self.frame_superior.place(relx=0, rely=0, relheight=0.05, relwidth=1)

        boton_volver = Button(self.frame_superior, text="Volver", command=partial(self.volver, "Menu_frame"))
        boton_volver.place(relx=0, rely=0, relheight=1)

        if self.isSimilar:
            titulo_ventana = Label(self.frame_superior, text="Similares")
            
        else:
            titulo_ventana = Label(self.frame_superior, text="Recomendados")

        titulo_ventana.place(relx=0.05, rely=0, relheight=1)

    def volver(self, pagina):
        self.controller.show_frame(pagina)