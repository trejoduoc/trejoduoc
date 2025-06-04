# funciones, buenas prácticas

def calcular_descuentos_legales(sueldo_bruto):
    #calcular item pension y salud
    pension = sueldo_bruto * 0.13
    salud = sueldo_bruto * 0.07
    return salud, pension
    #python permite el retorno multiple
    pass

# ---------------------------------------------

def calcular_sueldo_liquido(sueldo_bruto):
        pension, salud = calcular_descuentos_legales(sueldo_bruto)
        liquido = sueldo_bruto - pension - salud
        return liquido
        
# ---------------------------------------------

def imprimir_liquidaciones(rut,nombre,salud,sueldo_bruto,pension,liquido):
    print(f'''*Liquidación Sueldo*
          \nRut: {rut}\nNombre: {nombre}\nSueldo Bruto: ${sueldo_bruto}\nSalud 7%: ${salud:.2f}\nPensión: ${pension}\n\nLquido: ${liquido}''')

# -------------------- Reglas -------------------------
# \n salta un enter \t simula un tab