# main.py

from morse import traducir_a_morse
from morse2 import *

# Ejemplo de uso
texto = input("Introduce el texto a traducir")
print(f"Texto original: {texto}")
print("Reproduciendo traducción a Morse...")

# Traducir el texto a Morse
morse_code = traducir_a_morse(texto)
#Mostrar el texto en morse tambien
morse_code = traducir_a_morse(texto)
print(f"Traduccion a morse: {morse_code}")

# Reproducir el código Morse
reproducir_morse(morse_code)
 