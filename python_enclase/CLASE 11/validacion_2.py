import os
os.system("cls")

print("\n---- vamos a validar un caracter ---")
en_efectivo = str(input('''
¿Paga en efectivo?  S/N ''')).strip().upper()

while not (en_efectivo == "S" or en_efectivo == "N"):
    print("Error, valido S o N")
    en_efectivo = str(input('''
    ¿Paga en efectivo?  S/N ''')).strip().upper()

print("...registrado!!")
