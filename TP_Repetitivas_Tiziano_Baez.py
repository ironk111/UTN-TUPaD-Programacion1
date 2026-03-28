import random

# 1 --------------

for num_Entero in range(1, 101):
    print(num_Entero)
    num_Entero += 1

# 2 --------------

num_Entero = int(input("Ingrese un número entero: "))
print(f"Tu número ingresado tiene {len(str(num_Entero))} dígitos")

# 3 --------------

valor1 = int(input("Ingrese el primer valor entero: "))
valor2 = int(input("Ingrese el segundo valor entero: "))

if valor1 < valor2:
    inicio = valor1 + 1
    fin = valor2 - 1
else:
    inicio = valor2 + 1
    fin = valor1 - 1

suma = 0
i = inicio
while i <= fin:
    suma += i
    i += 1

print("La suma de los enteros entre", valor1, "y", valor2, "excluyéndolos es:", suma)

# 4 --------------

acumulado = 0

while True:
    numero = int(input("Ingrese un número entero (0 para terminar): "))
    if numero == 0:
        break
    acumulado += numero

print("Total acumulado:", acumulado)

# 5 --------------

num_Elegido = random.randint(0, 9)
num_Ingresado = -1
intentos = 0

while num_Ingresado != num_Elegido:
    num_Ingresado = int(input("Adivina el número entre 0 y 9: "))
    intentos += 1

print(f"¡Adivinaste el número en {intentos} intentos!")
        
# 6 --------------

for i in range(100, 0, -2):
    print(i)

# 7 --------------

numero = int(input("Ingrese un número entero positivo: "))
suma = 0

for i in range(0, numero + 1):
    suma += i

print(f"La suma de todos los números entre 0 y {numero} es: {suma}")

# 8 --------------

cantidad = 2  # Valor a cambiar para procesar una cantidad diferente de numeros

pares = 0
impares = 0
negativos = 0
positivos = 0

for i in range(cantidad):
    numero = int(input(f"Ingrese el número {i + 1}/{cantidad}: "))
    
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    if numero < 0:
        negativos += 1
    elif numero > 0:
        positivos += 1

print(f"""Resultados:
Números pares: {pares}
Números impares: {impares}
Números negativos: {negativos}
Números positivos: {positivos}""")

# 9 --------------

cantidad = 2  # Valor a cambiar para procesar una cantidad diferente de numeros
suma = 0

for i in range(cantidad):
    numero = int(input(f"Ingrese el número {i + 1}/{cantidad}: "))
    suma += numero

media = suma / cantidad

print(f"La media de los {cantidad} números ingresados es: {media}")

# 10 --------------

numero = input("Ingrese un número: ")
numero_invertido = numero[::-1]

print(f"El número {numero} invertido es: {numero_invertido}")

