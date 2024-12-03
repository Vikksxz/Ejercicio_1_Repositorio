# 1.	Escribe una función en Python que devuelva el mínimo común múltiplo de dos números.

def mcm(a, b):
    # Función que calcula el mínimo común múltiplo (MCM) de dos números.
    return abs(a * b) // mcd(a, b)

# Ejemplo de uso
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

resultado = mcm(num1, num2)
print(f"El mínimo común múltiplo de {num1} y {num2} es: {resultado}")


# 2.	Escribe una función para calcula el máximo común divisor para dos números dados.

def mcd(a, b):
    #Función que calcula el máximo común divisor (MCD) de dos números utilizando el algoritmo de Euclides.
    while b:
        a, b = b, a % b
    return a


# Ejemplo de uso
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

resultado = mcd(num1, num2)
print(f"El maximo comun divisor de {num1} y {num2} es: {resultado}")

# 3.	Escribe una función que pida los coeficientes de una ecuación de segundo grado y devuelva las dos soluciones posibles. *Para este ejercicio si puedes ayudarte de alguna función externa, como la de la pista*

import math

def resolver_ecuacion_cuadratica(a, b, c):
    #//Función que resuelve una ecuación de segundo grado y devuelve las dos soluciones posibles.//
    disc = b**2 - 4*a*c
    
    if disc < 0:
        return None, None  # No hay soluciones reales
    elif disc == 0:
        x1 = -b / (2*a)
        return x1, x1  # Una única solución
    else:
        x1 = (-b + math.sqrt(disc)) / (2*a)
        x2 = (-b - math.sqrt(disc)) / (2*a)
        return x1, x2  # Dos soluciones distintas

# Pedir los coeficientes de la ecuación
a = float(input("Introduce el coeficiente a: "))
b = float(input("Introduce el coeficiente b: "))
c = float(input("Introduce el coeficiente c: "))

# Resolver la ecuación y mostrar las soluciones
solucion1, solucion2 = resolver_ecuacion_cuadratica(a, b, c)

if solucion1 is None:
    print("La ecuación no tiene soluciones reales.")
elif solucion1 == solucion2:
    print(f"La ecuación tiene una única solución: {solucion1}")
else:
    print(f"Las soluciones de la ecuación son: {solucion1} y {solucion2}")


#Mejora la función para avisar al usuario que los números dados dan una raíz negativa, en el caso de que así sea.

import math

def resolver_ecuacion_cuadratica(a, b, c):
    """ Función que resuelve una ecuación de segundo grado y devuelve las dos soluciones posibles. """
    discriminante = b**2 - 4*a*c
    
    if discriminante < 0:
        print("La ecuación no tiene soluciones reales porque el discriminante es negativo.")
        return None, None  # No hay soluciones reales
    elif discriminante == 0:
        x1 = -b / (2*a)
        return x1, x1  # Una única solución
    else:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        return x1, x2  # Dos soluciones distintas

# Pedir los coeficientes de la ecuación
a = float(input("Introduce el coeficiente a: "))
b = float(input("Introduce el coeficiente b: "))
c = float(input("Introduce el coeficiente c: "))

# Resolver la ecuación y mostrar las soluciones
solucion1, solucion2 = resolver_ecuacion_cuadratica(a, b, c)

if solucion1 is None:
    print("No se pueden calcular soluciones reales.")
elif solucion1 == solucion2:
    print(f"La ecuación tiene una única solución: {solucion1}")
else:
    print(f"Las soluciones de la ecuación son: {solucion1} y {solucion2}")

# **Difícil** Mejórala para que den igual los negativos 

import cmath

def resolver_ecuacion_cuadratica(a, b, c):
    """ Función que resuelve una ecuación de segundo grado y devuelve las dos soluciones posibles, incluyendo soluciones complejas. """
    discriminante = b**2 - 4*a*c
    
    if discriminante < 0:
        # Soluciones complejas
        x1 = (-b + cmath.sqrt(discriminante)) / (2*a)
        x2 = (-b - cmath.sqrt(discriminante)) / (2*a)
    elif discriminante == 0:
        # Una única solución real
        x1 = -b / (2*a)
        x2 = x1
    else:
        # Dos soluciones reales
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
    
    return x1, x2

# Pedir los coeficientes de la ecuación
a = float(input("Introduce el coeficiente a: "))
b = float(input("Introduce el coeficiente b: "))
c = float(input("Introduce el coeficiente c: "))

# Resolver la ecuación y mostrar las soluciones
solucion1, solucion2 = resolver_ecuacion_cuadratica(a, b, c)

if solucion1 == solucion2:
    print(f"La ecuación tiene una única solución: {solucion1}")
else:
    print(f"Las soluciones de la ecuación son: {solucion1} y {solucion2}")


