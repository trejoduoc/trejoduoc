import os
import time
# ----------- variables ----------
opcion = ""  # selección del menú principal
cupos_inicial_platea = 50
cupos_inicial_general = 120
precio_platea = 50_000
precio_general = 30_000

cupos_platea = cupos_inicial_platea
cupos_general = cupos_inicial_general
total_recaudado = 0

tipo_entrada = ""    # G:general   P:platea
cant_entradas = 0   # entradas a comprar
total_compra = 0    # valor_entrada X cantidad

# --------- Código Principal ---------
while True:
    os.system("cls")
    opcion = str(input('''
    --------- MENÚ ----------
    1.- Vender entradas
    2.- Reingresar entradas
    3.- Monto recaudado
    4.- Salir                     
    \nElija opción:  '''))

    if opcion == "1":
        os.system("cls")
        print("\n --- Vender entradas ----")
        # tipo entrada -------------------------------------
        while True:
            tipo_entrada = str(input("G: general  P:platea: ")).strip().upper()
            if tipo_entrada in ["G", "P"]:
                break
            else:
                print("Error, valido G o P")

        # cantidad ------------------------------------
        while True:
            try:
                cant_entradas = int(input("Ingrese cantidad:"))
                if cant_entradas > 0:
                    break
                else:
                    print("Error, debe ser mayor a cero")
            except:
                print("Error, debe ser un N° entero")

        # calculamos el total de la compra ----------------
        if tipo_entrada == "G":
            total_compra = precio_general*cant_entradas
        elif tipo_entrada == "P":
            total_compra = precio_platea*cant_entradas

        # ------ imprimir ticket -----------------------
        tipo_entrada = "General" if tipo_entrada == "G" else "Platea"
        print(f'''
            ------------ TICKET COMPRA ------------------
            Tipo entrada: {tipo_entrada}  X {cant_entradas}  
            TOTAL COMPRA ${total_compra}    ''')
        
        # ---- estadísticas ---------------------
        total_recaudado += total_compra
        
        # Actualizamos el stock de entradas
        if tipo_entrada == "General":
            cupos_general -= cant_entradas            
        elif tipo_entrada == "Platea":
            cupos_platea -= cant_entradas    

        os.system("pause")

    if opcion == "2":
        os.system("cls")
        print("\n --- Reingresar entradas ----")
        os.system("pause")

    if opcion == "3":
        os.system("cls")
        print(f'''
              --- Monto Recaudado ----
            TOTAL recaudado ${total_recaudado}  
            Cant. entradas general vendidas:{cupos_inicial_general-cupos_general}
            Cant. entradas platea vendidas:{cupos_inicial_platea-cupos_platea}     ''')
        os.system("pause")

    if opcion == "4":
        os.system("cls")
        print("...cerrando app")
        time.sleep(1)
        break
