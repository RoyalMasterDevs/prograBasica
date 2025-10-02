# ciclo FOR
frutas = ["manzana", "banana", "naranja", "uva"]
for fruta in frutas:
    print(f"Me gusta la {fruta}")
    
# range() para numeros
for i in range(5):
    print(i)
# Imprime numeros del 0 al 4
for i in range(1, 11):
    print(i)
for i in range(2, 11, 2):
    print(i)
# enumerate() 
nombres = ["Ana", "Luis", "Maria", "Carlos"]

for indice, nombre in enumerate(nombres):
    print(f"Indice {indice}: {nombre}")

# While (mientras)
# Contar del 1 al 5
contador = 1

while contador <= 5:
    print(f"Contador: {contador}")
    contador = contador + 1
    # contador += 1
    
# Pedir un numero valido al usuario
numero = -1
# or
while numero < 0 or numero > 10:
    numero = int(input("Ingresa un numero entre 0 y 10: "))
    if numero < 0 or numero > 10:
            print("Numero invalido, Intenta de nuevo")
print(f"Perfecto !Elegiste el numero {numero}")