#PARA ESTA MEJORA NO HE ENCONTRADO COMO HACERLO SIN IMPORTAR LA LIBRERIA DE CMATH PARA LOS NUMEROS COMPLEJOS


#4.	Escribir una función que convierta un número decimal en binario y otra que      convierta un número binario en decimal.

def decimal_a_binario(decimal):
    #Función que convierte un número decimal en binario. """
    if decimal == 0:
        return "0"
    binario = ""
    while decimal > 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return binario

def binario_a_decimal(binario):
    #Función que convierte un número binario en decimal. """
    decimal = 0
    longitud = len(binario)
    for i in range(longitud):
        decimal += int(binario[longitud - 1 - i]) * (2 ** i)
    return decimal

# Ejemplo de como se utiliza
numero_decimal = int(input("Introduce un número decimal: "))
binario_convertido = decimal_a_binario(numero_decimal)
print(f"El número decimal {numero_decimal} en binario es: {binario_convertido}")

numero_binario = input("Introduce un número binario: ")
decimal_convertido = binario_a_decimal(numero_binario)
print(f"El número binario {numero_binario} en decimal es: {decimal_convertido}")

#5.	Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y su frecuencia. Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.

# para esto podemos importar la libreria de defaultdict

from collections import defaultdict

def contar_palabras(cadena):
    #Función que recibe una cadena de caracteres y devuelve un diccionario con cada palabra y su frecuencia. """
    palabras = cadena.split()
    frecuencia = defaultdict(int)
    
    for palabra in palabras:
        frecuencia[palabra] += 1
    
    return dict(frecuencia)

def palabra_mas_repetida(diccionario):
    #Función que recibe un diccionario de palabras y su frecuencia, y devuelve una tupla con la palabra más repetida y su frecuencia. """
    if not diccionario:
        return None, 0
    
    palabra_max = max(diccionario, key=diccionario.get)
    frecuencia_max = diccionario[palabra_max]
    
    return palabra_max, frecuencia_max

# Ejemplo de como se usa
cadena = input("Introduce una cadena de caracteres: ")
diccionario_palabras = contar_palabras(cadena)
print("Diccionario de palabras y frecuencias:", diccionario_palabras)

palabra_repetida, frecuencia = palabra_mas_repetida(diccionario_palabras)
print(f"La palabra más repetida es '{palabra_repetida}' con una frecuencia de {frecuencia}.")

#¿Cuántas veces aparece la palabra “que” en el quijote?

def contar_palabra_en_texto(texto, palabra):
    #Función que cuenta cuántas veces aparece una palabra en un texto. """
    # Convertir el texto a minúsculas para hacer la búsqueda insensible a mayúsculas
    texto_minusculas = texto.lower()
    # Dividir el texto en palabras
    palabras = texto_minusculas.split()
    # Contar las ocurrencias de la palabra
    contador = palabras.count(palabra.lower())
    return contador

# Leer el texto del Quijote desde un archivo txt
def leer_texto_desde_archivo(archivo):
    with open(archivo, 'r', encoding='utf-8') as file:
        return file.read()

# Ruta al archivo txt del Quijote
archivo_quijote = 'quijote.txt'  # Asegúrate de que este archivo exista y contenga el texto del Quijote

# Leer el texto del Quijote
quijote_texto = leer_texto_desde_archivo(archivo_quijote)

# Contar la palabra "que"
palabra_a_contar = "que"
contador = contar_palabra_en_texto(quijote_texto, palabra_a_contar)

# Mostrar el resultado
print(f"La palabra '{palabra_a_contar}' aparece {contador} veces en el Quijote.")


#Escribe una función que muestre cuantas veces aparece una palabra dada en un texto.

def contar_palabra_en_texto(texto, palabra):
    #Función que cuenta cuántas veces aparece una palabra en un texto. """
    # Convertir el texto a minúsculas para hacer la búsqueda insensible a mayúsculas
    texto_minusculas = texto.lower()
    # Dividir el texto en palabras
    palabras = texto_minusculas.split()
    # Contar las ocurrencias de la palabra
    contador = palabras.count(palabra.lower())
    return contador

# Leer el texto del Quijote desde un archivo txt
def leer_texto_desde_archivo(archivo):
    with open(archivo, 'r', encoding='utf-8') as file:
        return file.read()

# Ruta al archivo txt del Quijote
archivo_quijote = 'quijote.txt'  # Asegúrate de que este archivo exista y contenga el texto del Quijote

# Leer el texto del Quijote
quijote_texto = leer_texto_desde_archivo(archivo_quijote)

# Contar la palabra "que"
palabra_a_contar = input("Introduce la palabra a contar")
contador = contar_palabra_en_texto(quijote_texto, palabra_a_contar)

# Mostrar el resultado
print(f"La palabra '{palabra_a_contar}' aparece {contador} veces en el Quijote.")