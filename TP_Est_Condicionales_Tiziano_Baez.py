# 1 ------
edad = int(input("Ingrese su edad en número: "))

if edad >= 18:
    print("Es mayor de edad")

# 2 ------
nota = float(input("Ingrese su nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# 3 ------
num = int(input("Por favor, ingrese un número entero: "))

if num % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingresar un número par")

# 4 ------
edad = int(input("Ingrese su edad en años: "))

if edad < 12 and edad > 0:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

# 5 ------
password = input("Ingrese su contraseña nueva: ")

if len(password) >= 8 and len(password) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# 6 ------
consumo_Energetico = float(input("Ingrese su consumo mensual de energía eléctrica en kWh: "))

if consumo_Energetico < 150:
    print("Consumo bajo.")
elif consumo_Energetico >= 150 and consumo_Energetico <= 300:
    print("Consumo medio.")
else:
    # Si es mayor a 300 kWh
    print("Consumo alto.")
    # Y si pasa los 500 kWh
    if consumo_Energetico > 500:
        print("Considere medidas de ahorro energético.")

# 7 ------
string = input("Ingrese una palabra o una frase: ")

# Uso -1 para acceder al último carácter de la frase o palabra, y se verifica si es una vocal
if string[-1] in ("AEIOUaeiou"):
    print(f"{string}!")
else:
    print(string)

# 8 ------
nombre = input("Ingrese su nombre: ")

# Uso la triple commilla para mostrar el texto con saltos de línea y que se vea mejor
print("""
Elija el número según cómo quiere que se vea su nombre:
1. Si quiere su nombre en MAYÚSCULAS.
2. Si quiere su nombre en minúsculas.
3. Si quiere su nombre con la primera letra Mayúscula.
""")

opcion = int(input("Ingrese el número de operación que desea realizar (1, 2 o 3): "))

if opcion == 1:
    nombre_Mayus = nombre.upper()
    print(nombre_Mayus)
elif opcion == 2:
    nombre_Minuscula = nombre.lower()
    print(nombre_Minuscula)
elif opcion == 3:
    nombre_Title = nombre.title()
    print(nombre_Title)
# En caso de error, si el usuario ingresa un número diferente a 1, 2 o 3
else:
    print("Por favor, ingrese únicamente 1, 2 o 3")

# 9 ------------------
magnitud_terremoto = float(input("Indique la magnitud del terremoto según la escala de Ritcher: "))

if magnitud_terremoto < 3:
    print("Muy leve")
elif magnitud_terremoto >= 3 and magnitud_terremoto < 4:
    print("Leve")
elif magnitud_terremoto >= 4 and magnitud_terremoto < 5:
    print("Moderado")
elif magnitud_terremoto >= 5 and magnitud_terremoto < 6:
    print("Fuerte")
elif magnitud_terremoto >= 6 and magnitud_terremoto < 7:
    print("Muy fuerte")
else:
    print("Extremo")

# 10 ------------------

# Se pregunta el hemisferio, mes y día al usuario
hemisferio = input("¿En qué hemisferio se encuentra? (N/S): ").upper()
hemisferio = hemisferio.lower()
mes = int(input("¿Qué mes del año es? (1-12): "))
dia = int(input("¿Qué día del mes es? (1-31): "))

# --------------------Hemisferio sur
if hemisferio == "s":
    # Es verano si, es después del 21/12, en cualquier día de enero o febrero, o antes del 20/3
    if (mes == 12 and dia >= 21) or (mes in (1,2)) or (mes == 3 and dia <= 20):
        print("Verano")
    # Es otoño si, es después del 21/3, en cualquier día de abril o mayo, o antes del 20/6
    elif (mes == 3 and dia >= 21) or (mes in (4,5)) or (mes == 6 and dia <= 20):
        print("Otoño")
    # Es invierno si, es después del 21/6, en cualquier día de julio o agosto, o antes del 20/9
    elif (mes == 6 and dia >= 21) or (mes in (7,8)) or (mes == 9 and dia <= 20):
        print("Invierno")
    # Es primavera si, es después del 21/9, en cualquier día de octubre o noviembre, o antes del 20/12
    elif (mes == 9 and dia >= 21) or (mes in (10,11)) or (mes == 12 and dia <= 20):
        print("Primavera")
# --------------------Hemisferio norte
elif hemisferio == "n":
    # Es invierno si, es después del 21/12, en cualquier día de enero o febrero, o antes del 20/3
    if (mes == 12 and dia >= 21) or (mes in (1,2)) or (mes == 3 and dia <= 20):
        print("Invierno")
    # Es primavera si, es después del 21/3, en cualquier día de abril o mayo, o antes del 20/6
    elif (mes == 3 and dia >= 21) or (mes in (4,5)) or (mes == 6 and dia <= 20):
        print("Primavera")
    # Es verano si, es después del 21/6, en cualquier día de julio o agosto, o antes del 20/9
    elif (mes == 6 and dia >= 21) or (mes in (7,8)) or (mes == 9 and dia <= 20):
        print("Verano")
    # Es otoño si, es después del 21/9, en cualquier día de octubre o noviembre, o antes del 20/12
    elif (mes == 9 and dia >= 21) or (mes in (10,11)) or (mes == 12 and dia <= 20):
        print("Otoño")
# En caso de error, si el usuario ingresa un hemisferio diferente a N o S
    else:  
        print("ERROR. Por favor, ingrese únicamente N o S para indicar el hemisferio")