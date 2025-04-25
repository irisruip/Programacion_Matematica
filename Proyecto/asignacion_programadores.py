# Usando el Método del Costo Mínimo para asignar programadores a tareas

from typing import List, Dict
import numpy as np

class Programador:
    def __init__(self, id: int, capacidad_max: int):
        self.id = id
        self.capacidad_max = capacidad_max  # Máximo de tareas que puede asumir
        self.tareas_asignadas = []

class Tarea:
    def __init__(self, id: int, demanda: int, ubicacion: str):
        self.id = id
        self.demanda = demanda  # Número de programadores requeridos
        self.ubicacion = ubicacion

class ProblemaTransporte:
    def __init__(self, programadores: List[Programador], tareas: List[Tarea], costos: np.ndarray):
        self.programadores = programadores
        self.tareas = tareas
        self.costos = costos
        self.asignaciones = []
        self.costo_total = 0

    def metodo_costo_minimo(self):
        suministro = [p.capacidad_max for p in self.programadores]
        demanda = [t.demanda for t in self.tareas]
        costos = self.costos.copy()
        
        while sum(suministro) > 0 and sum(demanda) > 0:
            # Encontrar el mínimo costo
            min_val = np.inf
            min_idx = (-1, -1)
            for i in range(len(suministro)):
                for j in range(len(demanda)):
                    if suministro[i] > 0 and demanda[j] > 0 and costos[i][j] < min_val:
                        min_val = costos[i][j]
                        min_idx = (i, j)
            
            i, j = min_idx
            if i == -1:
                break
            
            cantidad = min(suministro[i], demanda[j])
            self.asignaciones.append((i, j, cantidad))
            self.costo_total += cantidad * costos[i][j]
            suministro[i] -= cantidad
            demanda[j] -= cantidad

    def reporte(self):
        print("\n--- Reporte de Asignación con Transporte ---")
        for i, j, cantidad in self.asignaciones:
            print(
                f"Programador {self.programadores[i].id} → Tarea {self.tareas[j].id} "
                f"(Ubicación: {self.tareas[j].ubicacion}), "
                f"Asignaciones: {cantidad}, Costo unitario: {self.costos[i][j]}"
            )
        print(f"\nCosto total mínimo: {self.costo_total}")