import vistas.recomendador as r
import os
from config.definitions import ROOT_DIR
import numpy
import TransformTFIDF as tf
from config.definitions import IDF_FILE_RPATH

# cambiar current directory para evitar problemas con los path de archivos
os.chdir(ROOT_DIR)

matriz_txt = numpy.loadtxt("matriz.txt")
listaIDF = tf.getIDFlistOfMatriz(matriz_txt)
numpy.savetxt(IDF_FILE_RPATH, listaIDF)


#crear la ventana del programa
app = r.Recomendador()

#visualizar
app.mainloop()

