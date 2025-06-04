import os
os.system("cls")

lista_profes = []     #--> vacia, sin elementos!!

# vamos a registrar 3 profes
for k in range(3):
    lista_profes.append(str(input(f'''
    Ingrese nombre profe {k+True}: ''')).strip())
 
print("\n---- registros ------")    
print(lista_profes)
# ordenamos los datos
lista_profes.sort()
print(lista_profes)
print(f'''
    Lista ordenada: {lista_profes}  
    cantidad: {len(lista_profes)}
    2do elemnento: {lista_profes[1]}   ''')