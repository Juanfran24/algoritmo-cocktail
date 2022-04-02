
def cocktailSort(a):
    # Arreglo de numeros que están en el archivo
    arr = [] 
    
    # Instancia del archivo
    arh = open(a,'r')
    
    # For encargado de leer numeros del archivo y concatenarlos en un arreglo
    for num in arh:
        n = num.rstrip()
        arr.append(int(n))
    
    
    n = len(arr)
    swapped = True
    start = 0
    end = n-1

    while (swapped == True):
 
        swapped = False
 
        for i in range(start, end):
            if (arr[i] > arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
 
        if (swapped == False):
            break
 
        swapped = False
 
        end = end-1
 
        for i in range(end-1, start-1, -1):
            if (arr[i] > arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
 
        start = start + 1
 