import tkinter
# con la extension de archivo .pyw el archivo se ejecuta haciendo doble click
def mensaje():
    print("Mensaje del boton")

ventana = tkinter.Tk()
ventana.geometry("400x280")
ventana.title("Recomendador")

lbl = tkinter.Label(ventana, text="Hola")
lbl.place(x=60, y=40, width=100, height=30) #valores absolutos
#valores relativos al padre, valores entre 0 y 1, proporción respecto al padre
#0.1 = 10% del padre
#lbl.place(relx=0.1, rely=0.1, relwidth=0.5, relheight=0.5)

btn = tkinter.Button(ventana, text = "Boton", command=mensaje)
btn.pack() #posicionamiento relativo
#en vez de especificar las coordenadas, se especifica si el elemento va
#arriba abajo a la izquierda o a la derecha con respecto al contenedor
#si no se indica ningun argumento, pack los posiciona uno encima del otro
#la propiedad side controla la posicion
#side.TOP side.BOTTOM side.LEFT, side.RIGHT
#admite after y before: .pack(before=otroelemento)
#admite padx (margen x), pady (margen y), ipadx (padding x), ipady (padding y) en valores absolutos
#admite expand=True/False para especificar si cambia el tamaño con la ventana
#admite fill=tk.BOTH/tk.X/tk.Y hacia que lado debe expandirse


ventana.mainloop()

#GRID
#componente.grid(row= , column= , rowspan= , columnspan= , sticky= ) ----- sticky puede ser n s w e para indicar la posicion que va a tomar
#los paddings y margenes funcionan igual
#componente.columnconfigure(0, weight=1) ---- 0 es el numero de la columna, weight el peso de la columna en todo el conjunto
#componente.rowconfigure()
