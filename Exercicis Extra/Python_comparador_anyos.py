# codgin: utf -8
anyo_actual=int(input("Indique el año en el que se encuentra:"))
anyo_cualquiera=int(input("Indique un año cualquiera:"))
resultado=abs(anyo_actual-anyo_cualquiera)
if(anyo_actual==anyo_cualquiera):
    print("¡Son el mismo año!")
else:
    if(anyo_actual==2015)and(anyo_cualquiera>2015):
        print("Para llegar al anyo_cualquiera",anyo_actual,"faltan", resultado, "años")
    else:
        if(anyo_actual==2015)and(anyo_cualquiera<2015):
            print("Desde el anyo_cualquiera",anyo_actual,"han pasado", resultado, "años")
