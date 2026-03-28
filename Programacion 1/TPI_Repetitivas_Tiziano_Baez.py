# ----------- Ejercicio 1 ---------------------------------

# validar nombre
while True:
    nombre = input("Ingrese el nombre del cliente: ")
    if nombre.isalpha() and nombre != "":
        break
    else:
        print("Error. Ingrese solo letras y no deje vacío.")

# validar cantidad de productos
while True:
    cantidad = input("Ingrese la cantidad de productos: ")
    if cantidad.isdigit() and int(cantidad) > 0:
        cantidad = int(cantidad)
        break
    else:
        print("Error. Ingrese un número entero mayor a 0.")

total_sin_descuento = 0
total_con_descuento = 0

# Recorrer productos
for i in range(1, cantidad + 1):
    
    # Validar precio
    while True:
        precio = input(f"Producto {i} - Precio: ")
        if precio.isdigit():
            precio = int(precio)
            break
        else:
            print("Error. Ingrese un número válido.")

    total_sin_descuento += precio

    # Validar descuento
    while True:
        descuento = input("¿Tiene descuento? (S/N): ").lower()
        if descuento == "s" or descuento == "n":
            break
        else:
            print("Error. Ingrese 'S' o 'N'.")

    # Aplicar descuento
    if descuento == "s":
        precio_con_descuento = precio * 0.9
    else:
        precio_con_descuento = precio

    total_con_descuento += precio_con_descuento

# Resultados finales
ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad

print("\n--- RESULTADO ---")
print(f"Cliente: {nombre}")
print(f"Total sin descuentos: ${total_sin_descuento}")
print(f"Total con descuentos: ${total_con_descuento:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")

# ----------- Ejercicio 2 ---------------------------------

# Credenciales fijas
usuario_correcto = "alumno"
clave_correcta = "python123"

intentos = 0
acceso = False

# Login con 3 intentos
while intentos < 3:
    print(f"\nIntento {intentos + 1}/3")
    
    usuario = input("Usuario: ")
    clave = input("Clave: ")

    if usuario == usuario_correcto and clave == clave_correcta:
        print("Acceso autorizado!.")
        acceso = True
        break
    else:
        print("Error: usuario o contraseña incorrectos.")
        intentos += 1

# Si se falla 3 veces en el login se bloquea la cuenta
if not acceso:
    print("Cuenta bloqueada.")

# Menú de opciones
while acceso:
    print("\n1) Estado  2) Cambiar clave  3) Mensaje  4) Salir")
    
    opcion = input("Opción: ")

    # Validación
    if not opcion.isdigit():
        print("Error: ingrese un número válido.")
        continue

    opcion = int(opcion)

    if opcion < 1 or opcion > 4:
        print("Error: esa opción no está.")
        continue

    # Opciones
    if opcion == 1:
        print("Estado: Inscripto")

    elif opcion == 2:
        nueva_clave = input("Escriba la clave nueva: ")
        confirmar = input("Confirmar clave: ")

        if len(nueva_clave) < 6:
            print("Error: la clave debe tener al menos 6 caracteres.")
        elif nueva_clave != confirmar:
            print("Error: las claves no coinciden.")
        else:
            clave_correcta = nueva_clave
            print("Clave cambiada con éxito.")

    elif opcion == 3:
        print("Siempre sé positivo!, que la vida es una!")

    elif opcion == 4:
        print("Saliendo del sistema...")
        break
    
# ----------- Ejercicio 3 ---------------------------------

# Turnos Lunes
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

# Turnos Martes
martes1 = ""
martes2 = ""
martes3 = ""

# Nombre del operador
while True:
    operador = input("Nombre del operador: ")
    if operador.isalpha():
        break
    else:
        print("Error. Solo letras.")

