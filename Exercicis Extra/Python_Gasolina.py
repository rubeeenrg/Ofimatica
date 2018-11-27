#coding:utf-8
gasolina=input("Indique que tipo de gasolina quiere:")
super=input("Indique si quiere gasolina normal o turbo:")
sin_plomo=input("Indique si quiere gasolina normal o con aditivios (sabor naranja):")
diesel=input("Indique si quiere gasolina normal o fast&furius:")
if(gasolina=="super") and (super=="normal"):
    print("1.50€")
else:
    if(gasolina=="super") and (super=="turbo"):
        print("1.55€")
    else:
        if(gasolina=="sin_plomo") and (sin_plomo=="normal"):
            print("1.60€")
        else:
             if(gasolina=="sin_plomo") and (sin_plomo=="con aditivios (sabor naranja)"):
                    print("1.65€")
             else:
                  if(gasolina=="diesel") and (diesel=="normal"):
                     print("1.70€")
                  else:
                       if(gasolina=="diesel") and (diesel=="fast&furius"):
                          print("1.75€")
                       else:
litros=float(input("Indique cuantos litros quiere:")
importe=abs(gasolina*litros)
print("Su importe és de", importe)
