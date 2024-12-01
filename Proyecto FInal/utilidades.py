# utilidades.py

import json

def cargar_datos(archivo):
    """
    Carga las tareas desde un archivo JSON.
    Si el archivo no existe o está corrupto, devuelve una lista vacía.
    """
    try:
        with open(archivo, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []  # Si no existe el archivo, iniciar con lista vacía
    except json.JSONDecodeError:
        print("Error al cargar los datos. Archivo corrupto.")
        return []

def guardar_datos(tareas, archivo):
    """
    Guarda las tareas en un archivo JSON.
    """
    try:
        with open(archivo, "w") as f:
            json.dump(tareas, f, indent=4)
        print("✔ Datos guardados con éxito.")
    except Exception as e:
        print(f"Error al guardar los datos: {e}")

def filtrar_por_estado(tareas, estado):
    """
    Filtra las tareas por su estado (pendiente, en progreso, completada).
    """
    return [tarea for tarea in tareas if tarea["estado"] == estado.lower()]

def ordenar_por_prioridad(tareas):
    """
    Ordena las tareas por prioridad: alta > media > baja.
    """
    prioridad_orden = {"alta": 1, "media": 2, "baja": 3}
    return sorted(tareas, key=lambda tarea: prioridad_orden.get(tarea["prioridad"], 4))

def filtrar_por_categoria(tareas, categoria):
    """
    Filtra las tareas por una categoría específica.
    """
    return [tarea for tarea in tareas if tarea["categoria"].lower() == categoria.lower()]

def mostrar_tareas_clasificadas(tareas):
    """
    Muestra tareas clasificadas por estado y ordenadas por prioridad.
    """
    print("\n--- Tareas Clasificadas por Estado ---")
    for estado in ["pendiente", "en progreso", "completada"]:
        print(f"\nEstado: {estado.capitalize()}")
        tareas_estado = filtrar_por_estado(tareas, estado)
        if tareas_estado:
            for tarea in ordenar_por_prioridad(tareas_estado):
                print(f"- {tarea['descripcion']} (Prioridad: {tarea['prioridad']}, Categoría: {tarea['categoria']})")
        else:
            print("No hay tareas en este estado.")
