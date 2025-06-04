import os
import funciones_notas as fn  # --> alias!!!

# ------------- variables -----------------
opcion = ""     # Selección menú principal
nota1, nota2, nota3, prom = 0, 0, 0, 0
estado = ""

# ---------- funciones locales -------------


def menu_principal():
    return str(input('''
    ---------- Menú Principal ---------
    1. Calcular promedio
    2. Estadísticas
    3. Salir                     
    \n Elija opción:  ''')).strip()


# -------- Código Principal ---------------
while True:
    os.system("cls")
    opcion = menu_principal()

    if opcion == "1":
        os.system("cls")
        print("\n --- Calcular promedio ----")
        nota1 = fn.solicitar_nota(1)
        nota2 = fn.solicitar_nota(2)
        nota3 = fn.solicitar_nota(3)

        prom = fn.sacar_promedio(nota1, nota2, nota3)
        estado = fn.determinar_estado(prom)
        fn.imprimir_ticket(nota1, nota2, nota3, prom, estado)

        os.system("pause")
