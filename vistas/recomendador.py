from tkinter import *
from menu import Menu_frame
from buscador_texto import Buscador_por_texto_frame
from buscador import Buscador_frame
from resultados import Resultados_frame

class Recomendador(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        #contenedor principal
        container = Frame(self)
        container.place(relx=0, rely=0, relheight=1, relwidth=1)
        self.geometry("1200x800")
        self.title("Recomendador")
        self.resizable(0,0)

        #configurar ventana para que salga centrada respecto a la pantalla
        self.update_idletasks()
        width = self.winfo_width()
        frm_width = self.winfo_rootx() - self.winfo_x()
        win_width = width + 2 * frm_width
        height = self.winfo_height()
        titlebar_height =   self.winfo_rooty() - self.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = self.winfo_screenwidth() // 2 - win_width // 2
        y = self.winfo_screenheight() // 2 - win_height // 2
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.deiconify()

        #paginas del programa
        self.frames = {}

        for F in (Menu_frame, Buscador_por_texto_frame, Buscador_frame, Resultados_frame):
            page_name = F.__name__
            frame = F(parent=container)
            self.frames[page_name] = frame
            self.frames[page_name].set_controller(controller=self)
            self.frames[page_name].create_widgets()
            #ponemos todos los frames en el mismo sitio para que se stackeen
            frame.place(relx=0, rely=0, relheight=1, relwidth=1)      

        self.show_frame("Menu_frame")

    #mostrar las paginas
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise() 

#crear la ventana
app = Recomendador()

#visualizar
app.mainloop()
