def buscartarea(tarea, fichero):
    nameFile = fichero+".txt"
    with open(nameFile,"r") as file:
        contenido = dict(file.read())
        print(contenido)


if __name__ == "__main__":
    buscartarea("tar","Task")
