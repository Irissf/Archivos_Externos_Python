import pickle

#rb -> read binary
fichero = open("archivos/lista_nombres","rb")

#cargamos lo que tenemos dentro del archivo binario
lista = pickle.load(fichero)

print(lista)

fichero.close()