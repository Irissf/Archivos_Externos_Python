import pickle

class Vehiculo():

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def estado(self):
        print("El coche: ",self.modelo," de la marca: ",self.marca)
#_____________________________________________________

coche1 = Vehiculo("Mazda","MX5")
coche2 = Vehiculo("Seat","Leon")
coche3 = Vehiculo("Renault","Megane")

coches = [coche1,coche2,coche3]

#=================Escritura=======================

#creamos el fichero
fichero = open("archivos/losCoches","wb")
pickle.dump(coches,fichero)

fichero.close()
del(fichero)

#=================lectura=======================

ficheroApertura = open("archivos/losCoches","rb")
misCoches = pickle.load(ficheroApertura)

ficheroApertura.close()

for c in misCoches:
    print(c.estado())