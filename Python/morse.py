# morse_translator.py

def traducir_a_morse(texto):
    # Diccionario con las traducciones de letras y números a Morse
    morse_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
        '8': '---..', '9': '----.', ' ': '/'
    }
    
    # Convertir el texto a mayúsculas para coincidir con las claves del diccionario
    texto = texto.upper()
    
    # Traducir cada carácter del texto a Morse
    traduccion = ' '.join(morse_dict[char] for char in texto if char in morse_dict)
    
    return traduccion






  