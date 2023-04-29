# reto que dejo el profe en la clase 25 
# agarre la idea de un estudiante que puso un "adivinador" de letras
# asi que hice uno de adivinar numeros

import random
# ahora que aprendi a usar el import ramdon mejore un poco el codigo haciendolo mas aleatorio

def run():
    numero_aleatorio=random.randint(1,10)
    numero=int(input("\nDel 1 al 10 en que numero estoy pensando? tienes 5 intentos \n\nEscoge un numero: "))
    intentos = 5
    while intentos > 0:
        if numero == numero_aleatorio:
            print("\nExcelente, adivinaste el numero!! :D")
            break
        elif numero<0 or numero>10:
            numero=int(input("\nEse numero esta fuera del rango permitido, elige otro por favor: "))
        elif numero != numero_aleatorio:
            intentos=intentos-1
            print("\nlo siento, ese no es el numero correcto, te quedan "+str(intentos)+" intentos\n")
            numero=int(input("Escoge otro numero: "))
        elif intentos == 0:
            print("\nLo siento te quedaste sin intentos :(\n") 
        # quiero que cuendo llegue a 0 intentos diga esto pero no supe como conectarlo


if __name__=="__main__":
    run()