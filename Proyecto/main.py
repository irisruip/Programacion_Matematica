
# Script principal 

from asignacion_programadores import Programador, Tarea, ProblemaTransporte
from optimizacion_servidores import Servidor, Solicitud, OptimizadorHungaro
import numpy as np

# Cargar datos de ejemplo para los módulos de transporte y servidores.
def cargar_datos_transporte():
    # Datos de ejemplo para transporte
    programadores = [Programador(0, 5), Programador(1, 3)]
    tareas = [Tarea(0, 2, "Caracas"), Tarea(1, 4, "Valencia")]
    costos = np.array([[3, 8], [5, 2]])
    return programadores, tareas, costos

# Cargar datos de ejemplo para servidores.
def cargar_datos_servidores():
    # Datos de ejemplo para servidores
    servidores = [Servidor(0, 16, 32), Servidor(1, 8, 16)]
    solicitudes = [Solicitud(0, 4, 8, 1), Solicitud(1, 2, 4, 3)]
    costos = np.array([[4, 2], [3, 5]])
    return servidores, solicitudes, costos

# Cargar datos desde la consola para el módulo de transporte.
def cargar_datos_transporte_consola():
    print("\n--- Datos para Módulo de Transporte ---")
    N = int(input("Número de programadores (N): "))
    M = int(input("Número de tareas (M): "))

    # Validar N y M positivos
    if N <= 0 or M <= 0:
        raise ValueError("N y M deben ser mayores a 0.")

    # Ingresar matriz de costos
    print("\nMatriz de costos (N filas x M columnas):")
    costos = []
    for i in range(N):
        fila = list(map(int, input(f"Costos para programador {i} (separados por espacio): ").split()))
        if len(fila) != M:
            raise ValueError(f"Se esperaban {M} valores para el programador {i}.")
        costos.append(fila)

    # Capacidades de programadores
    print("\nCapacidad máxima de tareas por programador:")
    capacidades = list(map(int, input("Separadas por espacio: ").split()))
    if len(capacidades) != N:
        raise ValueError("Debe ingresar N capacidades.")
    
    # Demandas y ubicaciones de tareas
    print("\nDemanda y ubicación de cada tarea:")
    tareas = []
    for j in range(M):
        demanda = int(input(f"Demanda para tarea {j}: "))
        ubicacion = input(f"Ubicación de la tarea {j}: ")
        tareas.append(Tarea(j, demanda, ubicacion))

    # Crear objetos Programador
    programadores = [Programador(i, capacidades[i]) for i in range(N)]
    return programadores, tareas, np.array(costos)

# Cargar datos desde la consola para el módulo de servidores.
def cargar_datos_servidores_consola():
    print("\n--- Datos para Módulo de Servidores ---")
    S = int(input("Número de servidores (S): "))
    R = int(input("Número de solicitudes (R): "))

    # Recursos de servidores
    print("\nRecursos de cada servidor (CPU Memoria):")
    servidores = []
    for i in range(S):
        cpu, memoria = map(int, input(f"Servidor {i}: ").split())
        servidores.append(Servidor(i, cpu, memoria))

    # Solicitudes
    print("\nDetalles de solicitudes (CPU Memoria Prioridad):")
    solicitudes = []
    for j in range(R):
        cpu, memoria, prioridad = map(int, input(f"Solicitud {j}: ").split())
        solicitudes.append(Solicitud(j, cpu, memoria, prioridad))

    # Matriz de costos
    print("\nMatriz de costos (S filas x R columnas):")
    costos = []
    for i in range(S):
        fila = list(map(int, input(f"Costos para servidor {i}: ").split()))
        costos.append(fila)
    
    return servidores, solicitudes, np.array(costos)

# Definir el menú principal para seleccionar módulos.
def menu_modulos():
    print("\n=== Menú Principal ===")
    print("1. Módulo de Transporte (Programadores y Tareas)")
    print("2. Módulo de Servidores (Asignación de Solicitudes)")
    print("3. Ambos módulos")
    print("4. Salir")
    return int(input("Seleccione una opción: "))

# Ejecutar el módulo de transporte.
def ejecutar_modulo_transporte():
    opcion = input("¿Usar datos de prueba para transporte? (s/n): ").lower()
    if opcion == 's':
        p, t, c = cargar_datos_transporte()
    else:
        p, t, c = cargar_datos_transporte_consola()
    problema = ProblemaTransporte(p, t, c)
    problema.metodo_costo_minimo()
    problema.reporte()

# Ejecutar el módulo de servidores.
def ejecutar_modulo_servidores():
    opcion = input("¿Usar datos de prueba para servidores? (s/n): ").lower()
    if opcion == 's':
        s, r, c = cargar_datos_servidores()
    else:
        s, r, c = cargar_datos_servidores_consola()
    optimizador = OptimizadorHungaro(s, r, c)
    optimizador.resolver()
    optimizador.reporte()

# Función principal que ejecuta el programa.
def main():
    while True:
        opcion = menu_modulos()
        if opcion == 1:
            print("\n=== Ejecutando Módulo de Transporte ===")
            ejecutar_modulo_transporte()
        elif opcion == 2:
            print("\n=== Ejecutando Módulo de Servidores ===")
            ejecutar_modulo_servidores()
        elif opcion == 3:
            ejecutar_modulo_transporte()
            ejecutar_modulo_servidores()
        elif opcion == 4:
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
