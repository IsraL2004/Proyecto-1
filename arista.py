class Arista:
    def __init__(self, nodoIni, nodoFinal, nombre):
        # Clase con 3 atributos, nodo de inicio, final y el nombre que se le da a la arista
        self.n0 = nodoIni
        self.n1 = nodoFinal
        self.nombre = nombre

    def getNombre(self): # Funcion para recuperar el nombre de la arista
        return self.nombre
    def getNodesIm(self): # Funcion para recuperar los nodos implicados en una arista
        return self.n0.nombre, self.n1.nombre

