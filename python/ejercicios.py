import os 
import time

# códigos vistos en clases
def AppTrabajadores():

    # ---------------- variables -----------------
    opcion = ""     # Selección menú principal
    cant_max = 0     # int , se solicita al user
    nombre = ""
    edad = 18
    sexo = "F"
    sueldo = 500_000  # --> quinientos mil
    # --- estadísticas ----------
    cant_mujeres = 0
    cant_hombres = 0
    mayor_edad = 0  # mi hipotetico tiene que se bajo
    sueldo_min = 10_000_000   # mi hipotetico es ALTO!!!!


    # ...........Código principal ....................
    while True:
        os.system("cls")
        print('''
        ---------- MENÚ ---------
        1 Ingresar trabajadores 
        2 Ver estadísticas
        3 Salir  ''')

        opcion = str(input("Ingrese opción: "))

        if opcion == "1":
            os.system("cls")
            print("\n --- ingresar registros ---")
            # vamos a pedir la cant. max
            while True:
                try:
                    cant_max = int(input("Ingrese cantidad max: "))
                    if cant_max > 0:
                        break
                    else:
                        print("Error debe ser positivo")
                except ValueError as va:
                    print(f"Error ingrese un N° entero. Error {va}")

            for k in range(cant_max):
                print(f"\n --- registrando {k+1} de {cant_max} ----")
                # nombre
                while True:
                    nombre = str(input("Ingrese nombre:")).strip()
                    if nombre:
                        break
                    else:
                        print("Error, no vacio")

                # Edad
                while True:
                    try:
                        edad = int(input("Ingrese edad: "))
                        if 18 <= edad <= 65:
                            break
                        else:
                            print("Error fuera rango!!!!!")
                    except ValueError as va:
                        print(f"Error ingrese un N° entero. Error {va}")

                # sexo
                while True:
                    sexo = str(input("Ingrese sexo F/M:")).strip().upper()
                    if sexo == "F" or sexo == "M":
                        break
                    else:
                        print("Error, es valido F o M")

                # sueldo
                while True:
                    try:
                        sueldo = int(input("Ingrese sueldo $ "))
                        if sueldo >= 500_000:
                            break
                        else:
                            print("Error debe mayor o igual a $500k")
                    except ValueError as va:
                        print(f"Error ingrese un N° entero. Error {va}")

                print(f'''
                GRABO >> {nombre}  {edad}  {sexo}  ${sueldo}
                    ''')

                # ....calculamos estadísticas ......
                if sexo == "F":
                    cant_mujeres += 1  # ---> abreviación matemática
                else:
                    cant_hombres += 1

                if edad > mayor_edad:
                    mayor_edad = edad

                if sueldo < sueldo_min:
                    sueldo_min = sueldo

            os.system("pause")

        if opcion == "2":
            os.system("cls")
            print("\n --- Estadísticas ---")
            print(f'''
                Cant. mujeres: {cant_mujeres}  
                Cant. hombres : {cant_hombres}  
                Mayor edad: {mayor_edad} años
                Sueldo min ${sueldo_min}
                ''')
            os.system("pause")

        if opcion == "3":
            print("...bye")
        else:
            print("Error, es 1 , 2 o 3")
        os.system("pause")

# practica menu try except / while
def menu_1():
    os.system("cls")
    on_off = 1
    while on_off == 1:    
        os.system("cls")
        menu = int(input('''*La picá del toro*\n
    1. Menu almuerzo
    2. Estadística
    3. Salir
    \nSeleccione una opción: '''))
        try:
            if menu < 4 and menu > 0:
                if menu == 1:
                    os.system("cls")
                    print("No hay amuerzo")
                    continuar = int(input("\nDesea salir? si=1/no=2: "))
                    if continuar == 1:
                        print("Adios")                            
                        on_off = 0
                    elif menu == 2:
                        print("no hay estadisticas.")
                        continuar = int(input("Desea salir? si=1/no=2: "))
                        if continuar == 1:
                            print("Adieu")
                            on_off = 1
                    elif menu == 3:  
                        print("Adieu")
                        on_off = 1
        except ValueError as va:
            print(f"Hubo un error al digitar. {va}")
            os.waitstatus_to_exitcode()
        
