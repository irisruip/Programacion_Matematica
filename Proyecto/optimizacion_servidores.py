from typing import List  # <-- Añadir esta línea
import numpy as np
from scipy.optimize import linear_sum_assignment

class Servidor:
    def __init__(self, id: int, cpu: int, memoria: int):
        self.id = id
        self.cpu_disponible = cpu
        self.memoria_disponible = memoria
        self.solicitudes = []

class Solicitud:
    def __init__(self, id: int, cpu: int, memoria: int, prioridad: int):
        self.id = id
        self.cpu = cpu
        self.memoria = memoria
        self.prioridad = prioridad

class OptimizadorHungaro:
    def __init__(self, servidores: List[Servidor], solicitudes: List[Solicitud], costos: np.ndarray):
        self.servidores = servidores
        self.solicitudes = sorted(solicitudes, key=lambda x: x.prioridad, reverse=True)
        self.costos = costos
        self.asignaciones = []

    def resolver(self):
        row_idx, col_idx = linear_sum_assignment(self.costos)
        self.row_idx = row_idx  # <-- Guardar como atributo
        self.col_idx = col_idx  # <-- Guardar como atributo
        for srv_idx, sol_idx in zip(row_idx, col_idx):
            srv = self.servidores[srv_idx]
            sol = self.solicitudes[sol_idx]
            if srv.cpu_disponible >= sol.cpu and srv.memoria_disponible >= sol.memoria:
                self.asignaciones.append((srv.id, sol.id))
                srv.cpu_disponible -= sol.cpu
                srv.memoria_disponible -= sol.memoria

    def reporte(self):
        print("\n--- Reporte de Asignación de Servidores ---")
        for srv_id, sol_id in self.asignaciones:
            print(f"Servidor {srv_id} → Solicitud {sol_id}")
        # Usar los índices guardados
        print(f"\nTiempo total estimado: {self.costos[self.row_idx, self.col_idx].sum()}") 