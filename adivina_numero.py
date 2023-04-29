import random


def run():
	numero_aleatorio=random.randint(1,100)
	numero_elegido=int(input("\nelige un numero del 1 al 100: "))
	while numero_elegido>100 or numero_elegido <=0:
		numero_elegido=int(input("\nEl numero que escogiste es invalido, recuerda que debe ser entre 1 al 100\nElige otro numero: "))
	while numero_elegido != numero_aleatorio:
		if numero_elegido < numero_aleatorio:
			print('\nBusca un numero mas grande\n')
		else:
			print('\nBusca un numero mas pequeño\n')
		numero_elegido=int(input("\nElige un otro numero: "))
	print('\nGanaste!')


if __name__ == '__main__':
	run()