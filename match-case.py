num1=int(input("Ingresa tu primer numero "))
ope=input("Elige un operador(+ , - , * , / ) ")
num2=int(input("Ingresa tu segundo numero "))

match ope:
    case "+":
        result= num1 + num2
        print(f'{num1}+{num2} = {result}')
    case "-":
        result= num1 - num2
        print(f'{num1} - {num2} = {result}')
    case "*":
        result= num1 * num2
        print(f'{num1} X {num2} = {result}')
    case "/":
        if num2 == 0:
            print("Error: no se puede dividir entre cero.")
        else:
            result= num1 / num2
            print(f'{num1} / {num2} = {result}')
    case _:
        print("Por favor escoge numeros o operadores validos")


