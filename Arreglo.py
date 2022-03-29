arreglo = [10, 7, 6, 10, 4, 9, 10, 5, 9, 8, 4, 3, 1, 10, 10, 10, 2]
suma = 0
for valor in arreglo:
    suma = suma + valor
    print(f"La suma es {suma}")
    cantidad_elementos = len(arreglo)
promedio = suma / cantidad_elementos
print(f"El promedio es {promedio}")