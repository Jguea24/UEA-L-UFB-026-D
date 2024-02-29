# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)
# Definir las ciudades, días de la semana y semanas

import random
ciudades_Napo = ['Archidona ', 'Tena', 'Chaco']

dias_semana = ['Lunes  ',
               'Martes',
               'Miércoles',
               'Jueves',
               'Viernes',
               'Sábado',
               'Domingo']
Semanas_de_Enero = ['Semana 1', 'Semana 2', 'Semana 3', 'Semana 4']

# Crear una matriz para almacenar las temperaturas
temperaturas_Grado = [[[random.randint(0, 40) for _ in dias_semana] for _ in Semanas_de_Enero] for _ in ciudades_Napo]

# Calcular y mostrar el promedio de temperaturas por ciudad y semana

for ciudad, temps_ciudad in zip(ciudades_Napo, temperaturas_Grado):

    print(f"Promedio de temperaturas para {ciudad}:  ")

    for semana, temps_semana in zip(Semanas_de_Enero, temps_ciudad):

        promedio = sum(temps_dia for temps_dia in temps_semana) / len(temps_semana)

        print(f"{semana}: {promedio:.2f} grados Celsius")
    print()