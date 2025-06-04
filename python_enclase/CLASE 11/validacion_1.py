import os

# Una vez instalado AUTOPEP8 podemos
# ordenar el código presionando:
# alt + shift + f

# Para mover un bloque de código, primero
# seleccionamos el código y luego presionamos
# TAB, con esto se mueve a la derecha y
# shift + TAB para mover a la izquierda

# Para comentar un BLOQUE de código
# primero lo seleccionas y luego debes
# presionar: CONTROL + }
print("\n--- validad una edad positiva ---")
edad = int(input("Ingrese edad: "))
while not edad > 0:
    print("Error, debe ser mayor a cero")
    edad = int(input("Ingrese edad: "))

print("...edad aceptada!!")


print("\n ----- validar un rango ----")
edad_trabajador = int(input("Ingrese edad:"))
while not (18 <= edad_trabajador <= 60):
    print("Error, rango valido 18 a 60")
    edad_trabajador = int(input("Ingrese edad:"))

print("...edad aceptada")
