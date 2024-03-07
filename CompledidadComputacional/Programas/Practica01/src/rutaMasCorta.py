import random
import queue

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
    distancia_nueva = distancias[verticeActual] + grafica[verticeActual][vecino]
    if distancia_nueva < distancias[vecino]:
        distancias[vecino] = distancia_nueva
        colaPrioridad.put(vecino)

# Ejemplo de uso
grafica = {
    'A': {'B': 2, 'C': 5},
    'B': {'A': 2, 'C': 1},
    'C': {'A': 5, 'B': 1}
}
inicio = 'A'
final = 'C'
k = 4

print(rutaMasCorta(grafica, inicio, final, k))
