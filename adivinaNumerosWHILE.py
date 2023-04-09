from random import *
# -------------------------------------- Inicio de bloque de variables
turns = 8
tries = 1
sved_num = randint(1,100)
name = input("Cual es tu nombre?\n ")
# -------------------------------------- Fin de bloque de variables

print('Hola '+ name + ' estoy pensando en un numero del 1 al 100, ¿Puedes adivinar cual es?.\n')

# Inicio del ciclo WHILE donde mientras turns sea mayor a 0 podremos ingresar un numero, el cual pasara por cada
# IF, mientras exista un error vamos a restar un turno y sumamos un intento para poder mostrar la cantidad que le tomo.
while turns > 0:
    numero = int(input("Dime un numero: "))
    if numero < 1 or numero > 100:
        print("No hagas trampa!, dije un numero del 1 al 100 solamente...")
        tries += 1
    elif numero < sved_num:
        print("Tu numero es menor al mio, intenta de nuevo")
        tries += 1
    elif numero > sved_num:
        print("Tu numero es mayor al mio, intenta de nuevo")
        tries += 1
    elif numero == sved_num:
        print(f"G A N A S T E y en solo {tries} intentos")
        print(f"Te dire un secreto... mi numero era: {sved_num}")
        break

    turns -= 1
    print(f"Tienes {turns}")