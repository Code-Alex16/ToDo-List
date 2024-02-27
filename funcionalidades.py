# importamos la clase tarea y el archivo con los datos
from Task import Task
from text import vocabulario as voc


def CrearTarea(titulo, descripcion, estado):
    nuevaTarea = Task(titulo, descripcion, estado)
    print("tarea creada exitosamente")
    return nuevaTarea


def EliminarTarea(indice_clave, tareas: dict):
    tareas.pop(indice_clave)
    return tareas


def CambiarEstado(indice_clave, tareas: dict, valores: list):
    # Eliminamos la anterior componente
    tareas.pop(indice_clave)
    print("seleccione el nuevo estado de la tarea")
    for i in range(1, 4):
        print(voc[f"estado {i}"])

    estado = input("Elija el estado de la tarea: ").capitalize()
    if (estado == "Comenzado") or (estado == "Suspendido") or (estado == "Terminado"):
        valores[1] = estado
        tareas[indice_clave] = valores
        return tareas
    else:
        print("El estado ingresado no es valido")
        return CambiarEstado(indice_clave, tareas, valores)


def GuardarTareas(tareas: dict, nameFichero, tareasTotales):
    name = nameFichero + ".txt"
    claves = list(tareas.keys())
    valores = list(tareas.values())
    with open(name, "a") as archivo:
        for i in range(0, tareasTotales):
            valor_especifico = valores[i]
            archivo.write(f"Titulo: {claves[i]} - estado: {valor_especifico[1]} \n")
            archivo.write(f"Descripción: {valor_especifico[0]} \n")

        archivo.close()

    print(f"Se han guardado correctamente los datos en el fichero {nameFichero}")


def MostrarTareas(nameFichero):
    name = nameFichero + ".txt"
    with open(name, "r") as archivo:
        contenido = archivo.read()
        print(contenido)
        archivo.close()


def BuscarTarea(nameFichero, tarea):
    nameFichero = nameFichero + ".txt"
    with open(nameFichero, "r") as file:
        for line in file:
            if line == tarea:
                print()
