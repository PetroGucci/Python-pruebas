year = int(input("Ingresa tu año aqui:"))
f=0x1F976
c=0x1F975

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"\n{year} es un año bisiesto {chr(c)}")
else:
    print(f"\n{year} no es un año bisiesto {chr(f)}")