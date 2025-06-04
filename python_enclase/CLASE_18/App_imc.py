import os
import modulo_imc as mi  # --> alias!!!!

# -------- variables ----------------------------------
opcion = ""     # Selección del menú
peso, estatura, imc = 0, 0, 0
clasificacion = ""

# ----------- funciones locales -----------------------
def menu_principal():
    return str(input('''
    ---------- Menú Principal ---------
    1. Calcular IMC
    2. Estadísticas
    3. Salir                     
    \n Elija opción:  ''')).strip()

# ---------- Código Principal --------------------------
while True:
    os.system("cls")
    opcion = menu_principal()
    
    if opcion == "1":
        os.system("cls")
        print("\n ----- Calcular IMC ------")
        peso = mi.solicitar_dato("peso")
        estatura = mi.solicitar_dato("estatura")
        
        imc = mi.calcular_imc(peso, estatura)
        clasificacion = mi.determinar_clasificacion(imc)
        mi.imprimir_ticket(peso, estatura, imc, clasificacion)
        
        os.system("pause")
        
    if opcion == "2":
        os.system("cls")
        print("...en construcción")        
        os.system("pause")    
        
    if opcion == "3":
        break    
