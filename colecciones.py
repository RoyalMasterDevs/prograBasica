# Tipos de Colecciones en Python

# 1 Lista (list)
# Ordenada
# Modificable 
# Permite duplicados
# Se usa corchetes
frutas = ["manzana", "banana", "cereza", "manzana"]
print(frutas[0]) # manzana
frutas.append("pera")
print(frutas[3])

# Tupla (tuple)
# Ordenada
# Inmutable (No se puede cambiar despues de crearla)
# Permite duplicados
# Usa parentesis
numeros = (10, 20, 30, 10)
print(numeros[1]) #20
# numeros[1] = 50 

# Diccionario (dict)
# Coleccion de pares> clave: valor
# No duplican claves
# Es modificable
# {}

persona = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "CDMX"
    
}

print(persona["nombre"]) # Ana
persona["edad"] = 26
print(persona)

# Set
# No ordenado
# No permite duplicados
# Modificable
# {}
numeros = {1, 2, 3, 3, 2}
print(numeros)
# Agregar elementos
numeros.add(4)
print(numeros)
#Eliminar elementos>
numeros.remove(2)
print(numeros)

# Resumen de Diferencias
# Tipo Ordenado Modificable Duplicados Sintaxis
# Lista   Si        Si          Si          []
# Tupla   Si        No          Si          ()
# Dic     Claves    Si         No           {}
# Set     No        Si          No          {}