from munkres import Munkres
import copy

def reducir_filas(matriz):
    reducida = []
    print("\n--- Reducción por filas ---")
    for i, fila in enumerate(matriz):
        minimo = min(fila)
        reducida_fila = [x - minimo for x in fila]
        print(f"Fila {i}: mínimo = {minimo}, reducida = {reducida_fila}")
        reducida.append(reducida_fila)
    return reducida

def reducir_columnas(matriz):
    matriz_transpuesta = list(zip(*matriz))
    reducida_transpuesta = []
    print("\n--- Reducción por columnas ---")
    for j, col in enumerate(matriz_transpuesta):
        minimo = min(col)
        reducida_col = [x - minimo for x in col]
        print(f"Columna {j}: mínimo = {minimo}, reducida = {reducida_col}")
        reducida_transpuesta.append(reducida_col)
    return [list(fila) for fila in zip(*reducida_transpuesta)]

def aplicar_metodo_hungaro_con_matrices(cost_matrix, N, M):
    matriz_original = copy.deepcopy(cost_matrix)

    # Hacer cuadrada para el algoritmo
    if N < M:
        for _ in range(M - N):
            cost_matrix.append([0] * M)
    elif N > M:
        for i in range(N):
            cost_matrix[i] += [0] * (N - M)

    print("\n--- Matriz original ---")
    for fila in matriz_original:
        print(fila)

    # Reducción
    matriz_reducida = reducir_filas(cost_matrix)
    matriz_reducida = reducir_columnas(matriz_reducida)

    print("\n--- Matriz después de reducción ---")
    for fila in matriz_reducida:
        print(fila)

    m = Munkres()
    asignacion = m.compute(matriz_reducida)

    asignacion_optima = []
    costo_total = 0

    for row, col in asignacion:
        if row < N and col < M:
            asignacion_optima.append((row, col))
            costo_total += matriz_original[row][col]

    return asignacion_optima, costo_total


# Entrada por archivo
def leer_datos_desde_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as file:
        lineas = file.readlines()
    N, M = map(int, lineas[0].strip().split())
    matriz_costos = [list(map(int, linea.strip().split())) for linea in lineas[1:N+1]]
    return matriz_costos, N, M

# Entrada por consola
def leer_datos_desde_consola():
    N = int(input("Ingrese el número de programadores (N): "))
    M = int(input("Ingrese el número de tareas (M): "))
    matriz_costos = []
    print("Ingrese la matriz de costos fila por fila (valores separados por espacio):")
    for i in range(N):
        fila = list(map(int, input(f"Costos del programador {i}: ").split()))
        matriz_costos.append(fila)
    return matriz_costos, N, M

def main():
    print("1. Desde archivo")
    print("2. Desde consola")
    opcion = input("Opción (1/2): ").strip()

    if opcion == '1':
        archivo = input("Nombre del archivo (ruta completa): ").strip()
        matriz_costos, N, M = leer_datos_desde_archivo(archivo)
    elif opcion == '2':
        matriz_costos, N, M = leer_datos_desde_consola()
    else:
        print("Opción inválida.")
        return

    asignacion_optima, costo_total = aplicar_metodo_hungaro_con_matrices(matriz_costos, N, M)

    print("\nAsignación óptima (programador → tarea):")
    for programador, tarea in asignacion_optima:
        costo = matriz_costos[programador][tarea]
        print(f"Programador {programador} → Tarea {tarea}  (costo = {costo})")
    print(f"\nCosto total: {costo_total}")

if __name__ == "__main__":
    main()






