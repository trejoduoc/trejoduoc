import os
import time
# ----------- variables -------------------
opcion = ""    # selección del usuario
nombre = ""    # str, nombre del user
edad = 0       # int
sexo = ""      # femenino / masculino
peso = 0       # int, en Kg
estatura = 0   # float, en Metros
imc = 0
clasificacion = 0

# ---- ESTADÍSTICAS --------
cant_mujeres = 0
cant_hombres = 0
suma_edad_mujeres = 0
suma_edad_hombres = 0
prom_edad_mujeres = 0
prom_edad_hombres = 0

# --------- Código Principal ------------
while True:
    os.system("cls")
    opcion = str(input('''
    --------- MENÚ ----------
    1.- Calcular IMC
    2.- Ver estadísricas
    3.- Salir              
    \nElija opción:  '''))

    if opcion == "1":
        os.system("cls")
        print("\n----- CALCULAR IMC -----")
        nombre = str(input("Ingrese nombre: ")).strip()
        # validamos que se cargue dato en la variable str
        while not nombre:
            print("Error, no puede ser vacio")
            nombre = str(input("Ingrese nombre: ")).strip()

        edad = int(input("Ingrese edad:"))
        while not edad > 0:
            print("Error, min 1")
            edad = int(input("Ingrese edad:"))

        sexo = str(input('''
        Ingrese sexo femenino/masculino:''')).strip().lower()
        while not (sexo == "femenino" or sexo == "masculino"):
            print("Error, valido masculino/femenino")
            sexo = str(input('''
            Ingrese sexo femenino/masculino:''')).strip().lower()

        peso = int(input("Ingrese peso Kg"))
        while not peso > 0:
            print("Error, mayor a cero")
            peso = int(input("Ingrese peso Kg"))

        estatura = float(input("Ingrese estatura: "))
        while not estatura > 0:
            print("Error, mayor a cero")
            estatura = float(input("Ingrese estatura: "))

        # --- calculamos y clasificamos el IMC ----------
        # round PARA REDONDEAR!!!!
        imc = round(peso/estatura**2, 2)  # --> 2 decimales

        if imc < 18.5:
            clasificacion = "Bajo Peso"
        elif 18.5 <= imc <= 24.9:
            clasificacion = "Normal"
        elif 25 <= imc <= 29.9:
            clasificacion = "Sobrepeso"
        elif imc >= 30:
            clasificacion = "Obesidad"
            
        # ----- limpiar pantalla y ticket -----------------
        os.system("cls")
        print(f'''
            ---------- ticket -----------
            Nombre: {nombre}   Edad:{edad} años
            Sexo:{sexo}
            Peso: {peso} Kg.
            Estatura: {estatura} m
            IMC: {imc}      Clasificación:{clasificacion}''')
        
        #---- determinar estadísticas --------------------
        if sexo == "femenino":
            # cant_mujeres = cant_mujeres + 1 
            cant_mujeres += 1
            suma_edad_mujeres += edad
            prom_edad_mujeres = suma_edad_mujeres/cant_mujeres
        else:
            cant_hombres +=1            
            suma_edad_hombres += edad
            prom_edad_hombres = suma_edad_hombres/cant_hombres

        os.system("pause")

    if opcion == "2":
        os.system("cls")        
        print(f'''
        ---------- ESTADÍSTICAS ----------
        Cant. mujeres: {cant_mujeres}
        Cant. hombres: {cant_hombres}
        Prom. edad mujeres: {prom_edad_mujeres} años      
        Prom. edad hombres: {prom_edad_hombres} años
              ''')
        os.system("pause")

    if opcion == "3":
        os.system("cls")
        resp = str(input('''
        ¿Estas seguro de salir? S/N  ''')).strip().upper()
        if resp == "S":
            print("...cerrando app")
            time.sleep(1)
            break
