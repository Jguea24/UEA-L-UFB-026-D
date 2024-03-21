# Crear un diccionario llamado informacion_personal
informacion_personal = {
    "nombre": "Johnnny ",
    "edad": 22,
    "ciudad": "Tena",
    "profesion": "Estudiante de Universodad Estatal Amazonica"
}

# Acceder al valor asociado con la clave "ciudad" y modificarlo
informacion_personal["ciudad"] = "Archidona"

# Agregar una nueva clave-valor que represente la "profesion" de la persona
informacion_personal["profesion"] = "Estudiantes_UEA"

# Verificar si la clave "telefono" existe y, si no existe, agregarla con un número de teléfono ficticio
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0989894314"

# Eliminar la clave "edad" del diccionario
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Imprimir el diccionario resultante

print(informacion_personal)
