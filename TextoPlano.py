#Fases necesarias para guardar información en archivos externos
#creación, apertura, manipulación, cierre

#=================== escritura ===========================
 
#Accedemos a la libreria IO
from io import open

#dos parámetros, la ruta y que queremos hacer, lectura, escritura append
#CREACIÓN-APERTURA
archivoTexto = open("archivos/archivo.txt","w")

#MANIPULACIÓN
frase = "un día bonito de verano con poco calor \nJueves"
archivoTexto.write(frase)

#CIERRE
archivoTexto.close()

#=================== lectura ===========================

archivoLectura = open("archivos/archivoLectura.txt","r")
#se puede mover la posicion del cursor para leer hasta cierto punto o desde
#con archivoLectura.seek(10)->el num es la posición

texto = archivoLectura.read()
#podemos usar readline, que leer linea por linea y guardarlo en una lista
archivoLectura.close()

print(texto)
#si queremos lectura y escritura a la vez. ponermos "r+"

#=================== append para agregar texto ===========================
archivoTexto = open("archivos/archivo.txt","a")

archivoTexto.write("\n Añadiendo una línea")

#podemos desplazar la posición del puntero para escribir en otra zona

archivoTexto.close

