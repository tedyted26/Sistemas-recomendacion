import numpy
import TransformTFIDF as tfidf
from vistas import recomendador

# leer matriz y convertirla a tf-idf para pasarla a los buscadores
matriz_txt = numpy.loadtxt("matriz.txt")
matriz_tfidf = tfidf.matrixToTFIDF(matriz_txt) 

