from random import *
nombre = input("Hola... antes que nada, ¿Podrias ingresar tu nombre primero por favor?:\n")
print("Hola "+nombre+" te doy la bienvenida a ADIVINA MI NUMERO!\n")
print("Te platico... yo estoy pensando en un numero, te reto a adivinar cual es ese numero en el menor numero de intentos posibles")
print("Claro que te ire dando un par de pistas para que pueda ser mas sensillo para ti, solo tienes 8 intentos eh... ¿Empezamos?\n")

num_pensado = randint(1,100)

print("El numero que estoy pensando esta entre el 1 al 100")

# --------------------------------------------------- Inicio del bloque de variables iniciadas
answ_uno = int(input("Dime tu PRIMER numero: "))
answ_dos = 0
answ_trs = 0
answ_ctr = 0
answ_cnc = 0
answ_sis = 0
answ_ste = 0
answ_och = 0
# --------------------------------------------------- Final del bloque de variables iniciadas

# ---------------------------------------------------------------------- Inicio del bloque ANSW UNO
if answ_uno > num_pensado:
    print("Error, dime un numero menor")
    answ_dos = int(input("Dime tu SEGUNDO numero: "))

if answ_uno < num_pensado:
    print("Error, dime un numero mayor")
    answ_dos = int(input("Dime tu SEGUNDO numero: "))

if answ_uno == num_pensado:
    print("G A N A S T E AL PRIMER INTENTO")
# ----------------------------------------------------------------------- Final del bloque ANSW UNO


# ---------------------------------------------------------------------- Inicio del bloque ANSW DOS
if answ_dos > num_pensado:
    print("Error, dime un numero menor")
    answ_trs = int(input("Dime tu TERCER numero: "))

if answ_dos < num_pensado:
    print("Error, dime un numero mayor")
    answ_trs = int(input("Dime tu TERCER numero"))

if answ_dos == num_pensado:
    print("G A N A S T E AL SEGUNDO INTENTO")
# ----------------------------------------------------------------------- Final del bloque ANSW DOS


# ---------------------------------------------------------------------- Inicio del bloque ANSW TRES
if answ_trs > num_pensado:
    print("Error, dime un numero menor")
    answ_ctr = int(input("Dime tu CUARTO numero: "))

if answ_trs < num_pensado:
    print("Error, dime un numero mayor")
    answ_ctr = int(input("Dime tu CUARTO numero: "))

if answ_trs == num_pensado:
    print("G A N A S T E AL TERCER INTENTO")
# ----------------------------------------------------------------------- Final del bloque ANSW TRES


# ---------------------------------------------------------------------- Inicio del bloque ANSW CUATRO
if answ_ctr > num_pensado:
    print("Error, dime un numero menor")
    answ_cnc = int(input("Dime tu QUINTO numero: "))

if answ_ctr < num_pensado:
    print("Error, dime un numero mayor")
    answ_cnc = int(input("Dime tu QUINTO numero: "))

if answ_ctr == num_pensado:
    print("G A N A S T E AL CUARTO INTENTO")
# ----------------------------------------------------------------------- Final del bloque ANSW CUATRO


# ---------------------------------------------------------------------- Inicio del bloque ANSW QUINTO
if answ_cnc > num_pensado:
    print("Error, dime un numero menor")
    answ_sis = int(input("Dime tu SEXTO numero: "))

if answ_cnc < num_pensado:
    print("Error, dime un numero mayor")
    answ_sis = int(input("Dime tu SEXTO numero: "))

if answ_cnc == num_pensado:
    print("G A N A S T E AL QUINTO INTENTO")
# ----------------------------------------------------------------------- Final del bloque ANSW QUINTO


# ---------------------------------------------------------------------- Inicio del bloque ANSW SEXTO
if answ_sis > num_pensado:
    print("Error, dime un numero menor")
    answ_ste = int(input("Dime tu SEPTIMO numero: "))

if answ_sis < num_pensado:
    print("Error, dime un numero mayor")
    answ_ste = int(input("Dime tu SEPTIMO numero: "))

if answ_sis == num_pensado:
    print("G A N A S T E AL SEXTO INTENTO")
# ----------------------------------------------------------------------- Final del bloque ANSW SEXTO


# ---------------------------------------------------------------------- Inicio del bloque ANSW SEPTIMO
if answ_ste > num_pensado:
    print("Error, dime un numero menor")
    print("Es tu ultimo intento eh.")
    answ_och = int(input("Dime tu OCTAVO numero: "))

if answ_ste < num_pensado:
    print("Error, dime un numero mayor")
    print("Es tu ultimo intento eh.")
    answ_och = int(input("Dime tu OCTAVO numero: "))

if answ_ste == num_pensado:
    print("G A N A S T E AL SEPTIMO INTENTO")
# ----------------------------------------------------------------------- Final del bloque ANSW SEPTIMO


# ---------------------------------------------------------------------- Inicio del bloque ANSW OCTAVO
if answ_och > num_pensado:
    print("P E R D I S T E")
    print(f'El numero pensado era: {num_pensado}')

if answ_och < num_pensado:
    print("P E R D I S T E")
    print(f'El numero pensado era: {num_pensado}')

if answ_och == num_pensado:
    print("G A N A S T E AL ULTIMO INTENTO")
# ----------------------------------------------------------------------- Final del bloque ANSW OCTAVO