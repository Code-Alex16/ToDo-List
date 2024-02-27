#importamos todos los modulos a usar
import funcionalidades as fn
#para el archivo texto importamos la variable vocabulario nombrada como nte
from text import vocabulario as nte

def main():
    tareas = {}
    while True:
        print(nte["titulo"])
        for i in range(1,7):
            print(nte[f"opcion {i}"])
        
        userOption = int(input("eliga una de las opciones establecidas anteriormente: "))
        
        if (userOption == 1): #creamos una nueva tarea por defecto comenzada
            titulo = input("Ingrese el titulo de la tarea: ")
            descipcion = input("Ingrese la descipcion de la tarea: ")
            tarea = fn.CrearTarea(titulo,descipcion,"comenzada")

            #guardado provisional
            tareas[tarea.getTitulo()] = [tarea.getDescripcion(), tarea.getEstado()]
            
        elif (userOption == 2): #Eliminamos una tarea existente 

            #Mostramos todas las tareas existentes
            for i,keys in enumerate(tareas.keys()):
                print(f"{i+1}: {keys}")

            #validamos los datos ingresados    
            try:
                userSelection = int(input("elija la tarea que desea eliminar: "))

                #creamos una lista con las claves del diccionario
                claves = list(tareas.keys())

                #enviamos la clave buscada por el indice en una lista y el diccionario original
                nuevasTareas = fn.EliminarTarea(claves[userSelection-1],tareas)
                tareas.clear
                tareas = nuevasTareas

            except:
                print("seleccione una opcion valida\n")

        elif (userOption == 3):
            for i,keys in enumerate(tareas.keys()):
                print(f"{i+1}: {keys} - estado: {tareas[keys][1]}")

            #validamos los datos ingresados    
            try:
                userSelection = int(input("elija la tarea que desea cambiar el estado: "))

                #creamos una lista con las claves del diccionario
                claves = list(tareas.keys())
                valores = list(tareas.values())
                
                #enviamos la clave buscada por el indice en una lista y el diccionario original
                nuevasTareas = fn.CambiarEstado(claves[userSelection-1],tareas,valores[userSelection-1])
                tareas.clear
                tareas = nuevasTareas
                
            except:
                print("seleccione una opcion valida\n")
        
        elif (userOption == 4):
            nameFichero = input("Ingrese el nombre del fichero donde se guardara todas las tareas: ")
            fn.GuardarTareas(tareas,nameFichero,len(tareas))

        elif (userOption == 5):
            print("Indique el nombre del fichero que guardo sus Tareas")
            nameFile = input("Ingrese el nombre del fichero: ")
            fn.MostrarTareas(nameFile)

        elif (userOption == 6):
            break
        

if __name__ == "__main__":
    main()