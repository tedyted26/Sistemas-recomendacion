from tkinter import *
from functools import partial
from tkinter import ttk

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

    #funcion necesaria para incluir el titulo de la noticia base seleccionada en la pantalla de busqueda en 
    #el titulo de la ventana
    def set_titulo_noticia(self, titulo):
        self.titulo_ventana.config(text="Resultados para: "+titulo)

    def create_widgets(self):
        #frame superior con título y boton de atrás
        self.frame_superior = Frame(self)
        self.frame_superior.place(relx=0, rely=0, relheight=0.05, relwidth=1)

        self.boton_volver = Button(self.frame_superior, text="Volver", command=self.volver)
        self.boton_volver.place(relx=0, rely=0, relheight=1)

        self.titulo_ventana = Label(self.frame_superior, text="Resultados")
        self.titulo_ventana.place(relx=0.05, rely=0, relheight=1)

        #resto de los componentes
        self.frame_contenido = Frame(self)
        self.frame_contenido.place(relx=0, rely= 0.05, relheight=0.95, relwidth=1)

        periodicos = ["El Mundo", "El País", "20 Minutos"]
        top = ["Top 3", "Top 5", "Top 10"]

        self.label_periodicos = Label(self.frame_contenido, text="Periódico:")
        self.label_periodicos.place(relx=0.05, rely=0.055)

        self.periodicos_combobox = ttk.Combobox(self.frame_contenido, values=periodicos, state="readonly")
        self.periodicos_combobox.current(0)
        self.periodicos_combobox.place(relx=0.12, rely= 0.055, relwidth=0.2)

        self.label_top = Label(self.frame_contenido, text="Filtrar por:")
        self.label_top.place(relx=0.35, rely=0.055)

        self.top_combobox = ttk.Combobox(self.frame_contenido, values=top, state="readonly")
        self.top_combobox.current(0)
        self.top_combobox.place(relx=0.42, rely= 0.055, relwidth=0.2)

        self.label_ranking = Label(self.frame_contenido, text="Ranking")
        self.label_ranking.place(relx=0.05, rely= 0.11)

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

        #inicializamos el panel de filtros
        self.frame_filtros = Frame(self)
        

    def volver(self):
        self.controller.show_frame(self.origin)
    
    def rellenar(self, filtros=False):
        #TODO rellenar según la busqueda
        #si viene de la página de recomendaciones debe tener los campos de filtros visibles
        if filtros:
            self.show_filtros()
        else:
            self.frame_contenido.place_configure(relheight=0.95)
            if self.frame_filtros.winfo_ismapped:
                self.frame_filtros.place_forget()
    
    def show_filtros(self):
        #TODO añadir frame con filtros y cambiar ligeramente la posicion del resto de contenidos
        self.frame_contenido.place_configure(relheight= 0.825)
        self.frame_filtros.place(relx=0, rely=0.85, relheight=0.15, relwidth=1)

        self.label_filtros_origen = Label(self.frame_filtros, text="Filtros origen")
        self.label_filtros_origen.place(relx=0.05, rely= 0)

        self.label_filtros_destino = Label(self.frame_filtros, text="Filtros destino")
        self.label_filtros_destino.place(relx=0.41, rely= 0)

        self.lista_filtros_origen = Text(self.frame_filtros, wrap='word')
        self.lista_filtros_origen.place(relx=0.05, rely= 0.2, relheight=0.5, relwidth=0.32)

        self.lista_filtros_destino = Text(self.frame_filtros, wrap='word')
        self.lista_filtros_destino.place(relx=0.41, rely= 0.2, relheight=0.5, relwidth=0.52)

