menu="""
Bienvenido al conversor de monedas 💰
1 - Bolivares
2 - Pesos mexicanos 
3 - Pesos colombianos

"""
opcion=int(input(menu))

if opcion==1:
    bolivares=float(input("Cuantos bolivares tienes?: "))
    valor_dolar=24.14
    dolares=round(bolivares/valor_dolar,2)
    dolares=str(dolares)
    print("Tienes $"+dolares+" dolares")

elif opcion==2:
    peso_mex=float(input("Cuantos pesos mexicanos tienes?: "))
    valor_dolar=18.49
    dolares=round(peso_mex/valor_dolar,2)
    dolares=str(dolares)
    print("Tienes $"+dolares+" dolares")

elif opcion==3:
    peso_co=float(input("Cuantos pesos colombianos tienes?: "))
    valor_dolar=4722.83
    dolares=round(peso_co/valor_dolar,2)
    dolares=str(dolares)
    print("Tienes $"+dolares+" dolares")

else:
    print("Coloca una opcion correcta por favor")


# dolares=float(input("cuantos dolares tienes? "))
# valor_bolivar=24.15
# dolares=valor_bolivar*dolares
# dolares= round(dolares,2)
# dolares=str(dolares)
# print("Tienes "+dolares+"bs bolivares")