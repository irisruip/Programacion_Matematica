import numpy as np

def leer_datos():
    #Lee los datos desde la consola.
    N = int(input("Ingrese la cantidad de programadores (N): "))
    M = int(input("Ingrese la cantidad de tareas (M): "))
    print("Ingrese la matriz de costos (N filas, M columnas):")
    C = [list(map(int, input(f"Fila {i + 1}: ").split())) for i in range(N)]
    return N, M, C

def reducir_filas(matriz):
    #Reduce cada fila de la matriz restando el valor mínimo de cada fila.

    print("\nReducción de filas:")
    for i in range(len(matriz)):
        min_val = min(matriz[i])
        for j in range(len(matriz[i])):
            matriz[i][j] -= min_val
    print(np.array(matriz))

def reducir_columnas(matriz):
    #Reduce cada columna de la matriz restando el valor mínimo de cada columna.
    
    print("\nReducción de columnas:")
    for j in range(len(matriz[0])):
        min_val = min(matriz[i][j] for i in range(len(matriz)))
        for i in range(len(matriz)):
            matriz[i][j] -= min_val
    print(np.array(matriz))

def encontrar_ceros_cubiertos(matriz, filas_cubiertas, columnas_cubiertas):
    #Encuentra los ceros no cubiertos por las líneas y devuelve sus coordenadas.
    
    for i in range(len(matriz)):
        if not filas_cubiertas[i]:
            for j in range(len(matriz[i])):
                if matriz[i][j] == 0 and not columnas_cubiertas[j]:
                    return i, j
    return None

def asignar_tareas(matriz):

    #método húngaro para encontrar la asignación óptima.

    N, M = len(matriz), len(matriz[0])
    asignaciones = [-1] * M
    filas_cubiertas = [False] * N
    columnas_cubiertas = [False] * M

    while True:
        cero = encontrar_ceros_cubiertos(matriz, filas_cubiertas, columnas_cubiertas)
        if cero is None:
            break
        i, j = cero
        asignaciones[j] = i
        filas_cubiertas[i] = True
        columnas_cubiertas[j] = True

    return asignaciones

def metodo_hungaro(C):
    #método húngaro para minimizar el costo de asignación.

    matriz = np.array(C, dtype=int)
    print("\nMatriz inicial:")
    print(matriz)

    reducir_filas(matriz)
    reducir_columnas(matriz)

    while True:
        filas_cubiertas = [False] * len(matriz)
        columnas_cubiertas = [False] * len(matriz[0])
        asignaciones = asignar_tareas(matriz)

        if -1 not in asignaciones:
            break

        # Ajustar la matriz si no se puede cubrir completamente
        valores_no_cubiertos = [
            matriz[i][j]
            for i in range(len(matriz))
            for j in range(len(matriz[i]))
            if not filas_cubiertas[i] and not columnas_cubiertas[j]
        ]
        min_val = min(valores_no_cubiertos)

        print("\nAjuste de la matriz:")
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if not filas_cubiertas[i] and not columnas_cubiertas[j]:
                    matriz[i][j] -= min_val
                elif filas_cubiertas[i] and columnas_cubiertas[j]:
                    matriz[i][j] += min_val
        print(matriz)

    return asignaciones

def calcular_costo_total(C, asignaciones):
    #Calcula el costo total de la asignación.
    costo_total = 0
    for j, i in enumerate(asignaciones):
        if i != -1:
            costo_total += C[i][j]
    return costo_total

def main():
    N, M, C = leer_datos()
    if N < M:
        print("Error: El número de programadores debe ser mayor o igual al número de tareas.")
        return

    asignaciones = metodo_hungaro(C)
    costo_total = calcular_costo_total(C, asignaciones)

    print("\nAsignaciones óptimas (tarea -> programador):")
    for j, i in enumerate(asignaciones):
        print(f"Tarea {j + 1} -> Programador {i + 1}")
    print(f"\nCosto total de la asignación: {costo_total}")

if __name__ == "__main__":
    main()





