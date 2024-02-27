#Variable con el texto a utilizar dentro del programa se importara la variable para su uso
vocabulario = {
    "titulo" : "--------------- Bienvenido a la ToDo - List ---------------",
    "opcion 1" : "1. Crear una nueva Tarea",
    "opcion 2" : "2. Eliminar una nueva tarea",
    "opcion 3" : "3. Cambiar el estado de una tarea",
    "opcion 4" : "4. Guardar tareas",
    "opcion 5" : "5. Mostrar tareas Guardadas",
    "opcion 6" : "6. salir",
    "error" : "Existe un error dentro del programa",
    "estado 1" : "Comenzada",
    "estado 2" : "Suspendida",
    "estado 3" : "Terminada",
    "Guardado 1": "Iniciando guardado de las Tareas, porfavor espere",
    "Guardado 2": "Guardado exitosamente en el fichero 'Tareas.txt'..."
}

'''
otra manera de realizar esto es mediante una funcion ejemplo:
def getDatos():
    return {
        "titulo":"datos del titulo ..."
        ...
    }

esta tambien se importa y se guarda dentro de una variable ejem: 
import archivo as arch
mis_datos = arch.getDatos()
'''