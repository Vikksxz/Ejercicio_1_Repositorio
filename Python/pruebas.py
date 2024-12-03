import tkinter as tk
from PIL import Image, ImageTk

# Función para actualizar la imagen en cada frame
def update_image(frame, label, image_path, frames):
    frame_index = frame % len(frames)
    label.config(image=frames[frame_index])
    frame += 1
    root.after(100, update_image, frame, label, image_path, frames)

# Crear la ventana principal
root = tk.Tk()
root.title("Imagen Animada de Fondo")

# Cargar la imagen animada (GIF)
image_path = "animacion.gif"  # Cambia esto por la ruta de tu GIF animado
image = Image.open(C:\Users\georg\OneDrive\1º GS\PROGRAMACION\Archivos\Python\.vscode\rule.png)

# Extraer los frames del GIF
frames = []
try:
    while True:
        frames.append(ImageTk.PhotoImage(image))
        image.seek(len(frames))  # Mover al siguiente frame
except EOFError:
    pass  # Llegamos al final del archivo

# Crear un label para mostrar la imagen
label = tk.Label(root, image=frames[0])
label.pack()

# Iniciar la animación
frame = 0
root.after(0, update_image, frame, label, image_path, frames)

# Iniciar el bucle principal de tkinter
root.mainloop()
