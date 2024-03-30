def convertir_Celsius(celsius):
    # Convertir a Fahrenheit
    fahrenheit = (celsius * 9 / 5) + 32
    # Convertir a Kelvin
    kelvin = celsius + 273.15
    # Devolver una tupla con los valores convertidos
    return (fahrenheit, kelvin)

# Obtener la entrada del usuario en grados Celsius
celsius = float(input("Ingresa la temperatura en grados Celsius: "))

# Llamar a la función para convertir los grados Celsius ingresados por el usuario
grados_fahrenheit, kelvin = convertir_Celsius(celsius)

# Imprimir los resultados
print(f"{celsius} grados Celsius equivalen a {grados_fahrenheit} grados Fahrenheit ")

print(f'{grados_fahrenheit} grados Fahrenheit  equivale a {kelvin} kelvin')