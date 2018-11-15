#coding:utf -8
cajon_1=("movil")
cajon_2=("bocadillo")
cajon_3=("boli")
cajon_4=("bebida")
cajon_5=()
if((cajon_1=="movil") and (cajon_2=="bocadillo") and (cajon_3=="boli") and (cajon_4=="bebida")):
    cajon_5=cajon_1
    cajon_1=cajon_3
    cajon_3=cajon_5
    cajon_5=cajon_2
    cajon_2=cajon_4
    cajon_4=cajon_5
    print("En el cajón 1 hay un",cajon_3,"en el cajón 2 hay una",cajon_4,"en el cajón 3 hay un",cajon_1,"y""en el cajón 4 hay un",cajon_2)
