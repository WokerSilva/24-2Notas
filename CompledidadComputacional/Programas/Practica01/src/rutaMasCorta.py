import queue
import random

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
                # Para una gráfica no dirigida, se pueden eliminar estas comprobaciones
                grafica[v1][v2] = 1
                grafica[v2][v1] = 1
    return grafica

def rutaMasCorta(grafica, inicio, final, k):
    # Paso 1: Inicialización
    distancias = inicializarDistancias(grafica, inicio)
    colaPrioridad = inicializarColaPrioridad(inicio)
    
    # Fase de no determinismo: selección aleatoria de vértices adyacentes
    while not colaPrioridad.empty():
        verticeActual = colaPrioridad.get()
        vecinos_aleatorios = list(grafica[verticeActual].keys())
        random.shuffle(vecinos_aleatorios)
        for vecino in vecinos_aleatorios:
            actualizarDistancia(distancias, verticeActual, vecino, colaPrioridad)
    
    # Paso 3: Verificación
    if distancias[final] < k:
        return "Sí, hay una ruta de peso menor que k entre inicio y final"
    else:
        return "No, no hay una ruta de peso menor que k entre inicio y final"

def inicializarDistancias(grafica, inicio):
    distancias = {}
    for vertice in grafica:
        if vertice == inicio:
            distancias[vertice] = 0
        else:
            distancias[vertice] = float('inf')
    return distancias

def inicializarColaPrioridad(inicio):
    colaPrioridad = queue.Queue()
    colaPrioridad.put(inicio)
    return colaPrioridad

def actualizarDistancia(distancias, verticeActual, vecino, colaPrioridad):
    distancia_nueva = distancias[verticeActual] + 1  # Suponemos que todas las aristas tienen peso 1
    if distancia_nueva < distancias[vecino]:
        distancias[vecino] = distancia_nueva
        colaPrioridad.put(vecino)

# Ejemplo de uso
nombre_archivo = "grafo_generado.txt"  # Nombre del archivo proporcionado por el usuario
inicio = 1
final = 7
k = 4

grafica = leer_grafica_desde_archivo(nombre_archivo)
print(rutaMasCorta(grafica, inicio, final, k))
