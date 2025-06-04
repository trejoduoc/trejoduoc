# Una colección es un grupo de datos
# Entre las colecciones estan las listas

# Todo nombre de lista debe ser plural

import os

os.system("cls")

print("\n----- ejemplo 1 ------")
#  index--->     0         1         2
verduras = ["zanahoria", "tomate", "palta"]

print(verduras)  # imprimimos como un "todo" la lista

# vamos a hacer referencia a una posición(index)
print(f'''
    1er elemento es {verduras[0]}  
      
    3er elemento es {verduras[2]}  
      ''')

# vamos a imprimir cada elemento de la lista
# para esto LO IDEAL es recorrer los datos
# con un ciclo for
for k in verduras:
    print(k)

# ------- funciones de las listas ------
print("\n----- ejemplo 2 ------")
print('''\n
    Vamos a agregar un elemento a la lista 
    usaremos la función append   ''')
verduras.append("papas")
print("\n----  uso de append ----")
print(verduras)


print('''\n
    Vamos a insertar un elemento a la lista 
    usaremos la función insert, OJO se indica
    la posición. Los datos se desplazan''')
verduras.insert(1, "lechuga")
print("\n----  uso de insert ----")
print(verduras)


print('''\n
    Vamos a eliminar un elemento a la lista 
    usaremos la función pop, OJO se indica
    la posición. Los datos se desplazan''')
verduras.pop(3)
print("\n----  uso de pop ----")
print(verduras)
verduras.pop()
print("\n----  uso de pop sin indice ----")
print(verduras)
