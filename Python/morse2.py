# morse_sound.py

import winsound
import time

def reproducir_morse(morse_code):
    # Duración de los tonos en milisegundos
    duracion_punto = 100  # Duración de un punto
    duracion_guion = 300  # Duración de un guion
    duracion_espacio = 200  # Duración del espacio entre puntos y guiones
    duracion_espacio_letra = 400  # Duración del espacio entre letras
    duracion_espacio_palabra = 800  # Duración del espacio entre palabras
    
    # Frecuencia del tono
    frecuencia = 1000  # 1000 Hz
    
    # Reproducir cada símbolo del código Morse
    for symbol in morse_code:
        if symbol == '.':
            winsound.Beep(frecuencia, duracion_punto)
            time.sleep(duracion_espacio / 1000)
        elif symbol == '-':
            winsound.Beep(frecuencia, duracion_guion)
            time.sleep(duracion_espacio / 1000)
        elif symbol == ' ':
            time.sleep(duracion_espacio_letra / 1000)
        elif symbol == '/':
            time.sleep(duracion_espacio_palabra / 1000)

