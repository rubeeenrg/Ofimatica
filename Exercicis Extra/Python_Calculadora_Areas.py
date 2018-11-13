#coding:utf-8
opcio=input("Quieres calcular el área de T o C:")
if(opcio=="T"):
    base_triangulo=int(input("Indique la base del triangulo:"))
    altura_triangulo=float(input("Indique la altura del triangulo:"))
    calculo=abs(base_triangulo*altura_triangulo/2)
    print("El área del triangulo és de",calculo)
else:
    pi=3.14159265359
    radio_circulo=int(input("Indique el radio del circulo:"))
    calculo_2=abs(2*pi*radio_circulo)
    if(opcio=="C"):
        print("El área del circulo és de",calculo_2) 
