# Metodos Basicos en Python
# Ejemplo con cadenas (str):

texto = "Hola Mundo"
print(texto.lower()) # hola mundo
print(texto.upper()) # HOLA MUNDO
print(texto.replace("Mundo", "Python")) # Hola Python
print(len(texto)) # Longitud = 10

numeros = [10, 20, 30] # agrega al final
numeros.append(40)
print(numeros)
numeros.remove(20) # elimina el 20
print(numeros)
print(len(numeros)) # 3 elementos