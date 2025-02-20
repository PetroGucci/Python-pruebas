name=input("Mi nombre es ")
rocket=0x1F680
if name.istitle() == True:
    print(f'Mi nombre es {name} {chr(rocket)}')
elif name:
    nametitle=name.title()
    print(f'Mi nombre es {nametitle} \N{rocket}')
else:
    print(f"Debes colocar tu nombre {chr(rocket)}")
