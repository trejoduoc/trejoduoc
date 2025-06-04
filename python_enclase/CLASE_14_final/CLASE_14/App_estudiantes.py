import os
import time
# ----------- variables ----------
opcion = ""     # selección del menú principal
cant_max = 0    # cantidad máxima de registros
nombre = ""     # NO PUEDE SER VACIO
edad = 0        # MAYOR A CERO
carrera = ""    # NO PUEDE SER VACIO

# ----- estadísticas ----------------
mayor_edad = 0
cant_estudiantes_analistas = 0

# --------- Código Principal ---------
while True:
    os.system("cls")
    opcion = str(input('''
    --------- MENÚ ----------
    1.- Ingresar estudiantes
    2.- Estadísticas
    3.- Salir      
    \nElija opción:  '''))

    if opcion == "1":
        # vamos a reinicializar variables------------------
        cant_estudiantes_analistas = 0
        mayor_edad = 0

        os.system("cls")
        print("\n--- Ingresar estudiantes ----")
        while True:
            try:
                cant_max = int(input("Ingrese cantidad registros: "))
                while not cant_max > 0:
                    print("Error, mayor a cero")
                    cant_max = int(input("Ingrese cantidad registros: "))
                break  # ---> quiebra el while True
            except:
                print("Error, debe ser un N° entero")

        # --- ahora pedimos los datos a cada estudiante -----
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
                    while not edad > 0:
                        print("Error, mayor a cero!!!")
                        edad = int(input("Ingrese edad:"))
                    break  # --> detiene al while True
                except:
                    print("Error, ingrese N° entero")

            # carrera
            carrera = str(input("Ingrese carrera:")).strip()
            while not carrera:
                print("Error, no vacio")
                carrera = str(input("Ingrese carrera:")).strip()

            # -- visualizamos lo capturado --------
            print(f"GRABO--> {nombre}  {edad}  {carrera}")

            # ----- CALCULAMOS LAS ESTADÍSTICAS -------------
            if edad > mayor_edad:
                mayor_edad = edad

            if carrera.lower() == "analista":
                cant_estudiantes_analistas += 1

        os.system("pause")

    if opcion == "2":
        os.system("cls")
        print(f'''
            ----------- Estadísticas -------------
            Mayor edad: {mayor_edad} años
            Cant. estudiantes analistas: {cant_estudiantes_analistas}  
              ''')
        os.system("pause")

    if opcion == "3":
        os.system("cls")
        print("...cerrando app")
        time.sleep(1)
        break
