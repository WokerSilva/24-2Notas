import random

# La función recibe el nombre de archivo que contendrá la grafica para el programa
def generar_grafica(nombre_archivo):    
    with open(nombre_archivo, 'w') as archivo:
        # Genera un número aleatorio n entre 10 y 20 (|V|)
        n = random.randint(10, 20)
        # Genera un número aleatorio m entre 2*n+1 y 2*n+10 (|A|)
        m = random.randint(2 * n + 1, 2 * n + 10)  # m > 2n
        # Crea una lista de vértices que van desde 1 hasta n
        vertices = list(range(1, n + 1))        
        aristas = []
        # Itera m veces para generar las aristas
        for _ in range(m):
            # Elige aleatoriamente un vértice v1 de la lista de vértices
            v1 = random.choice(vertices)
            # Elige aleatoriamente otro vértice v2 de la lista de vértices
            v2 = random.choice(vertices)
            # Verificamos que no sean iguales y no existan aristas repetidas
            while v1 == v2 or (v1, v2) in aristas or (v2, v1) in aristas:
                v1 = random.choice(vertices)
                v2 = random.choice(vertices)

            aristas.append((v1, v2))
        # Escribe en el archivo los vértices separados por comas y agrega un salto de línea.
        archivo.write(','.join(map(str, vertices)) + '\n')        
        for v1, v2 in aristas:
            archivo.write(f"{v1},{v2}\n")

# Genera el nombre del archivo de texto.
nombre_archivo = "grafoRutaMasCorta.txt"
generar_grafica(nombre_archivo)
print(f"Se ha generado el archivo '{nombre_archivo}'")