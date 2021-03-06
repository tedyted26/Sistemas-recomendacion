from tkinter import *
from tkinter import ttk
import sys
import os

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

import tratamientoDatos

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

        periodicos = ["Todos", "El Mundo", "El Pais", "20Minutos"]

        self.label_periodicos = Label(self.frame_contenido, text="Periódico:")
        self.label_periodicos.place(relx=0.05, rely=0.055)

        self.periodicos_combobox = ttk.Combobox(self.frame_contenido, values=periodicos, state="readonly")
        self.periodicos_combobox.current(0)
        self.periodicos_combobox.place(relx=0.12, rely= 0.055, relwidth=0.2)
        self.periodicos_combobox.bind("<<ComboboxSelected>>", self.cambiarPeriodico)

        self.label_ranking = Label(self.frame_contenido, text="Ranking")
        self.label_ranking.place(relx=0.05, rely= 0.11)

        self.label_error = Label(self.frame_contenido, text="", fg="red")
        self.label_error.place(relx=0.41, rely=0.055, relwidth=0.52)
        
        self.label_previsualizacion = Label(self.frame_contenido, text="Previsualización")
        self.label_previsualizacion.place(relx=0.41, rely= 0.11)

        self.lista_noticias = ttk.Treeview(self.frame_contenido, column=("pos", "tit", "por"), show='headings', height=5, selectmode=BROWSE)

        self.lista_noticias.column('#0', width=0, stretch=NO)
        self.lista_noticias.column('pos', width=1, anchor=E)
        self.lista_noticias.column('tit', width=150, anchor=W)
        self.lista_noticias.column('por', width=1, anchor=CENTER)

        self.lista_noticias.heading("pos", text="Posición", anchor=CENTER)
        self.lista_noticias.heading("tit", text="Título", anchor=W)   
        self.lista_noticias.heading("por", text="%", anchor=CENTER)

        self.lista_noticias.place(relx=0.05, rely= 0.15, relheight=0.8, relwidth=0.32)
        self.lista_noticias.bind("<<TreeviewSelect>>", self.mostrar_texto)

        sb = Scrollbar(self.frame_contenido)
        sb.place(relx=0.37, rely= 0.15, relheight=0.8, relwidth=0.02)

        self.lista_noticias.config(yscrollcommand=sb.set)
        sb.config(command=self.lista_noticias.yview)

        self.vista_noticias = Text(self.frame_contenido, wrap='word', state="disabled")
        self.vista_noticias.place(relx=0.41, rely= 0.15, relheight=0.8, relwidth=0.52)

        #inicializamos el panel de filtros
        self.frame_filtros = Frame(self)
        

    def volver(self):
        self.controller.show_frame(self.origin)
    
    def rellenar(self, noticias_similares, filtros=False, noticia_origen = None):
        self.label_error.config(text = "")

        self.noticias_similares = noticias_similares # diccionario
        self.noticia_origen = noticia_origen
        self.filtros = filtros

        self.vista_noticias['state'] = 'normal'
        self.vista_noticias.delete('1.0', "end")
        if noticia_origen is not None and len(noticia_origen.tags)==0 and self.filtros:
            self.vista_noticias.insert('1.0', "No se han podido realizar los cálculos")
        self.vista_noticias['state'] = 'disabled'

        #si viene de la página de similares debe tener los campos de filtros visibles
        if noticia_origen is not None and self.filtros:
            self.show_filtros()
            self.lista_filtros_origen['state'] = 'normal'
            self.lista_filtros_origen.delete('1.0', "end")
            if len(noticia_origen.tags)==0:
                self.lista_filtros_origen.insert('1.0', "No se ha podido cargar información sobre las etiquetas")
            self.lista_filtros_origen.insert('1.0', self.noticia_origen.getStringTags())
            self.lista_filtros_origen['state'] = 'disabled'

            self.lista_filtros_destino['state'] = 'normal'
            self.lista_filtros_destino.delete('1.0', "end")
            if len(noticia_origen.tags)==0:
                self.lista_filtros_destino.insert('1.0', "No se ha podido cargar información sobre las etiquetas")           
            self.lista_filtros_destino['state'] = 'disabled'

        else:
            self.frame_contenido.place_configure(relheight=0.95)
            if self.frame_filtros.winfo_ismapped:
                self.frame_filtros.place_forget()

        self.cambiarPeriodico()


    def mostrar_texto(self, event=None):
        
        if self.lista_noticias.focus():
            # habilitamos el campo para la edición y si tiene algo dentro se elimina
            self.vista_noticias['state'] = 'normal'
            self.vista_noticias.delete('1.0', "end")    

            # guardamos la noticia seleccionada
            if self.lista_noticias.focus()!='' and self.lista_noticias.focus()!=None:
                index_noticia = int(self.lista_noticias.focus())
                #noticia_seleccionada = self.noticias_similares[index_noticia]
                path_noticia_seleccionada = list(self.noticias_similares)[index_noticia]

                noticia_seleccionada = tratamientoDatos.leerNoticia(os.getcwd() + path_noticia_seleccionada)
                    
                # rellenamos vista
                self.vista_noticias.insert('1.0', noticia_seleccionada.titulo)
                self.vista_noticias.insert(END, "\n\n")
                self.vista_noticias.insert(END, noticia_seleccionada.subtitulo)
                self.vista_noticias.insert(END, "\n\n")
                self.vista_noticias.insert(END, noticia_seleccionada.texto)
                self.vista_noticias.insert(END, "\n\n")
                self.vista_noticias.insert(END, noticia_seleccionada.fecha)

                self.vista_noticias.tag_add("bold", "1.0", "1.0 lineend")
                self.vista_noticias.tag_config("bold", font="bold")

                if self.filtros:
                    self.lista_filtros_destino['state'] = 'normal'
                    self.lista_filtros_destino.delete('1.0', "end")
                    self.lista_filtros_destino.insert('1.0', noticia_seleccionada.getStringTags())
                    self.lista_filtros_destino['state'] = 'disabled'

            #volvemos a deshabilitar la edición
            self.vista_noticias['state'] = 'disabled'
        
    def cambiarPeriodico(self, event=None):
        self.lista_noticias.delete(*self.lista_noticias.get_children())
        self.lista_noticias.focus(None)
        
        periodico_seleccionado = self.periodicos_combobox.get()

        if self.noticias_similares is None or len(self.noticias_similares)==0:
            self.label_error.config(text = "Lo sentimos, no se han encontrado coincidencias.")
            return

        i = 0
        for key in self.noticias_similares:            
            key = key.replace("\n", "")
            noticia = tratamientoDatos.leerNoticia(os.getcwd() + key)
            ranking = self.noticias_similares[key]

            if periodico_seleccionado=="Todos":
                self.lista_noticias.insert(parent="", index="end", iid = i, text="a", values=(i+1, noticia.titulo, ranking))
                i = i+1
            elif periodico_seleccionado==noticia.periodico:
                self.lista_noticias.insert(parent="", index="end", iid = i, text="a", values=(i+1, noticia.titulo, ranking))
                i = i+1

        # seleccionar el primer elemento de la lista por defecto
        try:
            self.lista_noticias.selection_set(0)
            self.lista_noticias.focus(0)
        except:
            self.lista_noticias.selection_clear

    def show_filtros(self):
        self.frame_contenido.place_configure(relheight= 0.825)
        self.frame_filtros.place(relx=0, rely=0.85, relheight=0.15, relwidth=1)

        self.label_filtros_origen = Label(self.frame_filtros, text="Etiquetas origen")
        self.label_filtros_origen.place(relx=0.05, rely= 0)

        self.label_filtros_destino = Label(self.frame_filtros, text="Etiquetas destino")
        self.label_filtros_destino.place(relx=0.41, rely= 0)

        self.lista_filtros_origen = Text(self.frame_filtros, wrap='word', state="disabled")
        self.lista_filtros_origen.place(relx=0.05, rely= 0.2, relheight=0.5, relwidth=0.32)

        sb_3 = Scrollbar(self.frame_filtros)
        sb_3.place(relx=0.37, rely= 0.2, relheight=0.5, relwidth=0.02)

        self.lista_filtros_origen.config(yscrollcommand=sb_3.set)
        sb_3.config(command=self.lista_filtros_origen.yview)

        self.lista_filtros_destino = Text(self.frame_filtros, wrap='word', state="disabled")
        self.lista_filtros_destino.place(relx=0.41, rely= 0.2, relheight=0.5, relwidth=0.52)

        sb_4 = Scrollbar(self.frame_filtros)
        sb_4.place(relx=0.93, rely= 0.2, relheight=0.5, relwidth=0.02)

        self.lista_filtros_destino.config(yscrollcommand=sb_4.set)
        sb_4.config(command=self.lista_filtros_destino.yview)
     
            

