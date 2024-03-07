import random

def generar_grafica(nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        n = random.randint(10, 20)
        m = random.randint(2 * n + 1, 2 * n + 10)  # Garantizamos m > 2n
        vertices = list(range(1, n + 1))
        aristas = []
        for _ in range(m):
            v1 = random.choice(vertices)
            v2 = random.choice(vertices)
            while v1 == v2 or (v1, v2) in aristas or (v2, v1) in aristas:
                v1 = random.choice(vertices)
                v2 = random.choice(vertices)
            aristas.append((v1, v2))
        archivo.write(','.join(map(str, vertices)) + '\n')
        for v1, v2 in aristas:
            archivo.write(f"{v1},{v2}\n")

# Generar el archivo de texto
nombre_archivo = "grafo_generado.txt"
generar_grafica(nombre_archivo)
print(f"Se ha generado el archivo '{nombre_archivo}' satisfactoriamente.")
