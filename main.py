import vistas.recomendador as r
import os
from config.definitions import ROOT_DIR

# cambiar current directory para evitar problemas con los path de archivos
os.chdir(ROOT_DIR)

#crear la ventana del programa
app = r.Recomendador()

#visualizar
app.mainloop()

