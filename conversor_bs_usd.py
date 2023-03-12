menu="""
Bienvenido al sistema de conversor de moneda de BS a USD
ingrese de que moneda desea convertir

1 - Bolivares
2 - Dolares

"""

option=int(input(menu))

if option==1:
    bolivares=float(input("Cuantos bolivares tiene? "))
    valor_dolar=24.15
    dolares=round(bolivares/valor_dolar,2)
    dolares=str(dolares)
    print("Tienes $"+dolares+" Dolares")
elif option==2:
    dolares=float(input("Cuantos dolares tiene? "))
    valor_bs=24.15
    bolivares=round(dolares*valor_bs)
    bolivares=str(bolivares)
    print("Tienes "+bolivares+" Bolivares")
else:
    print("ingresa un valor correcto, por favor")
