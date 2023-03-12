def conversor(nombre_moneda,valor_dolar):
    tasa=float(input("Cuantos "+nombre_moneda+" tienes? "))
    if option==1:
        dolares=round(tasa/valor_dolar,2)
        dolares=str(dolares)
        print("Tienes $"+dolares+" Dolares")
    elif option==2:
        dolares=round(tasa*valor_dolar,2)
        dolares=str(dolares)
        print("Tienes "+dolares+" Bolivares")

menu="""
Bienvenido al sistema de conversor de moneda de BS a USD
ingrese de que moneda desea convertir

1 - Bolivares
2 - Dolares

"""

option=int(input(menu))

if option==1:
    conversor("Bolivares", 24.15)
elif option==2:
    conversor("Dolares",24.15)
else:
    print("ingresa un valor correcto, por favor")
