# codgin: utf -8
anyo_actual=int(input("Indique el año en el que se encuentra:"))
anyo_cualquiera=int(input("Indique un año cualquiera:"))
if(anyo_actual==2015)and(anyo_cualquiera==2015):
  print("¡2015 y 2015 son el mismo año!")
else:
    if(anyo_actual==2015)and(anyo_cualquiera==2020):
        print("Para llegar al anyo_cualquiera","faltan 5 años")
    else:
        if(anyo_actual==2015)and(anyo_cualquiera==1997):
           print("Desde el anyo_cualquiera","han pasado 17 años")
