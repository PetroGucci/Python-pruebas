def conversor(tipo_pesos,valor_dolar):
    pesos=float(input("Cuantos "+tipo_pesos+" tienes?: "))
    dolares=round(pesos/valor_dolar,2)
    dolares=str(dolares)
    print("Tienes $"+dolares+" dolares")

menu="""
Bienvenido al conversor de monedas 💰
1 - Pesos Colombianos
2 - Pesos Mexicanos 
3 - Pesos Argentinos

"""
opcion=int(input(menu))

if opcion==1:
    conversor("Colombianos",4722.83)

elif opcion==2:
    conversor("Mexicanos ",18.49)

elif opcion==3:
    conversor("Argentinos" ,199.38)

else:
    print("Coloca una opcion correcta por favor")


# dolares=float(input("cuantos dolares tienes? "))
# valor_bolivar=24.15
# dolares=valor_bolivar*dolares
# dolares= round(dolares,2)
# dolares=str(dolares)
# print("Tienes "+dolares+"bs bolivares")