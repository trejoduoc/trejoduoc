import os
# ---------- variables -----------------
opcion = ""         # Selección del menú principal
lista_nombres = []  # lista de str
lista_edades = []   # lista de int
nombre = ""         # str, NO puede ser cadena vacia
edad = 0            # int, mayor a cero
# ---- estadísticas ----------
cant_usuarios = 0   # cant. total de usuarios
edad_mayor = 0      # valor hipotético

# ------- Código Principal ----------------
while True:
    os.system("cls")
    opcion = str(input('''
    ------- Menú Principal ------
    1. Registrar usuario
    2. Listar usuarios
    3. Estadísticas
    4. Salir
    \n Elija opción: '''))

    if opcion == "1":
        os.system("cls")
        print("\n---- Registrar usuario ----")
        # nombre ---------------------------------------
        while True:
            nombre = str(input("Ingrese nombre:")).strip()
            if nombre:
                break
            else:
                print("Error, no puede ser vacio")

        lista_nombres.append(nombre)

        # edad -------------------------------------------
        while True:
            try:
                edad = int(input("Ingrese edad: "))
                if edad > 0:
                    break
                else:
                    print("Error, debe ser mayor a cero")
            except:
                print("Error, debe ser N° entero")
         
        lista_edades.append(edad)       

        print("\n >>> grabado exitosamente <<<")
        os.system("pause")

    if opcion == "2":
        os.system("cls")
        print("\n --- Listar usuarios ---")
        # len cuenta la cantidad de elementos
        # que posee la lista
        if len(lista_nombres) == 0:
            print("NO hay datos registrados")
        else:
            for k in range(len(lista_nombres)):
                print(f'''
                {lista_nombres[k]}   {lista_edades[k]} años''')
                            
        os.system("pause")

    if opcion == "3":
        os.system("cls")
        print("\n---- Estadísticas -----")
        cant_usuarios = len(lista_nombres)
        
        print(f"Total de usuarios {cant_usuarios}")
        #---- la máxima edad --------------
        print("\n La máxima edad la registra: ")
        edad_mayor = max(lista_edades)
        
        for k in range(len(lista_nombres)):
            if edad_mayor == lista_edades[k]:
                print(f'''
                {lista_nombres[k]}   {lista_edades[k]} años''')
        

        os.system("pause")

    if opcion == "4":
        break
