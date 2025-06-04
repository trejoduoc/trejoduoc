import os
import time
# ----------- variables ----------
opcion = ""     # selección del menú principal
cant_max = 0    # cantidad máxima de registros
nombre = ""     # NO PUEDE SER VACIO
edad = 0        # MAYOR A CERO
sexo = ""       # F / M
sueldo = 0      # mayor a $500.000

# ----- estadísticas ----------------
cant_hombres = 0
cant_mujeres = 0
mayor_edad = 0
sueldo_min = 10_000_000   # --> 10 millones

# --------- Código Principal ---------
while True:
    os.system("cls")
    opcion = str(input('''
    --------- MENÚ ----------
    1.- Ingresar trabajadores
    2.- Estadísticas
    3.- Salir      
    \nElija opción:  '''))

    if opcion == "1":
        # vamos a reinicializar variables------------------
        cant_hombres = 0
        cant_mujeres = 0
        mayor_edad = 0

        os.system("cls")
        print("\n--- Ingresar trabajador ----")
        while True:
            try:
                cant_max = int(input("Ingrese cantidad registros: "))
                while not cant_max > 0:
                    print("Error, mayor a cero")
                    cant_max = int(input("Ingrese cantidad registros: "))
                break  # ---> quiebra el while True
            except:
                print("Error, debe ser un N° entero")

        # --- ahora pedimos los datos a cada trabajador -----
        for k in range(cant_max):
            print(f"\n--- Estudiante {k+1} ------")
            # nombre
            nombre = str(input("Ingrese nombre:")).strip()
            while not nombre:
                print("Error, no vacio")
                nombre = str(input("Ingrese nombre:")).strip()

            # edad
            while True:
                try:
                    edad = int(input("Ingrese edad:"))
                    while not (18 <= edad <= 65):
                        print("Error, rango 18 a 65")
                        edad = int(input("Ingrese edad:"))
                    break  # --> detiene al while True
                except:
                    print("Error, ingrese N° entero")

            # sexo
            sexo = str(input("Ingrese sexo F/M:")).strip().upper()
            while not (sexo == "F" or sexo == "M"):
                print("Error, valido F o M")
                sexo = str(input("Ingrese sexo F/M:")).strip().upper()

            # sueldo
            while True:
                try:
                    sueldo = int(input("Ingrese sueldo $"))
                    while not (sueldo >= 500_000):
                        print("Error, min. $500000")
                        sueldo = int(input("Ingrese sueldo $"))
                    break  # --> detiene al while True
                except:
                    print("Error, ingrese N° entero")

            # -- visualizamos lo capturado --------
            print(f"GRABO--> {nombre}  {edad}  {sexo}  {sueldo}")

            # ----- CALCULAMOS LAS ESTADÍSTICAS -------------
            if edad > mayor_edad:
                mayor_edad = edad

            if sexo == "F":
                cant_mujeres += 1
            else:
                cant_hombres += 1

            if sueldo < sueldo_min:
                sueldo_min = sueldo

        os.system("pause")

    if opcion == "2":
        os.system("cls")
        print(f'''
            ----------- Estadísticas -------------
            Mayor edad: {mayor_edad} años
            Cant. hombres: {cant_hombres}  
            Cant. mujeres: {cant_mujeres}  
            Sueldo min. ${sueldo_min}    ''')
        os.system("pause")

    if opcion == "3":
        os.system("cls")
        print("...cerrando app")
        time.sleep(1)
        break
