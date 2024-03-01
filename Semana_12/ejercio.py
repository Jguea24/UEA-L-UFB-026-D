# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)
import random

# Definir las ciudades, días de la semana y semanas
ciudades =['Tena', 'Archidona', 'Chaco']

Dia_semana = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']

Semanas_Enero = ['Semana1', 'Semana2', 'Semana3']

# Almacenamiento de matriz de temperaturas

temperaturasdiarias = [[[random.randint(0,45)for _ in Dia_semana]for _ in Semanas_Enero] for _ in ciudades]

# vamos a calcular el promedio por ciudades y semanas y

for ciudad, tems_ciudad in zip(ciudades,  temperaturasdiarias):

    print(f"Promedio de temperaturas para {ciudad}:")

    for Semana, temperaturaSemana in zip( Semanas_Enero, tems_ciudad):

        promedio = sum(temperaturadia for temperaturadia in temperaturaSemana) / len (temperaturaSemana)

        print (f"{Semana}: {promedio:.2f} grados celsius")
    print()
