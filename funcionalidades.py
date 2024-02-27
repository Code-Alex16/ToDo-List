# importamos la clase tarea y el archivo con los datos
from Task import Task
from text import vocabulario as voc

'''
Modulo de funciones para la creacion, eliminacion, modificacion y guardado de las tareas 
dentro del programa principal
'''

#funcion para la creacion de una nueva tarea, retorno de un objeto
def CrearTarea(id,titulo, descripcion, estado) -> Task:
    NuevaTarea = Task(id,titulo, descripcion, estado)
    print("tarea creada exitosamente")
    return NuevaTarea

#funcion eliminacion de Tarea mediante el id
def EliminarTarea(id : int, tareas: dict) -> dict:
    if id in tareas:
        del tareas[id]
        print(f"Tarea con ID {id} eliminada exitosamente.")
    else:
        print(f"No existe una tarea con el ID {id}.")
    return tareas


#Modificacion de una Tarea 
def CambiarEstado(id, Tareas: dict) -> dict:
    print("seleccione el nuevo estado de la tarea")
    for i in range(1, 4):
        print(voc[f"estado {i}"])

    estado = input("Elija el estado de la tarea: ").capitalize()
    if estado in ["Comenzada", "Suspendida", "Terminada"]:  # Lista de estados válidos
        objeto_a_modificar = Tareas[id]
        objeto_a_modificar.setEstado(estado)
        Tareas[id] = objeto_a_modificar
        return Tareas
    else:
        print("El estado ingresado no es válido")
        return CambiarEstado(id, Tareas)


def GuardarTareas(Tareas : dict) -> None:
    name = "Tareas.txt"
    with open(name, "a") as archivo:
        for id,tarea in enumerate(Tareas.values()):
            archivo.writelines(f"{id}. {tarea.getTitulo()} - status: {tarea.getEstado()} \n")
            archivo.writelines(f"Descripcion: {tarea.getDescripcion()} \n")

        archivo.close()

    print(voc["Guardado 2"])


def MostrarTareas():
    nombre_archivo = "Tareas.txt"  
    try:
        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                # Procesar la línea
                print(linea.strip())  # .strip() elimina los espacios en blanco al principio y al final de la línea
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no fue encontrado.")
    except IOError:
        print("Ocurrió un error al intentar leer el archivo.")


# TO-DO completa la opcion de buscar una tarea esecifica 
'''
def BuscarTarea():
   pass 
'''