# ejercicio: juego de vocales
def contar_vocales(palabra):
    vocales = "aeiou"
    # suma 1 por cada letra de la palabra que contenga una vocal
    contador = sum(1 for letra in palabra if letra in vocales)
    return contador
def juego_vocales():
    y = 1
    while True:
        os.system("cls")
        palabra = str(input("Ingresa una palabra: ")).strip().lower()
        # activamos la funcion contar vocales con la variable "palabra"
        cantidad = contar_vocales(palabra)
        try:
            print(f"La palabra tiene {cantidad} vocal(es).")
            if cantidad <=2:
                print("Perdiste.")
            elif cantidad > 2 and cantidad < 6:
                print("Casi casi ganaste..")
            elif cantidad > 5:
                print("Has ganado, felicidades.\n")
                break
                
        except ValueError as va:
            print(f"Ingresaste mal un digito, {va}")
     
        input("Presiona cualquier tecla para continuar...")
    
# templeate de todo visto hasta clase 15
def template_1():
    
    # ----------- VARIABLES GLOBALES -----------
    opcion = ""
    cant_max = 0

    # TODO: Define tus variables aquí
    # ejemplo: nombre = ""
    # ejemplo: edad = 0
    # ejemplo: categoria = ""

    # ----------- ESTADÍSTICAS INICIALES -----------
    # TODO: Inicializa estadísticas que necesites
    # ejemplo: total_mayores = 0
    # ejemplo: valor_minimo = 999999

    # ----------- BUCLE PRINCIPAL DEL MENÚ -----------
    while True:
        os.system("cls")  # Limpia pantalla
        opcion = input('''
        -------- MENÚ PRINCIPAL --------
        1. Ingresar datos
        2. Ver estadísticas
        3. Salir
        \nSeleccione una opción: ''')

        # ----------- OPCIÓN 1: INGRESO DE DATOS -----------
        if opcion == "1":
            os.system("cls")

            # Reiniciar estadísticas si es necesario
            # TODO: Reinicia variables estadísticas si aplica

            # Validar cantidad de registros
            while True:
                try:
                    cant_max = int(input("Ingrese cantidad de registros: "))
                    while cant_max <= 0:
                        print("Error: debe ser mayor a cero")
                        cant_max = int(input("Ingrese cantidad de registros: "))
                    break
                except ValueError:
                    print("Error: debe ingresar un número válido")

            # Bucle de ingreso de datos
            for i in range(cant_max):
                print(f"\n--- Registro {i + 1} ---")

                # TODO: Agregar capturas de datos con validación
                # Ejemplo: 
                # nombre = input("Ingrese nombre: ").strip()
                # while not nombre:
                #     print("Error: no puede estar vacío")
                #     nombre = input("Ingrese nombre: ").strip()

                # TODO: Validaciones similares para otros campos (int, rango, etc.)

                # TODO: Calcular estadísticas si aplica
                # Ejemplo:
                # if edad > mayor_edad:
                #     mayor_edad = edad

                # Mostrar confirmación de registro
                print(f"Registro {i + 1} guardado correctamente.")

            os.system("pause")

        # ----------- OPCIÓN 2: ESTADÍSTICAS / RESULTADOS -----------
        elif opcion == "2":
            os.system("cls")

            # TODO: Mostrar estadísticas almacenadas
            # Ejemplo:
            # print(f"Mayor edad: {mayor_edad}")
            # print(f"Cantidad total: {total_registros}")

            os.system("pause")

        # ----------- OPCIÓN 3: SALIR -----------
        elif opcion == "3":
            os.system("cls")
            print("Saliendo del programa...")
            time.sleep(1)
            break

        else:
            print("Opción inválida. Intente de nuevo.")
            time.sleep(1)
