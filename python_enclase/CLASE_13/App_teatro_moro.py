import os
import time
# ----------- variables ----------
opcion = ""         # selección del menú principal
opcion_dia = ""     # Selección del día de la obra
nombre_dia = ""     # viernes / sábado / domingo
tipo_entrada = ""   # General (G)  Estudiante (E)
precio_entrada = 0
cantidad = 0
con_descuento = "N"     # S/N
opcion_descuento = ""   # selección menú empresa para dscto
nombre_empresa = ""
monto_descuento = 0
subtotal = 0
total = 0
# -------- estadísticas -------------------------------
cant_entradas = 0
total_recaudado = 0

# --------- Código Principal ---------
while True:
    os.system("cls")
    opcion = str(input('''
    --------- MENÚ ----------
    1.- Vender entradas
    2.- Ver estadísticas
    3.- Salir                     
    \nElija opción:  '''))

    if opcion == "1":
        os.system("cls")
        print("\n--- vender entradas teatro -------")
        os.system("pause")

    if opcion == "2":
        os.system("cls")
        print("\n ----- ver estadísticas ----------")
        os.system("pause")

    if opcion == "3":
        os.system("cls")
        print("...cerrando app")
        time.sleep(1)
        break
