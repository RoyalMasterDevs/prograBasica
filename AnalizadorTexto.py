# Crear un analizador de texto, en base a un texto que el usuario ingrese, el programa debe hacer:
# 1. Contar la cantidad de letras repetidas en el texto ingresado.
# 2. Contar la cantidad de palabras.
# 3. Mencionar las letras de inicio y fin.
# 4. Invertir el texto del usuaio por los JAJAS.
# 5. Buscar la palabra "python".

# Variables del programa
texto = input("Ingresa un texto a eleccion: ")
letras = []

# Se transforma todo el texto en minus.
texto = texto.lower()

# El usuario ingresa las letras y las almacena en la variable "letras"
letras.append(input("Ingresa la primera letra: ").lower())
letras.append(input("Ingresa la primera letra: ").lower())
letras.append(input("Ingresa la primera letra: ").lower())

print("\n") # Hace un salto de linea en la consola

# 1 Devuelve la cantidad de letras
print("CANTIDAD DE LETRAS")
cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])

print(f"Hemos encontrado la letra '{letras[0]}' repetida {cantidad_letras1} veces")
print(f"Hemos encontrado la letra '{letras[1]}' repetida {cantidad_letras2} veces")
print(f"Hemos encontrado la letra '{letras[2]}' repetida {cantidad_letras3} veces")


print("\n")
# 2 Devuelve la cantidad de Palabras
print("CANTIDAD DE PALABRAS")
# split
palabras = texto.split()
print(f"Hemos encontrado {len(palabras)} palabras en tu texto.")

# 3 Menciona las letras de inicio y fin
print("\n")
print("LETRAS DE INICIO Y FIN")

letra_inicio = texto[0]
letra_final = texto[-1]

print(f"La letra inicial es '{letra_inicio}' y la letra final es '{letra_final}'.")

# 4. Invertir el texto del usuaio por los JAJAS.
print("\n")
print("TEXTO INVERTIDO")
palabras.reverse()
texto_invertido = ' '.join(palabras)
print(f"Si ordenamos tu texto al reves va a decir: '{texto_invertido}'.")

# 5. Buscar la palabra "python".
print("BUSCANDO LA PALABRA 'python'")
buscar_python = 'python' in texto
dic = {True:"si", False:"no"}
print(f"La palabra 'python' {dic[buscar_python]} se encuentra en el texto.")
# Tarea
# Hacer que la busqueda de la palabra sea dinamica.
# Opcional. Cambiar la variable por un IF