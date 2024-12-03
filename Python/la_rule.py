import tkinter as tk
import random
import os

color_fondo = "#c3e48e"
contador_negro = 0
contador_rojo = 0
contador_verde = 0
apuesta_actual = None
cantidad_apuesta = 0
ganancia_neta = 0
saldo_perdido = 0

def determinar_color(numero):
    if numero == 0:
        return "verde"
    elif numero % 2 == 0:
        return "negro"
    else:
        return "rojo"

def tirada():
    global apuesta_actual, cantidad_apuesta, ganancia_neta, saldo_perdido
    numero = random.randint(0, 36)
    color = determinar_color(numero)
    resultado_label.configure(text=f'Número: {numero} ({color})')
   
    if apuesta_actual == color:
        ganancia_neta += cantidad_apuesta
        ganador_label.configure(text=f"¡Ganaste! +{cantidad_apuesta}", fg="green")
        cambiar_fondo("fuegos_artificiales.png")  # Cambiar fondo a fuegos artificiales
    else:
        saldo_perdido += cantidad_apuesta
        ganador_label.configure(text=f"Perdiste -{cantidad_apuesta}", fg="red")
        cambiar_fondo("fondo_normal.png")  # Volver al fondo normal
   
    actualizar_contadores(color)
    actualizar_etiquetas()

def actualizar_contadores(color):
    global contador_negro, contador_rojo, contador_verde
    if color == "negro":
        contador_negro += 1
    elif color == "rojo":
        contador_rojo += 1
    elif color == "verde":
        contador_verde += 1

def actualizar_etiquetas():
    suma_negro.configure(text=f"Negro: {contador_negro}")
    suma_rojo.configure(text=f"Rojo: {contador_rojo}")
    suma_verde.configure(text=f"Verde: {contador_verde}")
    ganancia_label.configure(text=f"Ganancia Neta: {ganancia_neta}")
    perdida_label.configure(text=f"Saldo Perdido: {saldo_perdido}")

def apostar_negro():
    global apuesta_actual, cantidad_apuesta
    apuesta_actual = "negro"
    cantidad_apuesta = int(apuesta_de_entrada.get())
    apuesta_label.configure(text=f"Apuesta actual: Negro ({cantidad_apuesta})")

def apostar_rojo():
    global apuesta_actual, cantidad_apuesta
    apuesta_actual = "rojo"
    cantidad_apuesta = int(apuesta_de_entrada.get())
    apuesta_label.configure(text=f"Apuesta actual: Rojo ({cantidad_apuesta})")

def apostar_verde():
    global apuesta_actual, cantidad_apuesta
    apuesta_actual = "verde"
    cantidad_apuesta = int(apuesta_de_entrada.get())
    apuesta_label.configure(text=f"Apuesta actual: Verde ({cantidad_apuesta})")

def cambiar_fondo(imagen):
    if imagen in fondo_imagenes:
        fondo_label.configure(image=fondo_imagenes[imagen])
        fondo_label.image = fondo_imagenes[imagen]
    else:
        print(f"Imagen {imagen} no encontrada.")

# Ventana principal
ventana = tk.Tk()
ventana.title("Ruleta")
ventana.configure(bg=color_fondo)

# Cargar imágenes de fondo
fondo_imagenes = {}
for imagen in ["fondo_normal.png", "fuegos_artificiales.png"]:
    if os.path.exists(imagen):
        fondo_imagenes[imagen] = tk.PhotoImage(file=imagen)
    else:
        print(f"Imagen {imagen} no encontrada.")

# Etiqueta para el fondo
fondo_label = tk.Label(ventana, image=fondo_imagenes.get("fondo_normal.png", ""))
fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(ventana, text="Número: ", font=("arial", 50, "bold"), bg=color_fondo)
resultado_label.pack(pady=20, expand=True, fill=tk.BOTH)

# Etiqueta para mostrar si ganaste o perdiste
ganador_label = tk.Label(ventana, text="", font=("arial", 60, "bold"), bg=color_fondo)
ganador_label.pack(pady=20, expand=True, fill=tk.BOTH)

# Etiqueta para mostrar la apuesta actual
apuesta_label = tk.Label(ventana, text="Apuesta actual: Ninguna", font=("arial", 18, "bold"), bg=color_fondo)
apuesta_label.pack(pady=10, expand=True, fill=tk.BOTH)

# Entrada de texto para la cantidad de la apuesta
apuesta_de_entrada = tk.Entry(ventana, font=("arial", 20))
apuesta_de_entrada.pack(pady=10, expand=True, fill=tk.BOTH)
apuesta_de_entrada.insert(0, "Introduce la cantidad")

# Botón para girar la ruleta
girar_boton = tk.Button(ventana, text="Girar Ruleta", font=("arial", 24, "bold"), command=tirada)
girar_boton.pack(pady=10, expand=True, fill=tk.BOTH)

# Frame para los botones de apuestas
frame_apuestas = tk.Frame(ventana, bg=color_fondo)
frame_apuestas.pack(side=tk.BOTTOM, pady=10, expand=True, fill=tk.BOTH)

# Botones de apuestas
boton_negro = tk.Button(frame_apuestas, text="Apostar Negro", font=("arial", 18, "bold"), background="#414141", command=apostar_negro, activebackground="lightgrey")
boton_negro.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.BOTH)

boton_verde = tk.Button(frame_apuestas, text="Apostar Verde", font=("arial", 18, "bold"), background="green", command=apostar_verde, activebackground="lightgrey")
boton_verde.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.BOTH)

boton_rojo = tk.Button(frame_apuestas, text="Apostar Rojo", font=("arial", 18, "bold"), background="red", command=apostar_rojo, activebackground="lightgrey")
boton_rojo.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.BOTH)

# Etiquetas para mostrar los contadores de colores
suma_negro = tk.Label(ventana, text="Negro: 0", font=("arial", 18, "bold"), bg=color_fondo)
suma_negro.pack(pady=5, expand=True, fill=tk.BOTH)

suma_rojo = tk.Label(ventana, text="Rojo: 0", font=("arial", 18, "bold"), bg=color_fondo)
suma_rojo.pack(pady=5, expand=True, fill=tk.BOTH)

suma_verde = tk.Label(ventana, text="Verde: 0", font=("arial", 18, "bold"), bg=color_fondo)
suma_verde.pack(pady=5, expand=True, fill=tk.BOTH)

# Etiquetas para mostrar la ganancia neta y el saldo perdido
ganancia_label = tk.Label(ventana, text="Ganancia Neta: 0", font=("arial", 18, "bold"), bg=color_fondo)
ganancia_label.pack(pady=5, expand=True, fill=tk.BOTH)

perdida_label = tk.Label(ventana, text="Saldo Perdido: 0", font=("arial", 18, "bold"), bg=color_fondo)
perdida_label.pack(pady=5, expand=True, fill=tk.BOTH)

# Iniciar el bucle principal de la ventana
ventana.mainloop()
