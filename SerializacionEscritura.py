import pickle

listaNombres = ["Iris", "María", "Ici", "Ka"]

#wb -> writte binary
ficheroBinario = open("archivos/lista_nombres","wb")

#volcamos la lista al archivo
pickle.dump(listaNombres,ficheroBinario)

ficheroBinario.close()

#lo borramos de la memoria si queremos
del(ficheroBinario)

