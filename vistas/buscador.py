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

from Noticia import Noticia
from sorensen_dice import sorensen_dice
import tratamientoDatos
import teorema_coseno

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
            self.titulo_ventana.config(text="Recomendador por contenido (etiquetas)")          
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

        self.periodicos = ["El Mundo", "El Pais", "20Minutos"]
        self.categorias = ["Salud/Sanidad", "Tecnologia", "Ciencia"]
        self.top = [3, 5, 10]

        self.label_periodicos = Label(self.frame_contenido, text="Periódico:")
        self.label_periodicos.place(relx=0.05, rely=0.055)

        self.periodicos_combobox = ttk.Combobox(self.frame_contenido, values=self.periodicos, state="readonly")
        self.periodicos_combobox.current(0)
        self.periodicos_combobox.place(relx=0.12, rely= 0.055, relwidth=0.2)
        self.periodicos_combobox.bind("<<ComboboxSelected>>", self.rellenar)

        self.label_categorias = Label(self.frame_contenido, text="Categoría:")
        self.label_categorias.place(relx=0.35, rely=0.055)

        self.categorias_combobox = ttk.Combobox(self.frame_contenido, values=self.categorias, state="readonly")
        self.categorias_combobox.current(0)
        self.categorias_combobox.place(relx=0.42, rely= 0.055, relwidth=0.2)
        self.categorias_combobox.bind("<<ComboboxSelected>>", self.rellenar)

        self.label_top = Label(self.frame_contenido, text="Top:")
        self.label_top.place(relx=0.65, rely=0.055)

        self.top_combobox = ttk.Combobox(self.frame_contenido, values=self.top, state="readonly")
        self.top_combobox.current(0)
        self.top_combobox.place(relx=0.69, rely= 0.055, relwidth=0.05)

        self.boton_resultados = Button(self.frame_contenido, text="Buscar", command=self.boton_buscar)
        self.boton_resultados.place(relx=0.85, rely= 0.05, relwidth=0.1)

        self.label_seleccionar = Label(self.frame_contenido, text="Selecciona una noticia")
        self.label_seleccionar.place(relx=0.05, rely= 0.11)

        self.label_previsualizacion = Label(self.frame_contenido, text="Previsualización")
        self.label_previsualizacion.place(relx=0.41, rely= 0.11)

        self.lista_noticias = Listbox(self.frame_contenido, selectmode=SINGLE)
        self.lista_noticias.place(relx=0.05, rely= 0.15, relheight=0.77, relwidth=0.32)
        self.lista_noticias.bind("<<ListboxSelect>>", self.mostrar_texto)

        sb = Scrollbar(self.frame_contenido)
        sb.place(relx=0.37, rely= 0.15, relheight=0.8, relwidth=0.02)

        self.lista_noticias.config(yscrollcommand=sb.set)
        sb.config(command=self.lista_noticias.yview)

        sb_x = Scrollbar(self.frame_contenido, orient='horizontal')
        sb_x.place(relx=0.05, rely= 0.92, relheight=0.03, relwidth=0.32)

        self.lista_noticias.config(xscrollcommand=sb_x.set)
        sb_x.config(command=self.lista_noticias.xview)

        self.vista_noticias = Text(self.frame_contenido, wrap='word', state="disabled")
        self.vista_noticias.place(relx=0.41, rely= 0.15, relheight=0.8, relwidth=0.52)

        self.label_error = Label(self.frame_contenido, text="Debe seleccionar una noticia", fg="red")

        self.rellenar()

    # vuelve una pagina para atras
    def volver(self):
        self.controller.show_frame("Menu_frame")

    # rellena la lista de noticias y el texto de la noticia seleccionada
    def rellenar(self, event=None):
        # borramos el contenido que estaba antes
        self.lista_noticias.delete(0, "end")

        #recuperamos el directorio y el array de nombres de archivo
        path,files = self.encontrar_archivos()

        # inicializamos un array con self para que una vez se haya filtrado, si no se cambia la selección no volver a hacer cálculos
        self.files_noticias = []

        # por cada archivo en la carpeta creamos una Noticia, la metemos en el array de noticias file_noticias, y la añadimos a la vista
        i=0
        for file in files:
            rutaFichero = os.path.join(path, file)
            if os.path.isfile(rutaFichero):
                    noticia = tratamientoDatos.leerNoticia(rutaFichero)
                    noticia.path = rutaFichero
                    self.files_noticias.append(noticia)
                    self.lista_noticias.insert(i, str(i+1) + ". " + noticia.titulo)
                    i = i+1   
   
        # esto deja seleccionado un archivo de base y muestra su contenido
        self.lista_noticias.selection_set(0,0)
        self.mostrar_texto()
    
    # muestra el texto en la vista de noticias
    def mostrar_texto(self, event=None):
        # habilitamos el campo para la edición y si tiene algo dentro se elimina
        if self.lista_noticias.curselection():

            self.vista_noticias['state'] = 'normal'
            self.vista_noticias.delete('1.0', "end")

            # guardamos el indice de la noticia seleccionada
            if self.lista_noticias.curselection():
                index_noticia = self.lista_noticias.curselection()[0]

                #comprobamos por cada noticia en nuestra lista de noticias cual coincide con el indice, si coincide rompemos el bucle
                noticia = self.files_noticias[index_noticia]

                # el titulo se guarda con self para utilizarlo mas tarde
                self.titulo_noticia = noticia.titulo
                self.vista_noticias.insert('1.0', self.titulo_noticia)
                self.vista_noticias.insert(END, "\n")
                self.vista_noticias.insert(END, noticia.subtitulo)
                self.vista_noticias.insert(END, "\n")
                self.vista_noticias.insert(END, noticia.texto)
                self.vista_noticias.insert(END, "\n")
                self.vista_noticias.insert(END, noticia.fecha)

                self.vista_noticias.tag_add("bold", "1.0", "1.0 lineend")
                self.vista_noticias.tag_config("bold", font="bold")            

            #volvemos a deshabilitar la edición
            self.vista_noticias['state'] = 'disabled'

    #funcion para encontrar archivos dependiendo de los filtros seleccionados, devuelve la ruta y la lista de nombres de archivo
    def encontrar_archivos(self):
        path = self.periodicos_combobox.get()
        if self.categorias_combobox.get()=="Salud/Sanidad":
            if self.periodicos_combobox.get()=="El Pais":
                path+= "/Sanidad/"
            else:
                path+= "/Salud/"
        else:
            path+= "/"+ self.categorias_combobox.get() + "/"



        files = os.listdir(path)
        return path, files

    def boton_buscar(self):

        if self.lista_noticias.curselection():
            self.label_error.forget()

            indice = self.lista_noticias.curselection()[0] #esto devuelve el índice del archivo
            noticia = self.files_noticias[indice]

            top = self.top_combobox.get()

            noticias_similares = self.buscar(noticia, int(top))

            #configuración del frame de resultados
            self.controller.show_frame("Resultados_frame")
            self.controller.frames["Resultados_frame"].rellenar(noticias_similares, self.filtros, noticia)
            self.controller.frames["Resultados_frame"].set_origin("Buscador_frame")
            self.controller.frames["Resultados_frame"].set_titulo_noticia(self.titulo_noticia)
        else:
            self.label_error.place(relx=0.79, rely=0.005)
    
    def buscar(self, noticia, top):
        #TODO funcion de buscar (calculos y mierdas)
        noticias_similares = {}
        if self.filtros:
            noticias_similares = sorensen_dice(noticia, top)
        else: 
            noticias_similares = teorema_coseno.noticias_coseno(noticia, top)
        return noticias_similares