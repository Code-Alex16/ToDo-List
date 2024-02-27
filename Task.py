#Clase tarea con metodo de obtencion y modificacion de atributos
class Task:

    #iniciamos por defecto con valores nulos los datos
    def __init__(self,id,titulo,descipcion,estado):
        self.id = id
        self.titulo = titulo
        self.descripcion = descipcion
        self.estado = estado
    
    def getId(self):
        return self.id

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