def template_2():

    # ----------- Variables Globales ----------
    opcion = ""           # Selección del menú principal
    cant_max = 0          # Cantidad máxima de registros

    # Datos del trabajador (modificar según necesidades)
    nombre = ""           # NO PUEDE SER VACÍO
    edad = 0              # RANGO 18 - 65
    sexo = ""             # F / M
    sueldo = 0            # mayor o igual a $500.000

    # ----------- Estadísticas ----------------
    cant_hombres = 0
    cant_mujeres = 0
    mayor_edad = 0
    sueldo_min = 10_000_000  # Valor inicial alto para comparación

    # ----------- Código Principal -----------
    while True:
        os.system("cls")  # Limpia la consola (Windows)
        opcion = str(input('''
        --------- MENÚ ----------
        1.- Ingresar trabajadores
        2.- Ver estadísticas
        3.- Salir      
        \nElija opción:  '''))

        if opcion == "1":
            # Reiniciar estadísticas
            cant_hombres = 0
            cant_mujeres = 0
            mayor_edad = 0
            sueldo_min = 10_000_000

            os.system("cls")
            print("\n--- Ingresar trabajadores ----")

            # Ingresar cantidad de registros
            while True:
                try:
                    cant_max = int(input("Ingrese cantidad de registros: "))
                    while cant_max <= 0:
                        print("Error: debe ser mayor a cero.")
                        cant_max = int(input("Ingrese cantidad de registros: "))
                    break
                except:
                    print("Error: debe ingresar un número entero.")

            # Captura de datos por cada trabajador
            for k in range(cant_max):
                print(f"\n--- Trabajador {k + 1} ----")

                # Nombre
                nombre = input("Ingrese nombre: ").strip()
                while not nombre:
                    print("Error: nombre no puede estar vacío.")
                    nombre = input("Ingrese nombre: ").strip()

                # Edad
                while True:
                    try:
                        edad = int(input("Ingrese edad: "))
                        while not (18 <= edad <= 65):
                            print("Error: edad debe estar entre 18 y 65 años.")
                            edad = int(input("Ingrese edad: "))
                        break
                    except:
                        print("Error: debe ingresar un número entero.")

                # Sexo
                sexo = input("Ingrese sexo (F/M): ").strip().upper()
                while sexo not in ("F", "M"):
                    print("Error: sexo debe ser 'F' o 'M'.")
                    sexo = input("Ingrese sexo (F/M): ").strip().upper()

                # Sueldo
                while True:
                    try:
                        sueldo = int(input("Ingrese sueldo ($): "))
                        while sueldo < 500_000:
                            print("Error: sueldo mínimo es $500.000.")
                            sueldo = int(input("Ingrese sueldo ($): "))
                        break
                    except:
                        print("Error: debe ingresar un número entero.")

                # Mostrar los datos ingresados
                print(f"Registro guardado: {nombre} | {edad} años | {sexo} | ${sueldo}")

                # ----- Cálculo de estadísticas -----
                if edad > mayor_edad:
                    mayor_edad = edad

                if sexo == "F":
                    cant_mujeres += 1
                else:
                    cant_hombres += 1

                if sueldo < sueldo_min:
                    sueldo_min = sueldo

            os.system("pause")

        elif opcion == "2":
            os.system("cls")
            print(f'''
            ----------- Estadísticas -------------
            Mayor edad registrada: {mayor_edad} años
            Cantidad de hombres: {cant_hombres}
            Cantidad de mujeres: {cant_mujeres}
            Sueldo mínimo registrado: ${sueldo_min}
            ''')
            os.system("pause")

        elif opcion == "3":
            os.system("cls")
            print("...cerrando app")
            time.sleep(1)
            break

        else:
            print("Opción no válida. Intente nuevamente.")
            time.sleep(1)  

# clase 18 - tuplas, diccionarios, funciones
def clase18():
    # convierte una lista en tupla
    lista = [1,2,3,4]
    tupla = tuple(lista)
    print(tupla)
    
    # diccionario
    cliente = {"sebastian":18,"contactos":["javier","martin","rodrigo"], "desempleado":False}
    print(cliente)
    
    # conjuntos / set
    # el conjunto no permite datos repetidos
    # y al mismo tiempo los ordena
    conjunto = {3,1,4,1,5,2,4}
    listo = [3,1,4,1,5,2,4]
    print(f'conjunto = {conjunto}\nlista = {listo}')
    

clase18()

# ----- on/off -----
# AppTrabajadores()
# menu_1()
# juego_vocales()