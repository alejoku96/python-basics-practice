# Ejercicio 1: Variables y tipos de datos

mi_nombre = "Alejandro"
mi_edad = 28
mi_altura = 1.70
soy_estudiante = True

print(f"Nombre: {mi_nombre}, Tipo: {type(mi_nombre)}")
print(f"Edad: {mi_edad}, Tipo: {type(mi_edad)}")
print(f"Altura: {mi_altura}, Tipo: {type(mi_altura)}")
print(f"Es estudiante: {soy_estudiante}, Tipo: {type(soy_estudiante)}")

print(isinstance(mi_nombre, str))
print(isinstance(mi_edad, int))


# Ejercicio 2: Métodos de cadenas

texto_sucio = " hOlA mUnDo, eStO eS pYtHoN "
texto_limpio = texto_sucio.strip().capitalize()
print(texto_limpio)


# Ejercicio 3: Cortador de cadenas

correo = "estudiante.software@upn.edu.pe"
correo_simbolo = correo.find("@")
correo_usuario = correo[:correo_simbolo]
correo_dominio = correo[correo_simbolo + 1:]

print(f"Usuario: {correo_usuario}")
print(f"Dominio: {correo_dominio}")


# Ejercicio 4: Interpolación y Concatenación de cadenas

presentacion_concatenada = "Hola, mi nombre es " + mi_nombre + ", tengo " + str(mi_edad) + " años y mido " + str(mi_altura) + " metros."
presentacion_f_string = f"Hola, mi nombre es {mi_nombre}, tengo {mi_edad} años y mido {mi_altura} metros."

print(presentacion_concatenada)
print(presentacion_f_string)


# Ejercicio 5: Generador de Usuarios

  # Pide al usuario (o define tú mismo) un nombre_completo y un año_nacimiento.
nombre_completo = input("Ingrese su primer nombre y apellido: ")
año_nacimiento = int(input("Ingrese su año de nacimiento: "))

  # Usando métodos de strings, asegúrate de que el nombre esté todo en minúsculas y sin espacios en los extremos.
nombre_completo_limpio = nombre_completo.strip().lower()

  # Usando slicing, toma la primera letra del nombre y el apellido.
primera_letra_nombre = nombre_completo_limpio[0]
apellido = nombre_completo_limpio.split()[-1]

  # Usando f-strings, crea un nombre de usuario que sea la primera letra del nombre, seguida del apellido completo, seguido de los últimos dos dígitos del año de nacimiento.
nombre_usuario = f"{primera_letra_nombre}{apellido}{str(año_nacimiento)[-2:]}"
print(f"Nombre de usuario generado: {nombre_usuario}")
