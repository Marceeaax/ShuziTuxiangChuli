def promedio(lista):
    suma = sum(lista)
    promedio = suma / len(lista)
    return promedio, suma

def moda(lista):
    frecuencias = {}
    for elemento in lista:
        if elemento in frecuencias:
            frecuencias[elemento] += 1
        else:
            frecuencias[elemento] = 1
    
    moda = None
    max_frecuencia = 0
    for elemento, frecuencia in frecuencias.items():
        if frecuencia > max_frecuencia:
            moda = elemento
            max_frecuencia = frecuencia
    return moda
