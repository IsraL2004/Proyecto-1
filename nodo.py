# Clase nodo
class Nodo():
    def __init__(self, nombre, direccion=None):
        self.nombre = nombre # Nombre o identificador que tendra el nodo

        if direccion is not None: # Si hay una direccion se asigna a los atributos
            self.direccionX = direccion[0]
            self.direccionY = direccion[1]
        else:
            self.direccionX = None
            self.direccionY = None
        self.grado = 0 # El grado del nodo se inicializa en 0
    def getName(self): # Funcion para recuperar el nombre del nodo
        return self.nombre

    def getDireccionX(self): # Funcion para recuperar la posicion en X
        return self.direccionX

    def getDireccionY(self): # Funcion para recuperar la posicion en Y
        return self.direccionY

    def getGrado(self): # Funcion para obtener el grado de un nodo
        return self.grado