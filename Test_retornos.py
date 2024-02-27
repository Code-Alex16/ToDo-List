#Variables globales
dicTask = {}
id = 0

class Task:

    #iniciamos por defecto con valores nulos los datos
    def __init__(self,id,titulo,descipcion,estado):
        self.id = id
        self.titulo = titulo
        self.descripcion = descipcion
        self.estado = estado
    
    def getTitulo(self):
        return self.titulo
    
    def getDescripcion(self):
        return self.descripcion
    
    def getEstado(self):
        return self.estado
    
    def setTitulo(self,nuevoTitulo):
        self.titulo = nuevoTitulo

    def setDescripcion(self, nuevaDescripcion):
        self.descripcion = nuevaDescripcion
    
    def setEstado(self,nuevoEstado):
        self.estado = nuevoEstado


#Funcion para crear los objetos y retornarlos para su respectivo guardado clasificados mediante su id
def Crear_Persona(id) -> Task:
	nombre = input("Ingrese el nombre de la tarea: ")
	descripcion = input("ingrese la descripcion de la tarea: ")
	id += 1
	return id,Task(id,nombre,descripcion,"Comenzado")



seguir = True
while seguir:
	id,objec = Crear_Persona(id)
	dicTask[id] = objec
	print(dicTask)

	print(f"title: {dicTask[id].titulo} \ndescripcion: {dicTask[id].descripcion}\n")