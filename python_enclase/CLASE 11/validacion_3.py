import os
os.system("cls")

while True:
    try:
        promedio = float(input("Ingrese promedio:"))
        estado = "APROBADO" if promedio >= 4 else "REPROBADO"
        print(F"PROM:{promedio}   Estado:{estado}")
    except:
        print("Error, formato incorrecto")