# menú
while True:
    print("\n1) Reservar turno")
    print("2) Cancelar turno")
    print("3) Ver agenda del día")
    print("4) Ver resumen general")
    print("5) Cerrar sistema")

    opcion = input("Opción: ")

    if not opcion.isdigit():
        print("Error. Ingrese un número.")
        continue

    opcion = int(opcion)

    if opcion < 1 or opcion > 5:
        print("Error. Opción inválida.")
        continue

    # RESERVAR---
    if opcion == 1:
        dia = input("Día (1=Lunes, 2=Martes): ")

        if not dia.isdigit():
            print("Error.")
            continue

        dia = int(dia)

        while True:
            nombre = input("Nombre del paciente: ")
            if nombre.isalpha():
                break
            else:
                print("Error. Solo letras.")

        # LUNES
        if dia == 1:
            if nombre == lunes1 or nombre == lunes2 or nombre == lunes3 or nombre == lunes4:
                print("Ese nombre ya tiene turno.")
            elif lunes1 == "":
                lunes1 = nombre
            elif lunes2 == "":
                lunes2 = nombre
            elif lunes3 == "":
                lunes3 = nombre
            elif lunes4 == "":
                lunes4 = nombre
            else:
                print("No hay turnos disponibles.")

        # MARTES
        elif dia == 2:
            if nombre == martes1 or nombre == martes2 or nombre == martes3:
                print("Ese nombre ya tiene turno.")
            elif martes1 == "":
                martes1 = nombre
            elif martes2 == "":
                martes2 = nombre
            elif martes3 == "":
                martes3 = nombre
            else:
                print("No hay turnos disponibles.")

    # CANCELAR---
    elif opcion == 2:
        dia = input("Ingrese 1 o 2 para cancelar segun el día (1 = Lunes, 2 = Martes): ")

        if not dia.isdigit():
            print("Error.")
            continue

        dia = int(dia)

        while True:
            nombre = input("Nombre del paciente: ")
            if nombre.isalpha():
                break
            else:
                print("Error.")

        if dia == 1:
            if lunes1 == nombre:
                lunes1 = ""
            elif lunes2 == nombre:
                lunes2 = ""
            elif lunes3 == nombre:
                lunes3 = ""
            elif lunes4 == nombre:
                lunes4 = ""
            else:
                print("No se encontró el turno.")

        elif dia == 2:
            if martes1 == nombre:
                martes1 = ""
            elif martes2 == nombre:
                martes2 = ""
            elif martes3 == nombre:
                martes3 = ""
            else:
                print("No se encontró el turno.")

    # VER AGENDA---
    elif opcion == 3:
        dia = input("Día (1=Lunes, 2=Martes): ")

        if not dia.isdigit():
            print("Error.")
            continue

        dia = int(dia)

        if dia == 1:
            print("\nLunes:")
            print("Turno 1:", lunes1 if lunes1 != "" else "(libre)")
            print("Turno 2:", lunes2 if lunes2 != "" else "(libre)")
            print("Turno 3:", lunes3 if lunes3 != "" else "(libre)")
            print("Turno 4:", lunes4 if lunes4 != "" else "(libre)")

        elif dia == 2:
            print("\nMartes:")
            print("Turno 1:", martes1 if martes1 != "" else "(libre)")
            print("Turno 2:", martes2 if martes2 != "" else "(libre)")
            print("Turno 3:", martes3 if martes3 != "" else "(libre)")

    # RESUMEN---
    elif opcion == 4:
        ocupados_lunes = 0
        ocupados_martes = 0

        # (uso if de manera corta para no repetir tanto código y usar menos)
        if lunes1 != "": ocupados_lunes += 1
        if lunes2 != "": ocupados_lunes += 1
        if lunes3 != "": ocupados_lunes += 1
        if lunes4 != "": ocupados_lunes += 1

        if martes1 != "": ocupados_martes += 1
        if martes2 != "": ocupados_martes += 1
        if martes3 != "": ocupados_martes += 1

        print("\nResumen:")
        print("Lunes ocupados:", ocupados_lunes, "Disponibles:", 4 - ocupados_lunes)
        print("Martes ocupados:", ocupados_martes, "Disponibles:", 3 - ocupados_martes)

        if ocupados_lunes > ocupados_martes:
            print("Día con más turnos: Lunes")
        elif ocupados_martes > ocupados_lunes:
            print("Día con más turnos: Martes")
        else:
            print("Ambos días tienen la misma cantidad de turnos.")

    # SALIR---------------------
    elif opcion == 5:
        print("Sistema cerrado.")
        break
    
# ----------- Ejercicio 4 ---------------------------------

# Variables iniciales
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

# para la regla anti-spam
racha_forzar = 0 

# Nombre del agente
while True:
    agente = input("Elegí tu nombre de agente: ")
    if agente.isalpha():
        break
    else:
        print("Error. Solo letras >:( .")

