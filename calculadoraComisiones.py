nombre = input("Por favor, escribe tu nombre\n")
ventas = input("Por favor, digita el total de ventas que realizaste\n")
calculo = int(ventas)*13/100
comisiones = round(calculo,2)
print("Hola "+nombre+" te queremos recordar que recibiras el 13% de el total de tus ventas en comisiones :D")
print(nombre+" "+"Tu total de ventas es de: "+ventas+" "+"Por lo tanto, tu total de comisiones es de: "+str(comisiones))
