# codgin: utf -8
loteria=input("Indica si le ha tocado la loteria:")
if(loteria=="si"):
    print("Tienes 3.000€ al mes")
else:
    edad_milloneti=int(input("Indique la edad del/la milloneti:"))
    problemas_de_corazon=input("Indique si el/la milloneti tiene problemas de corazón:")
    casada_la_milloneti=input("Indique si el/la milloneti está casado/a:")
    if(edad>=80)and(problemas_de_corazon=="si")and(milloneti_casada=="no"):
       print("Ganas 3.000€ al mes")
    else:
        estudiar=input("Indique si estudia mucho o poco:")
        nota_M01=int(input("Indique la nota de M01:"))
        nota_M02=int(input("Indique la nota de M02:"))
        nota_M03=int(input("Indique la nota de M03:"))
        nota_M05=int(input("Indique la nota de M05:"))
        if((estudiar=="mucho")and(nota_M01>=9)and(nota_M02>=10)and(nota_M03>=8)and((nota_M05>=6)or(nota_M05<=8))):
            print("Ganas 3.000€ al mes")
        ponderada=((M01*0.30)+(M02*0.40)+(M03*0.25)+(M05*0.05))
        if(ponderada>=8):
            print("Ganas 3.000€ al mes")
