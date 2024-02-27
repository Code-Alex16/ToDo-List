#Clase tarea con metodo de obtencion y modificacion de atributos
class Task:

    #iniciamos por defecto con valores nulos los datos
    def __init__(self,titulo,descipcion,estado):
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