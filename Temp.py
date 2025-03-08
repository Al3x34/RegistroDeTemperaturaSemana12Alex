# Lista con los nombres de las ciudades
ciudades = ["Pastaza", "Ambato", "Quito"]

# Lista que almacena las temperaturas de cada ciudad
# Cada ciudad tiene 2 semanas, y cada semana tiene 7 días
temperaturas = [
    [[30, 32, 31, 29, 33, 34, 31], [29, 31, 32, 30, 33, 32, 30]],  # Pastaza
    [[22, 24, 23, 22, 24, 25, 23], [21, 23, 22, 23, 24, 25, 22]],  # Ambato
    [[18, 20, 19, 21, 22, 23, 20], [19, 21, 20, 22, 23, 24, 21]]   # Quito
]

# Recorrer la lista de ciudades usando un bucle
for i in range(len(ciudades)):  # 'i' representa el índice de la ciudad
    print(f"{ciudades[i]}:")  # Muestra el nombre de la ciudad

    # Recorre la lista de semanas dentro de la ciudad
    for j in range(len(temperaturas[i])):  # 'j' representa el índice de la semana
        suma = sum(temperaturas[i][j])  # Sumar todas las temperaturas de la semana
        promedio = suma / len(temperaturas[i][j])  # Calcular el promedio dividiendo por 7
        print(f"  Semana {j + 1}: {promedio:.2f}°C")  # Mostrar el promedio con 2 decimales

    print()  # Se Agrega una línea en blanco para separar ciudades
