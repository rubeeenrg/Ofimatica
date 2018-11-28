dividendo=int(input("Cual és el dividendo: "))
divisor=int(input("Cual és el divisor: "))
if (divisor==0):
print("Lo siento, no se puede dividir entre 0.")
cociente=dividendo//divisor
residuo=dividendo%divisor
if(residuo==0):
print("La division al parecer es exacta, el cociente es ",cociente,".")
else:
print("La division al parecer no es exacta, el cociente es ",cociente,", y el residuo es ",residuo,".")
