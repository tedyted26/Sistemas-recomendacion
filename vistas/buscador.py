from tkinter import *
from functools import partial
from tkinter import ttk

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

        periodicos = ["El Mundo", "El País", "20 Minutos"]
        categorias = ["Salud/Sanidad", "Tecnología", "Ciencia"]

        self.label_periodicos = Label(self.frame_contenido, text="Periódico:")
        self.label_periodicos.place(relx=0.05, rely=0.055)

        self.periodicos_combobox = ttk.Combobox(self.frame_contenido, values=periodicos, state="readonly")
        self.periodicos_combobox.current(0)
        self.periodicos_combobox.place(relx=0.12, rely= 0.055, relwidth=0.2)

        self.label_categorias = Label(self.frame_contenido, text="Categoría:")
        self.label_categorias.place(relx=0.35, rely=0.055)

        self.categorias_combobox = ttk.Combobox(self.frame_contenido, values=categorias, state="readonly")
        self.categorias_combobox.current(0)
        self.categorias_combobox.place(relx=0.42, rely= 0.055, relwidth=0.2)

        self.boton_resultados = Button(self.frame_contenido, text="Buscar", command=self.boton_buscar)
        self.boton_resultados.place(relx=0.85, rely= 0.05, relwidth=0.1)

        self.label_seleccionar = Label(self.frame_contenido, text="Seleccionar noticia")
        self.label_seleccionar.place(relx=0.05, rely= 0.11)

        self.label_previsualizacion = Label(self.frame_contenido, text="Previsualización")
        self.label_previsualizacion.place(relx=0.41, rely= 0.11)

        self.lista_noticias = Text(self.frame_contenido)
        self.lista_noticias.place(relx=0.05, rely= 0.15, relheight=0.8, relwidth=0.32)

        sb = Scrollbar(self.frame_contenido)
        sb.place(relx=0.37, rely= 0.15, relheight=0.8, relwidth=0.02)

        self.lista_noticias.config(yscrollcommand=sb.set)
        sb.config(command=self.lista_noticias.yview)

        self.vista_noticias = Text(self.frame_contenido, wrap='word')
        self.vista_noticias.place(relx=0.41, rely= 0.15, relheight=0.8, relwidth=0.52)

        sb_2 = Scrollbar(self.frame_contenido)
        sb_2.place(relx=0.93, rely= 0.15, relheight=0.8, relwidth=0.02)

        self.vista_noticias.config(yscrollcommand=sb_2.set)
        sb_2.config(command=self.vista_noticias.yview)


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
        #hay que recoger antes la noticia seleccionada de los widgets
        titulo_noticia = "Titulo Noticia"
        self.buscar()
        #configuración del frame de resultados
        self.controller.show_frame("Resultados_frame")
        self.controller.frames["Resultados_frame"].rellenar(self.filtros)
        self.controller.frames["Resultados_frame"].set_origin("Buscador_frame")
        self.controller.frames["Resultados_frame"].set_titulo_noticia(titulo_noticia)
        self.borrar_contenido()
    
    def buscar(self):
        #TODO funcion de buscar (calculos y mierdas)
        print("Buscando")