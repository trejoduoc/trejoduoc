import os

os.system("cls")

notas = []     # lista vacia 

while True:
    notas.append(float(input("Ingrese nota:")))
    
    # suma determina la suma de los elementos
    # len determina la cantidad de elementos
    prom = sum(notas)/len(notas)
    print(f'''
        notas: {notas}  
        Promedio: {prom}  ''')