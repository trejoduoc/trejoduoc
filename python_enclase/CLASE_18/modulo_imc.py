
def calcular_imc(peso, estatura):
    return peso/estatura**2

def determinar_clasificacion(imc):
    clasificacion = ""
    if imc < 18.5:
        clasificacion = "Bajo Peso"
    elif 18.5 <= imc <= 24.9:
        clasificacion = "Normal"
    elif 25 <= imc <= 29.9:
        clasificacion = "Sobrepeso"
    else:
        clasificacion = "Obesidad"

    return clasificacion

def imprimir_ticket(peso, estatura, imc, clasificacion):
    print(f'''
    =========== Ticket ============      
    Peso:{peso} Kg    Estatura: {estatura} m
    IMC: {imc:.2f}
    Clasificación: {clasificacion} 
    ===============================  ''')    
    
    
def solicitar_dato(nombre_dato):
    while True:
        try:
            dato = float(input(f"Ingrese {nombre_dato}:"))
            if dato >0:
                break
            else:
                print("Error, debe ser mayor a cero!!!")
        except:
            print("Error, debe ser un N° float")
    return dato        