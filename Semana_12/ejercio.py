# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)
import random
import random

# Definir las ciudades, días de la semana y semanas
ciudades =  ['Napo', 'Pastaza', 'Orellana']

dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

semanas = ['Semana 1', 'Semana 2', 'Semana 3', 'Semana 4']

# Crear una matriz para almacenar las temperaturas
temperaturas = [[[random.randint(0, 40) for _ in dias_semana] for _ in semanas] for _ in ciudades]

# Calcular y mostrar la suma total de temperaturas por ciudad
for ciudad, temps_ciudad in zip(ciudades, temperaturas):
    print(f"Suma total de temperaturas para {ciudad}:")
    suma_total = 0
    for temps_semana in temps_ciudad:
        suma_total += sum(temps_dia for temps_dia in temps_semana)
    print(f"Suma total: {suma_total} grados Celsius")
    print()
