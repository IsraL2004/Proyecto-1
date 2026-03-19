import random
import math
from grafo import *

def distanciaAB(a,b): # Distancia entre 2 nodos
    return math.sqrt((a[0]-b[0] )**2 + (a[1]-b[1])**2)

def malla(m, n, dirigido):
    """
    Recibe parametros de
    n: filas
    m: columnas
    Y la direccion del grafo
    """
    grafo = Graph(dirigido)
    identificador = 0
    for i in range(m):
        for j in range(n):
            if j < n - 1:
                # Añade la arista si existe un nodo a la derecha
                grafo.addEdge("nodo_" + str(i*n + j), "nodo_" + str(i*n + j + 1), "Id" + str(identificador))
                identificador += 1
            if i < m - 1:
                # Añade la arista si existe un nodo abajo de el
                grafo.addEdge("nodo_" + str(i*n + j), "nodo_" + str(i * n + j + n), "Id" + str(identificador))
                identificador += 1
    return grafo

def grafoErdosRenyi(n, m, dirigido=False):
    grafo = Graph(dirigido)
    # Crear nodos
    for i in range(n):
        grafo.addNode("nodo_" + str(i))
    aristas = set()  # Para evitar duplicados
    while len(aristas) < m:
        u = random.randint(0, n - 1)
        v = random.randint(0, n - 1)
        if u == v:
            continue  # evitar loops
        # Normalizar si no es dirigido
        if not dirigido:
            arista = tuple(sorted((u, v)))
        else:
            arista = (u, v)
        if arista not in aristas:
            aristas.add(arista)
            grafo.addEdge(
                "nodo_" + str(arista[0]),
                "nodo_" + str(arista[1]),
                "Ident" + str(len(aristas))
            )
    return grafo


def grafoGibert(n, p, dirigido):
    """
    Recibe parametros de
    n: nodos
    p: probabilidad de conexion
    Y la direccion del grafo
    """
    grafo = Graph(dirigido)
    numeroIdent = 1
    for j in range(n): # Recorre cada elemento
        for k in range(n):  # Contra cada uno
            probabilidad = random.randint(0, 100) # probabilidad
            if probabilidad < p and j != k: # Si el nodo es distinto y la probabilidad menor crea la arista
                grafo.addEdge("nodo_" + str(j), "nodo_" + str(k), "Ident" + str(numeroIdent))
                numeroIdent += 1
    return grafo

def grafoGeografico(n, r, dirigido):
    """
    Recibe parametros de
    n: nodos
    r: distancia entre 0 y 1
    Y la direccion del grafo
    """
    grafo = Graph(dirigido)
    numeroIdent = 1
    for i in range(n):
        posicion = (random.random(), random.random())
        grafo.addNode("nodo_" + str(i), posicion) # Crea los nodos con una posicion al azar
    for j in range(n):
        for k in range(n): # Recorre todos los nodos contra todos
            a = (grafo.getNodo("nodo_" + str(j)).getDireccionX(), (grafo.getNodo("nodo_" + str(j)).getDireccionY()))
            b = (grafo.getNodo("nodo_" + str(k)).getDireccionX(), (grafo.getNodo("nodo_" + str(k)).getDireccionY()))
            distancia = distanciaAB(a,b)
            if j != k and distancia < r: # Si la distancia es menor y el nodo distinto crea la arista
                grafo.addEdge("nodo_" + str(j), "nodo_" + str(k), "Ident" + str(numeroIdent))
                numeroIdent += 1
    return grafo


def grafoBarabasiAlbert(n, d, dirigido):
    """
    Recibe parametros de
    n: nodos
    d: el maximo que cada nodo puede estar conectado
    Y la direccion del grafo
    """
    grafo = Graph(dirigido)
    identificador = 0
    for i in range(n):
        grafo.addNode("nodo_" + str(i)) # Crea el nodo
        for j in range(i):
            # La probabilidad se asigna en base al grado del nodo, si llega al maximo d tiene 0 probabilidades
            probablidad = 1 -( float(grafo.getNodo("nodo_" + str(j)).getGrado()) / d)
            acierto =random.random()
            if probablidad > acierto and float(grafo.getNodo("nodo_" + str(i)).getGrado()) < d:
                # Si la probabiliadad y el grado del nodo es menor crea la arista
                grafo.addEdge("nodo_" + str(i), "nodo_"+ str(j), str(identificador))
                identificador+= 1
    return grafo

def grafoDorogovtsevMendes(n, dirigido=False):
    """
        Recibe parametros de
        n: nodos
        Y la direccion del grafo
        """
    grafo = Graph(dirigido)
    identificador = 4
    # Al menos se crean 3 nodos
    grafo.addEdge("nodo_0", "nodo_1", "1")
    grafo.addEdge("nodo_0", "nodo_2", "2")
    grafo.addEdge("nodo_1", "nodo_2", "3")

    if n < 3:
        n = 3
    for i in range(n-3):
        arista = random.randint(1, identificador-1) # Se selecciona una arista al azar
        # Obtiene los nodos en los cuales esta implicada la arista
        n0, n1 = grafo.aristas.get(str(arista)).getNodesIm()
        # Crea las aristas entre los nodos implicados y el nodo en el cual estamos
        grafo.addEdge("nodo_" + str(i+4), str(n0), str(identificador))
        identificador += 1
        grafo.addEdge("nodo_" + str(i+4), str(n1), str(identificador))
        identificador += 1
    return grafo

