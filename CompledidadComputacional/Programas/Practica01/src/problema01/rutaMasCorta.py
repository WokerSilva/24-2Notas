import queue
import random

# leemos el archivo
def leer_grafica_desde_archivo(nombre_archivo):
    grafica = {}
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()
        vertices = lineas[0].strip().split(',')
        for vertice in vertices:
            grafica[int(vertice)] = {}
        for linea in lineas[1:]:
            v1, v2 = map(int, linea.strip().split(','))
            if v1 in grafica and v2 in grafica:                
                grafica[v1][v2] = 1
                grafica[v2][v1] = 1
    return grafica

# Esta función encuentra la ruta más corta en un grafo entre dos vertices
def rutaMasCorta(grafica, inicio, final, k):
    # Paso 1: Inicialización
    distancias = inicializarDistancias(grafica, inicio)
    colaPrioridad = inicializarColaPrioridad(inicio)
    
    print("Fase Adivinadora:")
    # Fase de no determinismo: selección aleatoria de vértices adyacentes
    while not colaPrioridad.empty():
        verticeActual = colaPrioridad.get()
        vecinos_aleatorios = list(grafica[verticeActual].keys())
        random.shuffle(vecinos_aleatorios)
        for vecino in vecinos_aleatorios:
            actualizarDistancia(distancias, verticeActual, vecino, colaPrioridad)
            print("Explorando vértice:", vecino)
    
    # Paso 3: Verificación
    print("\nFase Verificadora:")
    if distancias[final] < k:
        print("Sí, hay una ruta de peso menor que k entre inicio y final")
    else:
        print("No, no hay una ruta de peso menor que k entre inicio y final")

# Inicializamos lass distancias para todos los vertices en el grafo
def inicializarDistancias(grafica, inicio):
    distancias = {}
    for vertice in grafica:
        if vertice == inicio:
            distancias[vertice] = 0
        else:
            distancias[vertice] = float('inf')
    return distancias

# Cramos la cola de priodirdad añadiendo el vertice
def inicializarColaPrioridad(inicio):
    colaPrioridad = queue.Queue()
    colaPrioridad.put(inicio)
    return colaPrioridad

# Esta función actualiza la distancia entre dos vertices si se encuentra una ruta más corta.
def actualizarDistancia(distancias, verticeActual, vecino, colaPrioridad):
    distancia_nueva = distancias[verticeActual] + 1  # Suponemos que todas las aristas tienen peso 1
    if distancia_nueva < distancias[vecino]:
        distancias[vecino] = distancia_nueva
        colaPrioridad.put(vecino)

nombre_archivo = "grafoRutaMasCorta.txt"  # Nombre del archivo que esta dentro de la carpeta
inicio = 1
final = 7
k = 4

grafica = leer_grafica_desde_archivo(nombre_archivo)
rutaMasCorta(grafica, inicio, final, k)