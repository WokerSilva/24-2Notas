import random

# Esta función lee la fórmula desde un archivo.
def leer_formula_desde_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        formula = archivo.read()
    return formula

# Esta función adivina una asignación de verdad para las variables en la fórmula.
def adivinar_asignacion(formula):
    variables = set(formula.replace('-', '').replace('+', '').replace('*', '').replace('(', '').replace(')', '').split())
    asignacion = {var: random.choice([True, False]) for var in variables}
    return asignacion

# Esta función verifica si la asignación de verdad satisface la fórmula.
def verificar_asignacion(formula, asignacion):
    clausulas = formula.split('*')
    for clausula in clausulas:
        literales = clausula.replace('(', '').replace(')', '').split('+')
        if not any(asignacion[literal.strip().replace('-', '')] if '-' not in literal else not asignacion[literal.strip().replace('-', '')] for literal in literales):
            return False
    return True

# Esta es la función principal que resuelve el problema 3-SAT.
def resolver_3sat(nombre_archivo):
    # Leer la fórmula desde el archivo.
    formula = leer_formula_desde_archivo(nombre_archivo)
    print(f'Entrada:\n{formula}\n')

    # Fase de adivinanza:
    # - adivinar una asignación de verdad.
    asignacion = adivinar_asignacion(formula)
    print(f'Fase Adivinadora:\n{asignacion}\n')

    # Fase de verificación 
    # - verificar si la asignación satisface la fórmula.
    resultado = verificar_asignacion(formula, asignacion)
    print(f'Fase Verificadora:\n{"Sí encontrado" if resultado else "No encontrado"}')

# Ejecutar el algoritmo 3-SAT.
resolver_3sat('formula_3sat.txt')

