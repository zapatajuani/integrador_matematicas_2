# Proyecto Final: Matemática y Programación - Resolución de Laberintos

Este proyecto es la entrega final para la asignatura [NOMBRE DE LA ASIGNATURA]. El objetivo es demostrar la aplicación práctica de conceptos matemáticos fundamentales en el desarrollo de software.

## Información del Alumno
* **Nombre:** `[TU NOMBRE COMPLETO]`
* **DNI:** `[TU DNI]`
* **Profesor:** `[NOMBRE DEL PROFESOR/A]`
* **Fecha:** 13 de Noviembre de 2025

---

## 🎥 Video de la Presentación

Aquí puede encontrar el video explicativo donde se desarrolla la consigna, se explica la teoría y se demuestra el proyecto en vivo.

**[LINK A TU VIDEO EN YOUTUBE, GOOGLE DRIVE, ETC.]**

---

## 🧠 Demostración de las Unidades (Consigna)

Este script resuelve laberintos utilizando algoritmos de búsqueda. Fue elegido porque **aúna en un solo problema** las 3 unidades matemáticas asignadas por mi DNI:

### 1. Unidad 6: Grafos y Árboles
El laberinto se modela como un **Grafo**. Cada celda de camino (`0`) es un **nodo**, y las conexiones adyacentes (arriba, abajo, izquierda, derecha) son las **aristas**.

El script implementa dos métodos de recorrido de grafos:
* **DFS (Depth-First Search):** Utiliza una **Pila (Stack)**, explorando una rama hasta el final antes de hacer **Backtracking** (retroceder al nodo padre).
* **BFS (Breadth-First Search):** Utiliza una **Cola (Queue)**, explorando por niveles para garantizar la ruta más corta.

### 2. Unidad 3: Lógica Proposicional
La toma de decisiones del algoritmo se basa en la evaluación de proposiciones lógicas compuestas. En cada paso, el script evalúa con un operador **AND** si un movimiento es válido:

```python
# Un movimiento es válido SI:
# (Es un nodo transitable) Y (NO ha sido visitado)
if (nuevo_movimiento in valid_nodes) and (nuevo_movimiento not in visitados):
    # ... agregar a la lista
