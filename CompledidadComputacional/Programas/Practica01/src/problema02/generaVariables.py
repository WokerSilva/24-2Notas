import random

def generar_formula_3sat(nombre_archivo):
    # Definimos las variables y sus negaciones.
    variables = ['x', 'y', 'z']
    negaciones = ['-' + var for var in variables]

    # Generamos un número de cláusulas mayor que el doble del número de variables
    num_clausulas = random.randint(2 * len(variables) + 1, 2 * len(variables) + 10)

    # Generamos las cláusulas
    clausulas = []
    for _ in range(num_clausulas):
        # Cada cláusula tiene exactamente tres literales
        literales = random.sample(variables + negaciones, 3)
        # Al menos la mitad de las cláusulas deben contener al menos una negación
        if random.random() < 0.5:
            literales[random.randint(0, 2)] = random.choice(negaciones)
        clausula = ' + '.join(literales)
        # No puede haber dos cláusulas idénticas en la fórmula
        while clausula in clausulas:
            literales = random.sample(variables + negaciones, 3)
            if random.random() < 0.5:
                literales[random.randint(0, 2)] = random.choice(negaciones)
            clausula = ' + '.join(literales)
        clausulas.append(f'({clausula})')

    # Creamos la fórmula 3-SAT
    formula = ' * '.join(clausulas)

    # Escribimos la fórmula en el archivo
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(formula)

# Generamos la fórmula 3-SAT
generar_formula_3sat('formula_3sat.txt')