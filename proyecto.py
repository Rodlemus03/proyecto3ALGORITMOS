
from typing import List, Tuple

# Función para aplicar Move-To-Front (MTF)
def move_to_front(config: List[int], sequence: List[int]) -> Tuple[List[Tuple[int, List[int], int]], int]:
    history = []
    total_cost = 0
    for request in sequence:
        cost = config.index(request) + 1
        total_cost += cost
        config.remove(request)
        config.insert(0, request)
        history.append((request, config.copy(), cost))
    return history, total_cost

# Función para aplicar Improved Move-To-Front (IMTF)
def improved_mtf(config: List[int], sequence: List[int]) -> Tuple[List[Tuple[int, List[int], int]], int]:
    history = []
    total_cost = 0
    for i, request in enumerate(sequence):
        cost = config.index(request) + 1
        total_cost += cost
        look_ahead_range = sequence[i+1:i + cost]
        if request in look_ahead_range:
            config.remove(request)
            config.insert(0, request)
        history.append((request, config.copy(), cost))
    return history, total_cost

# Función para imprimir resultados
def imprimir_resultados(historial, total):
    for req, conf, c in historial:
        print(f"Solicitud: {req}, Costo: {c}, Configuración: {conf}")
    print(f"Costo total: {total}\n")

# Preguntas 1 y 2
secuencia_1 = [0, 1, 2, 3, 4] * 4
secuencia_2 = [4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4]

print("Ejercicio 1 - MTF")
hist, total = move_to_front([0, 1, 2, 3, 4], secuencia_1)
imprimir_resultados(hist, total)

print("Ejercicio 2 - MTF")
hist, total = move_to_front([0, 1, 2, 3, 4], secuencia_2)
imprimir_resultados(hist, total)

# Pregunta 3: Mejor caso (repetir el primer elemento)
mejor_caso = [0] * 20
hist, total = move_to_front([0, 1, 2, 3, 4], mejor_caso)
print("Ejercicio 3 - Mejor caso MTF")
imprimir_resultados(hist, total)

# Pregunta 4: Peor caso (ciclo completo sin repetidos)
peor_caso = [0, 1, 2, 3, 4] * 4
hist, total = move_to_front([0, 1, 2, 3, 4], peor_caso)
print("Ejercicio 4 - Peor caso MTF")
imprimir_resultados(hist, total)

# Pregunta 5: Repetición del mismo elemento
repetido = [2] * 20
hist, total = move_to_front([0, 1, 2, 3, 4], repetido)
print("Ejercicio 5 - MTF con 20 veces el número 2")
imprimir_resultados(hist, total)

repetido3 = [3] * 20
hist, total = move_to_front([0, 1, 2, 3, 4], repetido3)
print("Ejercicio 5 - MTF con 20 veces el número 3")
imprimir_resultados(hist, total)

# Pregunta 6: IMTF sobre mejor y peor caso
hist, total = improved_mtf([0, 1, 2, 3, 4], mejor_caso)
print("Ejercicio 6 - IMTF con mejor caso")
imprimir_resultados(hist, total)

hist, total = improved_mtf([0, 1, 2, 3, 4], peor_caso)
print("Ejercicio 6 - IMTF con peor caso")
imprimir_resultados(hist, total)
