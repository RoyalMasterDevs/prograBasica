# Funcion. Es una tarea que podemos definir dentro de nuestro programa. 

# def 

def saludar():
    print("Hola, bienvenido a Coderfy")

saludar()

def saludar_persona(nombre):
    print(f"Hola, {nombre}")
    
saludar_persona("Jorge")

# funcion con retorno
def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print("La suma es: ", resultado)

def potencia(base, exponente=2):
    return base ** exponente

print(potencia(4))
print(potencia(4, 3))