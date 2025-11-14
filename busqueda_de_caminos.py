import os
import time

MAZE_1 = [
    [1, 8, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 9, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

MAZE_2 = [
    [1, 8, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 9, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

MAZE_3 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 8, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 9, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]


def main(maze, method="DFS"):
    direcciones = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # --- UNIDAD 4: CONJUNTOS ---
    # 'valid_nodes': Conjunto de nodos por los que se puede caminar
    valid_nodes = set()
    start = (0, 0)
    end = (0, 0)

    # Preparación del Grafo
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell in [0, 8, 9]:  # Si es camino, inicio o fin
                valid_nodes.add((i, j))
            if cell == 8:
                start = (i, j)
            elif cell == 9:
                end = (i, j)

    # --- ESTRUCTURA DE DATOS SEGÚN MÉTODO ---
    # 'posibles_movimientos' actuará como Pila (DFS) o Cola (BFS)
    posibles_movimientos = [start]

    # --- UNIDAD 1: ÁLGEBRA DE BOOLE ---
    # 'visitados' es un conjunto para manejo booleano: ¿Ya pasé por aquí? True/False
    # Esto evita ciclos infinitos y mejora eficiencia.
    visitados = set()
    visitados.add(start)

    # Para efectos visuales (historial de lo que hemos explorado)
    historial_visual = []

    while True:
        # Limpiar consola
        os.system('cls' if os.name == 'nt' else 'clear')

        if len(posibles_movimientos) == 0:
            print("❌ No hay camino posible.")
            break

        # --- UNIDAD 6: ÁRBOLES Y RECORRIDOS ---
        if method == "DFS":
            # LIFO (Last In, First Out) -> Comportamiento de PILA
            current = posibles_movimientos.pop()
        else:  # BFS
            # FIFO (First In, First Out) -> Comportamiento de COLA
            current = posibles_movimientos.pop(0)

        historial_visual.append(current)

        # IMPRESIÓN DEL ESTADO ACTUAL
        print(f"Modo: {method} | Explorando: {current}")
        for i, row in enumerate(maze):
            for j, cell in enumerate(row):
                if (i, j) == current:
                    print("0", end=" ")  # Personaje
                elif (i, j) == end:
                    print("X", end=" ")  # Meta distinta
                elif (i, j) in historial_visual:
                    print("·", end=" ")  # Rastro
                else:
                    match cell:
                        case 1: print("█", end=" ")
                        case 0: print(" ", end=" ")
                        case 8: print("S", end=" ")
            print()

        # --- UNIDAD 3: LÓGICA ---
        if current == end:
            print("\n¡CAMINO ENCONTRADO!")
            break

        # --- UNIDAD 3 & 1: EVALUACIÓN DE VECINOS ---
        for d in direcciones:
            nuevo_movimiento = (current[0] + d[0], current[1] + d[1])

            # Proposición Lógica Compleja:
            # (Es un nodo válido del grafo) AND (NO ha sido visitado previamente)
            if nuevo_movimiento in valid_nodes and nuevo_movimiento not in visitados:

                posibles_movimientos.append(nuevo_movimiento)
                # Marcamos INMEDIATAMENTE como True
                visitados.add(nuevo_movimiento)

        time.sleep(0.1)


if __name__ == "__main__":
    print("--- TRABAJO PRÁCTICO DE MATEMÁTICA Y PROGRAMACIÓN ---")
    print("Selecciona un laberinto:")
    print("1. Laberinto Pequeño")
    print("2. Laberinto con Trampa")
    print("3. Laberinto Grande (Complejo)")

    try:
        opcion = int(input("Opción (1-3): "))
    except:
        opcion = 1

    print("\nSelecciona el algoritmo de GRAFOS (Unidad 6):")
    print("1. DFS (Busqueda en Profundidad) -> Usa PILA (.pop())")
    print("2. BFS (Busqueda en Anchura) -> Usa COLA (.pop(0))")

    try:
        metodo_opcion = int(input("Opción (1-2): "))
    except:
        metodo_opcion = 1

    metodo_seleccionado = "DFS" if metodo_opcion == 1 else "BFS"

    # Selección de mapa
    mapa_elegido = MAZE_1
    if opcion == 2:
        mapa_elegido = MAZE_2
    elif opcion == 3:
        mapa_elegido = MAZE_3

    main(mapa_elegido, method=metodo_seleccionado)
