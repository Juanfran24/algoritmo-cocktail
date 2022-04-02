import random
import time
import handleFile,algoritmo

# Variable con nombre del archivo
nom = handleFile.nombreArch


# Creacion de arreglos 10, 100, 1000, 10000, 100000 
arr1 = random.sample(range(50),10)
arr2 = random.sample(range(500),100)
arr3 = random.sample(range(5000),1000)
arr4 = random.sample(range(50000),10000)
arr5 = random.sample(range(500000),100000)

# Escritura de numeros en archivo
handleFile.writeInFile(arr4)

# Toma de tiempos

startCocktail = time.time()
algoritmo.cocktailSort(nom)
endCocktail = time.time()

print(f"tiempo: {endCocktail-startCocktail}")