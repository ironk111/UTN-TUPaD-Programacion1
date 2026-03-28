#-----1
print("Hola Mundo!")

#-----2
nombre = input("¿Cuál es tu nombre? ")
print(f"Muy buenas {nombre}!")

#-----3
nombre = input("Hola!, ¿Cuál es tu nombre? ")
apellido = input("¿Cuál es tu apellido? ")
edad = input("¿Cuál es tu edad? ")
lugar_residencia = input("¿Dónde residís? ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_residencia}.")

#----4
pi = 3.14
radio = float(input("Ingresa el radio del círculo(en cm): "))
area = pi * radio * radio
perimetro = 2 * pi * radio
print(f"El área del círculo es: {area}")
print(f"El perímetro del círculo es: {perimetro}")

#-----5
# Programa que convierte segundos a horas
segundos = int(input("Ingresa el número de segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas} hora/s")

#-----6----En este caso yo conozco una forma más avanzada y fácil que sería con el bucle FOR, pero hice la tabla sin el bucle.

numero_tabla = int(input("Ingresa un número para ver su tabla de multiplicar: "))
p1 = numero_tabla * 1
p2 = numero_tabla * 2
p3 = numero_tabla * 3
p4 = numero_tabla * 4
p5 = numero_tabla * 5
p6 = numero_tabla * 6
p7 = numero_tabla * 7
p8 = numero_tabla * 8
p9 = numero_tabla * 9
p10 = numero_tabla * 10
print(f"{numero_tabla} x 1 = {p1}")
print(f"{numero_tabla} x 2 = {p2}")
print(f"{numero_tabla} x 3 = {p3}")
print(f"{numero_tabla} x 4 = {p4}")
print(f"{numero_tabla} x 5 = {p5}")
print(f"{numero_tabla} x 6 = {p6}")
print(f"{numero_tabla} x 7 = {p7}")
print(f"{numero_tabla} x 8 = {p8}")
print(f"{numero_tabla} x 9 = {p9}")
print(f"{numero_tabla} x 10 = {p10}")
    
#-----7
a = int(input("Por favor, ingresa el primer número entero (distinto de 0): "))
b = int(input("Ingresa el segundo número entero (distinto de 0): "))

suma = a + b
resta = a - b
producto = a * b
division = a / b

print(f"Si los sumamos da como resultado: {suma}")
print(f"Si los restamos da como resultado: {resta}")
print(f"Si los multiplicamos da como resultado: {producto}")
print(f"Si los dividimos da como cociente: {division}")

#-----8
altura = float(input("Ingresa tu altura en metros (ej. 1.75): "))
peso = float(input("Ingresa tu peso en kilogramos (ej. 60.5): "))
imc = peso / (altura * altura)
print(f"Tu índice de masa corporal (IMC) es: {imc}")

#-----9
celsius = float(input("Ingresa la temperatura en grados Celsius: "))
fahrenheit = (9/5) * celsius + 32
print(f"{celsius} °C equivalen a {fahrenheit} °F")

#-----10
# Programa que pide 3 números y calcula su promedio
n1 = float(input("Ingresa el primer número: "))
n2 = float(input("Ingresa el segundo número: "))
n3 = float(input("Ingresa el tercer número: "))

promedio = (n1 + n2 + n3) / 3

print(f"El promedio de los tres números es: {promedio}")

