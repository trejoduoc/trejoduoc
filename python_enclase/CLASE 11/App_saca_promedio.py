import os

# -------  variables -----------------
opcion = ""     # Selección del usuario
nota1, nota2, nota3 = 0, 0, 0
promedio = 0
estado = ""     # aprobado / reprobado
# ------- estadísticas -----------
cant_usuarios = 0
cant_aprobados = 0
cant_reprobados = 0
# --------- CÓDIGO PRINCIPAL ----------
while True:
    os.system("cls")
    opcion = str(input('''
    -------- MENÚ ------
    1. Calcular promedio 
    2. Ver estadísticas
    3. Salir
    \n Elija opción: '''))

    if opcion == "1":
        os.system("cls")
        print("-- Calcular Promedio ---")
        nota1 = float(input("Ingrese nota1: "))
        while not (1 <= nota1 <= 7):
            print("Error, debe estar entre 1 y 7")
            nota1 = float(input("Ingrese nota1: "))

        nota2 = float(input("Ingrese nota2: "))
        while not (1 <= nota2 <= 7):
            print("Error, debe estar entre 1 y 7")
            nota2 = float(input("Ingrese nota2: "))

        nota3 = float(input("Ingrese nota3: "))
        while not (1 <= nota3 <= 7):
            print("Error, debe estar entre 1 y 7")
            nota3 = float(input("Ingrese nota3: "))

        promedio = (nota1+nota2+nota3)/3
        estado = "APROBADO" if promedio >= 4 else "REPROBADO"

        os.system("cls")
        print(f'''
            ------------ TICKET ---------------
            Nota1: {nota1}  Nota2: {nota2}  Nota3:{nota3}
            Promedio {promedio}   Estado:{estado}    ''')

        os.system("pause")

    if opcion == "2":
        os.system("cls")
        print("-- Estadísticas ---")
        os.system("pause")

    if opcion == "3":
        break
