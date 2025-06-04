# Un modulo es una librería, es decir, es un
# archivo que contiene funciones.

def sacar_promedio(nota1, nota2, nota3):
    """ Calcula el promedio de las tres 
    notas ingresadas por parámetro

    Args:
        nota1 (float): evaluación 1
        nota2 (float): evaluación 2
        nota3 (float): evaluación 3

    Returns:
        float: promedio pero con 2 decimales
    """
    suma = nota1 + nota2 + nota3
    prom = round(suma/3, 2) # 2 decimales
    return prom


def determinar_estado(prom):
    return "APROBADO" if prom>=4 else "REPROBADO"

def imprimir_ticket(nota1, nota2, nota3, prom, estado):
    print(f'''
        ============ TICKET ===============
        Nota1:{nota1}  Nota2:{nota2}  Nota3:{nota3}          
        Promedio: {prom}     Estado: {estado}
        ===================================  ''')
    
def solicitar_nota(num_nota):
    while True:
        try:
            nota = float(input(f"Ingrese nota{num_nota}:"))
            if 1 <= nota <= 7:
                break
            else:
                print("Error, rango es de 1 a 7")
        except:
            print("Error, debe ser N° float")  
    return nota          






