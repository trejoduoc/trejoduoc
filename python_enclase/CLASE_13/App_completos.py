import os
import time
# ----------- variables ----------
opcion = ""  # selección del usuario menú principal
opcion_completo = ""  # del menú de completos
nombre_completo = ""
precio_completo = 0    # valor por UN completo
cantidad = 0
con_adicionales = "N"   # S/N
opcion_adicional = ""   # del menú de adicionales
nombre_adicional = ""
precio_adicional = 0
total = 0    # TOTAL DE LA COMPRA
# ---- estadísticas ---------------
cant_ventas = 0   # variable contador
total_recaudado = 0  # variable acumulador

# --------- Código Principal ---------
while True:
    os.system("cls")
    opcion = str(input('''
    --------- MENÚ ----------
    1.- Vender completos
    2.- Ver estadísticas
    3.- Salir          
    \nElija opción:  '''))

    if opcion == "1":
        # vamos a reinicilizar variables para que esten
        # "limpias" de valores anteriores
        cantidad = 0
        total = 0
        precio_adicional = 0
        # -------------------------------------------------
        os.system("cls")
        print("\n ----- VENTA COMPLETOS -----")
        opcion_completo = str(input('''
         Tipo Completo        Valor 	
        -------------         ------------	
        1 Completo            $1.200		
        2 Italiano            $1.600		
        3 Dinámico            $1.700	
        \n Elija opción:  '''))

        # La REGLA es una lista de opciones posibles!!
        while not (opcion_completo in ["1", "2", "3"]):
            print("Error, valido 1, 2 o 3")
            opcion_completo = str(input("Elija opción:"))

        if opcion_completo == "1":
            nombre_completo = "Completo"
            precio_completo = 1200
        elif opcion_completo == "2":
            nombre_completo = "Italiano"
            precio_completo = 1600
        elif opcion_completo == "3":
            nombre_completo = "Dinamico"
            precio_completo = 1700

        # ------ preguntamos por cantidad -----------

        cantidad = int(input("Ingrese cantidad:"))
        while not cantidad > 0:
            print("Error, min 1 ")
            cantidad = int(input("Ingrese cantidad:"))

        # ------ preguntamos por adicionales -----------
        con_adicionales = str(input('''
        ¿Quiere adicionales?   S/N ''')).strip().upper()

        while not con_adicionales in ["S", "N"]:
            print("Error, valido S o N")
            con_adicionales = str(input('''
            ¿Quiere adicionales?   S/N ''')).strip().upper()

        if con_adicionales == "S":
            os.system("cls")
            opcion_adicional = str(input('''
                Adicionales	      Precio
            -------------         ---------
            1 papas fritas        $2.000	
            2 bebida 500cc        $1.200
            3 Ambos               $3.200
            \n Elija opción: '''))

            if opcion_adicional == "1":
                nombre_adicional = "Papas fritas"
                precio_adicional = 2000
            elif opcion_adicional == "2":
                nombre_adicional = "Bebida 500cc"
                precio_adicional = 1200
            elif opcion_adicional == "3":
                nombre_adicional = "Papas fritas+ bebida"
                precio_adicional = 3200

        # ---------- calcular total ------------------
        total = cantidad*precio_completo+precio_adicional

        # ---- limpiar pantalla y ticket --------------------
        os.system("cls")
        print(f'''
            ----------- TICKET ---------------
            Completo: {nombre_completo} a ${precio_completo} c/u
            Cantidad: {cantidad} 
            Subtotal ${precio_completo*cantidad}''')
        if (con_adicionales == "S"):
            print(f'''
                Adicional: {nombre_adicional} 
                Precio Adicional ${precio_adicional} ''')
        print(f"TOTAL PAGAR ${total}")

        # ------ CALCULAMOS LAS ESTADÍSTICAS -------------
        # Como estamos estamos cerrando una venta
        # el contador de ventas se incrementa en 1 unidad
        cant_ventas += 1  # ---> ABREVIACIÓN MATEMÁTICA

        # el total de venta se suma al acumulado
        total_recaudado += total

        os.system("pause")

    if opcion == "2":
        os.system("cls")
        print(f'''
            ---------- ESTADÍSTICAS ------------
            Cant. ventas: {cant_ventas}  
            Total recaudado ${total_recaudado} ''')
        os.system("pause")

    if opcion == "3":
        os.system("cls")
        print("...cerrando app")
        time.sleep(1)
        break
