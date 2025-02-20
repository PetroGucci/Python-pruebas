def identificar_personaje():
    puede_volar = input("¿Tu personaje puede volar? (Si/No): ").strip().lower()
    
    if puede_volar == "si":
        es_humano = input("¿Tu personaje es humano? (Si/No): ").strip().lower()
        
        if es_humano == "si":
            usa_mascara = input("¿Tu personaje usa máscara? (Si/No): ").strip().lower()
            if usa_mascara == "si":
                print("Tu personaje es Iron Man.")
            else:
                print("Tu personaje es Capitana Marvel.")
        
        elif es_humano == "no":
            usa_mascara = input("¿Tu personaje usa máscara? (Si/No): ").strip().lower()
            if usa_mascara == "si":
                print("Tu personaje es Ronan Accuser.")
            else:
                print("Tu personaje es Vision.")

        else:
            print("Respuesta no válida. Usa 'Si' o 'No'.")
    
    elif puede_volar == "no":
        es_humano = input("¿Tu personaje es humano? (Si/No): ").strip().lower()
        
        if es_humano == "si":
            usa_mascara = input("¿Tu personaje usa máscara? (Si/No): ").strip().lower()
            if usa_mascara == "si":
                print("Tu personaje es Spiderman.")
            else:
                print("Tu personaje es Hulk.")

        elif es_humano == "no":
            usa_mascara = input("¿Tu personaje usa máscara? (Si/No): ").strip().lower()
            if usa_mascara == "si":
                print("Tu personaje es Black Bolt.")
            else:
                print("Tu personaje es Thanos.")

        else:
            print("Respuesta no válida. Usa 'Si' o 'No'.")
    
    else:
        print("Respuesta no válida. Usa 'Si' o 'No'.")

identificar_personaje()