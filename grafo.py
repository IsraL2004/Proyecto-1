from nodo import *
from arista import *
# Clase Grafo con la cual se construyen los grafos
class Graph():
    def __init__(self, direcciones): # El unico parametro de entrada es para saber si posee direccion
        self.nodos = {}
        self.aristas = {}
        if direcciones is True: # Sí está direccionado
            self.identificador = "Digraph"
            self.direcciones = " -> "
        else:
            self.identificador = "Graph"
            self.direcciones = " -- "
        self.dot = "" # Atributo en el cual se va a exportar el grafo

    def addNode(self, nombre, posicion = None): # Funcion para crear un nodo
        identificador = self.nodos.get(nombre)
        if identificador is None: # Si existe identificador el nodo ya fue creado
            if posicion is None:
                identificador = Nodo(nombre) # Se construye el nodo con el nombre
            else:
                identificador = Nodo(nombre, posicion) # Si hay posicion se construye nodo con posicion
            self.nodos[nombre] = identificador # Se añade el nodo
        return identificador

    def addEdge(self, nombreNodoIni, nombreNodoFin, nombreArista):

        identificador = self.aristas.get(nombreArista)
        if identificador is None: # Si existe el identificador la arista ya habia sido creada
            if self.nodos.get(nombreNodoIni) is None: # Si el nodo inicial no existe se crea
                self.addNode(nombreNodoIni)
                self.getNodo(nombreNodoIni).grado += 1 # Y al nodo se le suma un grado
            else:
                self.getNodo(nombreNodoIni).grado += 1 # Si existia solo se le suma un grado

            if self.nodos.get(nombreNodoFin) is None: # Se replica el comportamiento para el nodo final
                self.addNode(nombreNodoFin)
                self.getNodo(nombreNodoFin).grado += 1
            else:
                self.getNodo(nombreNodoFin).grado += 1

            # Se crea la arista con los parametros
            identificador = Arista(self.getNodo(nombreNodoIni), self.getNodo(nombreNodoFin), nombreArista)
            self.aristas[nombreArista] = identificador # Se añade la arista
        return identificador

    def generar_Grafo(self): # Se crea el texto para exportar el grafo
        self.dot = self.identificador # Depende si esta dirigido o no
        self.dot += " X {\n"

        # Agregar todos los nodos (incluso aislados)
        for nombre_nodo in self.nodos.keys():
            self.dot += f'    {nombre_nodo};\n'

        # Agregar todas las aristas
        for arista in self.aristas.values():
            self.dot += "\t" + str(arista.n0.nombre)
            self.dot += str(self.direcciones)
            self.dot += str(arista.n1.nombre)
            self.dot += ';\n'
        self.dot += "}"
        return self.dot # Regresa la cadena del grafo

    def exportar_dot(self, nombre_archivo): # Con un nombre se exporta el archivo a un .gb
        self.dot = self.generar_Grafo()
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write(self.dot)
        print(f"Archivo {nombre_archivo} guardado exitosamente")

    def getNodo(self, nombre): # Funcion para obtener un nodo
        return self.nodos.get(nombre)
    def getEdge(self, nombre):# Funcion para obtener una arista
        return self.aristas.get(nombre)

