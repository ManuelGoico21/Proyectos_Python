# tareas.py

import uuid

def crear_tarea(tareas):
    """Permite al usuario crear una nueva tarea."""
    descripcion = input("Descripción de la tarea: ")
    fecha_limite = input("Fecha límite (YYYY-MM-DD): ")
    prioridad = input("Prioridad (baja/media/alta): ")
    categoria = input("Categoría: ")

    tarea = {
        "id": str(uuid.uuid4()),
        "descripcion": descripcion,
        "fecha_limite": fecha_limite,
        "prioridad": prioridad.lower(),
        "categoria": categoria,
        "estado": "pendiente"  # Estado inicial
    }
    tareas.append(tarea)
    print("✔ Tarea creada con éxito.")

def leer_tareas(tareas):
    """Muestra todas las tareas con sus detalles."""
    if not tareas:
        print("No hay tareas disponibles.")
        return

    print("\n--- Lista de Tareas ---")
    for tarea in tareas:
        print(f"ID: {tarea['id']}")
        print(f"Descripción: {tarea['descripcion']}")
        print(f"Fecha límite: {tarea['fecha_limite']}")
        print(f"Prioridad: {tarea['prioridad']}")
        print(f"Categoría: {tarea['categoria']}")
        print(f"Estado: {tarea['estado']}")
        print("-" * 20)

def actualizar_tarea(tareas):
    """Permite al usuario actualizar los detalles de una tarea existente."""
    tarea_id = input("Introduce el ID de la tarea a actualizar: ")

    # Buscar tarea por ID
    tarea = next((t for t in tareas if t["id"] == tarea_id), None)

    if not tarea:
        print("❌ No se encontró una tarea con ese ID.")
        return

    print("\n--- Información Actual de la Tarea ---")
    print(f"Descripción: {tarea['descripcion']}")
    print(f"Fecha límite: {tarea['fecha_limite']}")
    print(f"Prioridad: {tarea['prioridad']}")
    print(f"Categoría: {tarea['categoria']}")
    print(f"Estado: {tarea['estado']}")

    # Permitir al usuario modificar los campos
    nueva_descripcion = input("Nueva descripción (deja vacío para mantener actual): ")
    nueva_fecha = input("Nueva fecha límite (YYYY-MM-DD, deja vacío para mantener actual): ")
    nueva_prioridad = input("Nueva prioridad (baja/media/alta, deja vacío para mantener actual): ")
    nueva_categoria = input("Nueva categoría (deja vacío para mantener actual): ")
    nuevo_estado = input("Nuevo estado (pendiente/en progreso/completada, deja vacío para mantener actual): ")

    # Actualizar solo los campos que el usuario haya modificado
    if nueva_descripcion:
        tarea["descripcion"] = nueva_descripcion
    if nueva_fecha:
        tarea["fecha_limite"] = nueva_fecha
    if nueva_prioridad:
        tarea["prioridad"] = nueva_prioridad.lower()
    if nueva_categoria:
        tarea["categoria"] = nueva_categoria
    if nuevo_estado:
        tarea["estado"] = nuevo_estado.lower()

    print("✔ Tarea actualizada con éxito.")

def eliminar_tarea(tareas):
    """Permite al usuario eliminar una tarea existente."""
    tarea_id = input("Introduce el ID de la tarea a eliminar: ")

    # Buscar tarea por ID
    tarea = next((t for t in tareas if t["id"] == tarea_id), None)

    if not tarea:
        print("❌ No se encontró una tarea con ese ID.")
        return

    # Confirmar eliminación
    confirmacion = input(f"¿Estás seguro de que deseas eliminar la tarea '{tarea['descripcion']}'? (s/n): ")
    if confirmacion.lower() == "s":
        tareas.remove(tarea)
        print("✔ Tarea eliminada con éxito.")
    else:
        print("❌ Operación cancelada.")
