def multiplos_de_5(n):
    for i in range(5, n, 5):
        print(i, end=" ")

# Ejemplo de uso
numero = int(input("Ingrese un número: "))
multiplos_de_5(numero)
