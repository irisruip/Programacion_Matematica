# Usando el Método del Costo Mínimo para asignar programadores a tareas

from typing import List, Tuple
import copy

class Programador:
    def __init__(self, id: int, capacidad: int):
        self.id = id
        self.capacidad = capacidad

class Tarea:
    def __init__(self, id: int, demanda: int):
        self.id = id
        self.demanda = demanda

class ProblemaAsignacion:
    def __init__(self, programadores: List[Programador], tareas: List[Tarea], costos: List[List[int]]):
        self.programadores = programadores
        self.tareas = tareas
        self.costos = costos
        self.asignaciones = []
        self.costo_total = 0

    def metodo_costo_minimo(self):
        suministro = [p.capacidad for p in self.programadores]
        demanda = [t.demanda for t in self.tareas]
        costos = copy.deepcopy(self.costos)
        asignaciones = []
        
        while any(suministro) and any(demanda):
            # Buscar el menor costo
            minimo = float('inf')
            pos = (-1, -1)
            for i in range(len(suministro)):
                if suministro[i] == 0:
                    continue
                for j in range(len(demanda)):
                    if demanda[j] == 0:
                        continue
                    if costos[i][j] < minimo:
                        minimo = costos[i][j]
                        pos = (i, j)

            i, j = pos
            cantidad = min(suministro[i], demanda[j])
            asignaciones.append((i, j, cantidad))
            self.costo_total += cantidad * costos[i][j]
            suministro[i] -= cantidad
            demanda[j] -= cantidad

        self.asignaciones = asignaciones

    def reporte(self):
        print("\nReporte de Asignaciones:")
        for i, j, cantidad in self.asignaciones:
            print(f"Programador {i} asignado a Tarea {j} con {cantidad} asignaciones. Costo: {self.costos[i][j]} por asignación")
        print(f"\nCosto total mínimo de asignación y transporte: {self.costo_total}")


