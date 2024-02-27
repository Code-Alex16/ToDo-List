#importamos todos los modulos a usar
import funcionalidades as fn
from text import vocabulario as nte

def main():

    #variable a utilizar instanciadas desde el inicio
    tareas = {}
    id = 1

    #ciclo para la repetitividad de las tareas
    while True:

        #Mostramos por consola texto plano
        print(nte["titulo"])
        for i in range(1,7):
            print(nte[f"opcion {i}"])
        
        userOption = int(input("eliga una de las opciones establecidas anteriormente: "))
        

        #creamos una nueva tarea por defecto comenzada
        if (userOption == 1): 
            titulo = input("Ingrese el titulo de la tarea: ")
            descipcion = input("Ingrese la descipcion de la tarea: ")
            
            #guardamos con indice el id y el objeto tipo tarea
            tareas[id] = fn.CrearTarea(id,titulo,descipcion,"comenzada")

            #aumentamos el valor de id para que se incremente de manera automatica
            id += 1

        #Eliminamos una tarea existente 
        elif (userOption == 2): 
            if not tareas:
                print("No hay tareas para eliminar.")
            else:
                print("| id | Task")
                for tarea in tareas.values():
                    print(f"| {tarea.getId()}  | {tarea.getTitulo()}")
                
                try:
                    userSelection = int(input("elija la tarea que desea eliminar, seleccione su id: "))

                    # Verificamos si la tarea seleccionada existe antes de intentar eliminarla
                    if userSelection in tareas:
                        nuevasTareas = fn.EliminarTarea(userSelection,tareas)
                        tareas = nuevasTareas
                    else:
                        print("No existe una tarea con ese ID.")
                except ValueError:
                    print("Por favor, ingrese un ID de tarea válido.")

        #Cmabio de estado de una tarea existente
        elif (userOption == 3):
            print("| id | Task                        | status     |")
            #Mostramos todas las tareas existentes
            for tarea in tareas.values():
                print(f"| {tarea.getId()}  | {tarea.getTitulo()}                    | {tarea.getEstado()}     |")
            
            #validamos los datos ingresados    
            try:
                userSelection = int(input("elija la tarea que desea cambiar el estado: "))
                
                #enviamos el id y el diccionario con las tareas indexadas por su id como llave y un objeto como valor
                nuevasTareas = fn.CambiarEstado(userSelection,tareas)
                tareas.clear
                tareas = nuevasTareas
        
            except:
                print("seleccione una opcion valida\n")
        
        elif (userOption == 4):
            print(nte["Guardado 1"])
            fn.GuardarTareas(tareas)

        elif (userOption == 5):
            fn.MostrarTareas()

        elif (userOption == 6):
            break
        

if __name__ == "__main__":
    main()