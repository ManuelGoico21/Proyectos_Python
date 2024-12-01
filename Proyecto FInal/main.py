# main.py

from tareas import crear_tarea, leer_tareas, actualizar_tarea, eliminar_tarea
from utilidades import (
    cargar_datos,
    guardar_datos,
    mostrar_tareas_clasificadas,
    filtrar_por_categoria
)

# Archivo de datos para persistencia
ARCHIVO_DATOS = "datos.json"

def mostrar_menu():
    print("\n--- Sistema de Gestión de Tareas ---")
    print("1. Crear nueva tarea")
    print("2. Leer tareas existentes")
    print("3. Actualizar tarea")
    print("4. Eliminar tarea")
    print("5. Mostrar tareas clasificadas")
    print("6. Filtrar por categoría")
    print("7. Salir")

def main():
    # Cargar tareas desde archivo
    tareas = cargar_datos(ARCHIVO_DATOS)

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            crear_tarea(tareas)
        elif opcion == "2":
            leer_tareas(tareas)
        elif opcion == "3":
            actualizar_tarea(tareas)
        elif opcion == "4":
            eliminar_tarea(tareas)
        elif opcion == "5":
            mostrar_tareas_clasificadas(tareas)
        elif opcion == "6":
            categoria = input("Introduce la categoría para filtrar: ")
            tareas_categoria = filtrar_por_categoria(tareas, categoria)
            if tareas_categoria:
                print("\n--- Tareas en la Categoría ---")
                for tarea in tareas_categoria:
                    print(f"- {tarea['descripcion']} (Estado: {tarea['estado']}, Prioridad: {tarea['prioridad']})")
            else:
                print(f"No hay tareas en la categoría '{categoria}'.")
        elif opcion == "7":
            guardar_datos(tareas, ARCHIVO_DATOS)
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
