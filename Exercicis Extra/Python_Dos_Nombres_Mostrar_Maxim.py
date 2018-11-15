#coding:utf -8
numero_1=float(input("Indique el numero 1:"))
numero_2=float(input("Indique el numero 2:"))
if(numero_1>numero_2):
    print("És más grande el",numero_1)
else:
    if(numero_2>numero_1):
        print("És más grande el",numero_2)
    else:
        if(numero_1==numero_2):
            print("¡Són iguales!")
