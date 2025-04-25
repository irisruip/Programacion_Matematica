
# Script principal 

from asignacion_programadores import Programador, Tarea, ProblemaAsignacion

def pedir_datos_usuario():
    N = int(input("Ingrese el número de programadores: "))
    M = int(input("Ingrese el número de tareas: "))

    print("\nIngrese la matriz de costos C[N][M]:")
    costos = []
    for i in range(N):
        fila = list(map(int, input(f"Costos para el programador {i} separados por espacio: ").split()))
        if len(fila) != M:
            raise ValueError("Cantidad incorrecta de columnas en la matriz de costos.")
        costos.append(fila)

    print("\nIngrese la capacidad (S) de cada programador:")
    capacidades = list(map(int, input("Separadas por espacio: ").split()))
    if len(capacidades) != N:
        raise ValueError("Cantidad incorrecta de capacidades.")

    print("\nIngrese la demanda (D) de cada tarea:")
    demandas = list(map(int, input("Separadas por espacio: ").split()))
    if len(demandas) != M:
        raise ValueError("Cantidad incorrecta de demandas.")

    return N, M, costos, capacidades, demandas

def main():
    try:
        # Obtener datos del usuario
        N, M, costos, capacidades, demandas = pedir_datos_usuario()

        programadores = [Programador(i, capacidades[i]) for i in range(N)]
        tareas = [Tarea(j, demandas[j]) for j in range(M)]

        problema = ProblemaAsignacion(programadores, tareas, costos)
        problema.metodo_costo_minimo()
        problema.reporte()

    except Exception as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    main()

