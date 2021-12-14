import tkinter

#crear ventana
window=tkinter.Tk()
window.geometry("1200x800")
window.title("Recomendador")

#configurar ventana para que salga centrada respecto a la pantalla
window.update_idletasks()
width = window.winfo_width()
frm_width = window.winfo_rootx() - window.winfo_x()
win_width = width + 2 * frm_width
height = window.winfo_height()
titlebar_height = window.winfo_rooty() - window.winfo_y()
win_height = height + titlebar_height + frm_width
x = window.winfo_screenwidth() // 2 - win_width // 2
y = window.winfo_screenheight() // 2 - win_height // 2
window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
window.deiconify()

#llamada al frame de menu

#visualizar
window.mainloop()