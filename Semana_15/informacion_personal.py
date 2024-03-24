# Crear un diccionario llamado informacion_personal
#  Crear un Diccionario
informacion_johnny = { "nombre": "Johnny",
                        "edad": 21,
                        "ciudad": "Tena",
                        "profesion": "Estudiante de Universodad Estatal Amazonica"}
#Acceder y Modificar Valores:
# Acceder al valor asociado con la clave "ciudad" y modificarlo
informacion_johnny["ciudad"] = "Archidona"

informacion_johnny["profesion"] = "Estudiantes_UEA"

# Verificar si la clave "telefono" existe y, si no existe, agregarla con un número de teléfono ficticio
if "telefono" not in informacion_johnny:
    informacion_johnny["telefono"] = "0989894314"

# Eliminar la clave "edad" del diccionario
if "edad" in informacion_johnny:
    del informacion_johnny["edad"]

# Imprimir el diccionario resultante

print(informacion_johnny)
