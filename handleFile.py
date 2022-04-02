# Variable con nombre del archivo
nombreArch = 'archivo.txt'


# Funcion encargada de escribir los arreglos en el archivo
def writeInFile(array):
    # Instancia del archivo
    arch = open(nombreArch,'w')

    for i in range(0,len(array)):
        arch.write('%d' % array[i]+'\n')

    # Cierra instancia del archivo 
    arch.close()
