txt = input("Por favor ingresa un texto (Este puede ser un texto cualquiera: un artículo entero, un párrafo, una frase o un poema)\n")
print("Muchas gracias!\n")
txtUso = txt.lower()
# Convertimos el texto que da el usuario a una lista para poder realizar las funciones necesarias.
txtLista = list(txtUso)
letra1 = input("Elige una primer letra para buscar en el texto:\n").lower()
letra2 = input("Elige una primer letra para buscar en el texto:\n").lower()
letra3 = input("Elige una primer letra para buscar en el texto:\n").lower()
letras = [letra1,letra2,letra3]

txtLetra1  = txtUso.count(letra1)
print("El texto tiene la letra "+ letra1 + " " + str(txtLetra1)+" Veces")
txtLetra2  = txtUso.count(letra2)
print("El texto tiene la letra "+ letra2 + " " + str(txtLetra2)+" Veces")
txtLetra3  = txtUso.count(letra3)
print("El texto tiene la letra "+ letra3 + " " + str(txtLetra3)+" Veces")
# Utilizamos la lista que creamos del str original para crear nuestras variables de trabajo.
listConteo = len(txtLista)
listRever = txtLista[::-1]


# Paso 2 : Mencionamos al usuario el largo de su texto con la funciuon LEN.
print("El tamaño de tu texto es de "+ str(listConteo) +" Caracteres.")


# Paso 3 : Mencionamos cual es el primer caracter de la cadena y cual el ultimo.
print("La letra de inicio de su texto es: " + str(txtLista[0]))
print("La ultima letra de su texto es: " + str(txtLista[-1]))


# Mencionamos al usuario su texto al reves .
print("Su texto al reves es el siguiente: " + str(listRever))

# Mencionamos si la palabra PYTHON esta en el texto.
buscar_python = 'python' in txt
dic = {True:"sí", False:"no"}
print(f"La palabra 'Python' {dic[buscar_python]} se encuentra en el texto")