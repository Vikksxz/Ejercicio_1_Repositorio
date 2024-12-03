import tkinter as tk

def decimal_a_binario():
    try:
        decimal = int(entrada.get())
        binario = bin(decimal)[2:]
        resultado.config(text=f"Binario: {binario}")
    except ValueError:
        resultado.config(text="Por favor, ingrese un número válido.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora Decimal a Binario")
ventana.geometry("300x250")  # Tamaño de la ventana
ventana.configure(bg="#4CAF50")  # Color de fondo de la ventana

# Crear un campo de entrada para el número decimal
etiqueta = tk.Label(ventana, text="Ingrese un número decimal:", bg="#4CAF50", fg="white")
etiqueta.pack(pady=10)

entrada = tk.Entry(ventana, bg="white", fg="black")
entrada.pack(pady=10)

# Crear un botón para realizar la conversión
boton = tk.Button(ventana, text="Convertir", command=decimal_a_binario, bg="#FF9800", fg="white")
boton.pack(pady=10)

# Crear un área para mostrar el resultado
resultado = tk.Label(ventana, text="", bg="#4CAF50", fg="white")
resultado.pack(pady=20)

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()