# Juego
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:

    # Bloqueo por alarma
    if alarma and tiempo <= 3:
        print("Sistema bloqueado por alarma. PERDISTE.")
        break

    print("\n--- ESTADO ---")
    print("Energía:", energia)
    print("Tiempo:", tiempo)
    print("Cerraduras abiertas:", cerraduras_abiertas)
    print("Alarma:", alarma)
    print("Código parcial:", codigo_parcial)

    print("\n1) Forzar cerradura")
    print("2) Hackear panel")
    print("3) Descansar")

    opcion = input("Opción: ")

    if not opcion.isdigit():
        print("Error. Ingrese un número.")
        continue

    opcion = int(opcion)

    if opcion < 1 or opcion > 3:
        print("Error. Opción inválida.")
        continue

    # -------------------------
    # FORZAR CERRADURA
    # -------------------------
    if opcion == 1:
        energia -= 20
        tiempo -= 2
        racha_forzar += 1

        # Regla anti-spam
        if racha_forzar == 3:
            alarma = True
            print("¡Forzaste demasiado! La cerradura se trabó y activaste la alarma!")
            continue

        # Riesgo de alarma
        if energia < 40:
            while True:
                riesgo = input("Riesgo de alarma (1-3): ")
                if riesgo.isdigit():
                    riesgo = int(riesgo)
                    if 1 <= riesgo <= 3:
                        break
                print("Error.")

            if riesgo == 3:
                alarma = True
                print("¡Se activó la alarma!")

        # Abrir cerradura si no hay alarma
        if not alarma:
            cerraduras_abiertas += 1
            print("Abriste una cerradura.")

    # -------------------------
    # HACKEAR
    # -------------------------
    elif opcion == 2:
        energia -= 10
        tiempo -= 3
        racha_forzar = 0  # corta la racha

        print("Hackeando...")
        for i in range(4):
            print("Progreso:", i + 1)
            codigo_parcial += "A"

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("Código completo. Se abrió una cerradura.")

    # -------------------------
    # DESCANSAR
    # -------------------------
    elif opcion == 3:
        tiempo -= 1
        energia += 15
        racha_forzar = 0

        if energia > 100:
            energia = 100

        if alarma:
            energia -= 10
            print("La alarma consume energía extra.")

        print("Descansaste.")

# -------------------------
# RESULTADO FINAL------------
# -------------------------
if cerraduras_abiertas == 3:
    print("\n¡VICTORIA! Abriste la bóveda.")
elif energia <= 0 or tiempo <= 0:
    print("\nDERROTA. Te quedaste sin recursos.")
    

# ------------------- Ejercicio 5 --------------------------------------

print("--- Escape Room: La Arena del Gladiador ---")

# Nombre del jugador
while True:
    nombre = input("Nombre del Gladiador: ")
    if nombre.isalpha():
        break
    else:
        print("Error: Solo se permiten letras.")

# Variables iniciales/bases
vida_jugador = 100
vida_enemigo = 100
pociones = 3
danio_base = 15
danio_enemigo = 12
turno_jugador = True

print("\n--- INICIA EL COMBATE ---")

# Juego
while vida_jugador > 0 and vida_enemigo > 0:

    print("\n--- NUEVO TURNO ----")
    print(f"{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) / Pociones: {pociones}")

    # TURNO DEL JUGADOR
    if turno_jugador:

        print("\nElegí una acción:")
        print("1) Ataque Pesado")
        print("2) Ráfaga Veloz")
        print("3) Curar")

        opcion = input("Opción: ")

        if not opcion.isdigit():
            print("Error: Ingrese un número válido.")
            continue

        opcion = int(opcion)

        if opcion < 1 or opcion > 3:
            print("Error: opción fuera de rango.")
            continue

        # -------------------------
        # ATAQUE PESADO
        # -------------------------
        if opcion == 1:
            if vida_enemigo < 20:
                danio = danio_base * 1.5
                print("¡Golpe crítico!")
            else:
                danio = danio_base

            vida_enemigo -= danio
            print(f"¡Atacaste al enemigo por {danio} puntos de daño!")

        # -------------------------
        # RÁFAGA VELOZ
        # -------------------------
        elif opcion == 2:
            print(">> ¡Iniciaste una ráfaga de golpes!")
            for i in range(3):
                vida_enemigo -= 5
                print("> Golpe conectado por 5 de daño")

        # -------------------------
        # CURAR
        # -------------------------
        elif opcion == 3:
            if pociones > 0:
                vida_jugador += 30
                pociones -= 1
                print("Te curaste 30 puntos.")
            else:
                print("¡No quedan pociones!")

        # TURNO DEL ENEMIGO (si sigue vivo)
        if vida_enemigo > 0:
            vida_jugador -= danio_enemigo
            print(f"¡El enemigo te atacó por {danio_enemigo} puntos de daño!")

# -------------------------
# FIN DEL JUEGO
# -------------------------
print("\n=== FIN DEL COMBATE ===")

if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre}, ganaste crack!")
else:
    print("DERROTA. Caíste como los mejores...")