# juego de piedra papel o tijeras sencillo

import tkinter as tk
import random

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Juego de Piedra, Papel o Tijeras")

# Crear las opciones del juego
opciones = ["piedra", "papel", "tijeras"]

# Crear la función de juego
def juego(opcion):
# Generar una elección aleatoria para la computadora
    computadora = random.choice(opciones)

# Comparar la elección del jugador con la elección de la computadora
    if opcion == computadora:
        resultado.config(text="Empate")
    elif opcion == "piedra"and computadora == "tijeras":
        resultado.config(text="Ganaste")
    elif opcion == "papel"and computadora == "piedra":
        resultado.config(text="Ganaste")
    elif opcion == "tijeras"and computadora == "papel":
        resultado.config(text="Ganaste")
    else:
        resultado.config(text="Perdiste")

# Crear los botones de piedra, papel y tijeras
piedra = tk.Button(ventana, text="Piedra", command=lambda: juego("piedra"))
papel = tk.Button(ventana, text="Papel", command=lambda: juego("papel"))
tijeras = tk.Button(ventana, text="Tijeras", command=lambda: juego("tijeras"))

# Crear el label para mostrar el resultado
resultado = tk.Label(ventana, text="Elige una opción")

# Agregar los widgets a la ventana
piedra.pack()
papel.pack()
tijeras.pack()
resultado.pack()

# Ejecutar la ventana
ventana.mainloop()