import funciones_empleados as fn
import os

# buenas prácticas
# ----------------- variables -----------------
opcion = ""
lista_ruts = []
lista_nombres = []
lista_sueldos_bruto = []
lista_sueldos_liquidos = []
rut, nombre = "", ""
sueldo_bruto, sueldo_liquido = 0,0

# ----------------- funciones locales -----------------
# funciones locales, todo lo que tenga que ver con el menu
# saludos, despedidas, detalles.
def menu_principal():
    return str(input('''*MENU*\n\n1. Cargar datos\n2. Ver estadísticas\n3. Salir\n\nIngrese una opcion (1-3): ''')).strip()

# ----------------- código principal -----------------
# ciclos
while 1:
    os.system("cls")
    opcion = menu_principal()
    if opcion == "1":
        os.system("cls")
        print("--- Cargar datos y ver liquidacion ---")
        # ingreso rut
        rut = str(input("Ingrese rut: ")).strip().upper()
        lista_ruts.append(rut)
        
        # ingreso nombre
        nombre = str(input("Ingrese nombre: ")).strip()
        lista_nombres.append(nombre)
        
        # ingreso sueldo bruto
        sueldo_bruto = int(input("Ingrese sueldo bruto: $"))
        lista_sueldos_bruto.append(sueldo_bruto)
        
        # empezamos a usar funciones del modulo
        pension, salud = fn.calcular_descuentos_legales(sueldo_bruto)
        sueldo_liquido = fn.calcular_sueldo_liquido(sueldo_bruto)
        
        # cargar lista de sueldo liquido
        lista_sueldos_liquidos.append(sueldo_liquido)
        
        # pasamos a imprimir la liquidacion de sueldo
        fn.imprimir_liquidaciones(rut,nombre,salud,sueldo_bruto,pension,sueldo_liquido)
        
        os.system("pause")
    if opcion == "2":
        os.system("cls")
        
        os.system("pause")
    if opcion == "3":
        break