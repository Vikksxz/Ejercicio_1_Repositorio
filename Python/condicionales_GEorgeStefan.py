# 1.	Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

edad = int(input("Introduce tu edad"))

if edad < 18:
    print("Eres menor de edad")
else:
    print("Eres mayor de edad")

# 2.	Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas. Pista: busca cómo funciona lower en python

# Almacenar la contraseña en una variable
contraseña_guardada = "MiContraseña123"

# Preguntar al usuario por la contraseña
contraseña_introducida = input("Introduce la contraseña: ")

# Comparar las contraseñas sin tener en cuenta mayúsculas y minúsculas
if contraseña_guardada.lower() == contraseña_introducida.lower():
    print("La contraseña es correcta.")
else:
    print("La contraseña es incorrecta.")

# 3.	Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

#Establecemos que el programa requiera introducir los numeros al usuario
num = int(input("ingrese el numero"))
divisor = int(input("ingrese el dividendo"))

# Establecemos la condicion de error y de acierto en el bucle para 0 o mas de 0
if divisor == 0:
    print("ERROR, no se puede dividir entre 0")
else:
    resultado = num / divisor 
    print(f"El resultado es: {resultado}")

#4.	Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

#requerimos al usuario que introduzca los numeros
num = int(input("Ingrese el numero"))

#establecemos la condicion del resto

if num % 2 == 0:
    print(f"El numero: {num} es par")
else:
    print(f"El numero: {num} es impar")


#5.	Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

# Preguntar al usuario su edad y sus ingresos mensuales
edad = int(input("Introduce tu edad: "))
ingresos = float(input("Introduce tus ingresos mensuales en €: "))

# Verificar si el usuario debe tributar
if edad > 16 and ingresos >= 1000:
    print("Tienes que tributar.")
else:
    print("No tienes que tributar.")


# 6.	Con el nuevo sistema de evaluación hay que evaluar a los alumnos en: insuficiente, suficiente, bien, notable y sobresaliente. Escribe un programa que pregunte por la nota (0 al 10) e imprima el resultado en el nuevo sistema de evaluación.

# Preguntar al usuario por la nota
nota = float(input("Introduce la nota (0 al 10): "))

# Determinar el resultado en el nuevo sistema de evaluación
if nota < 5:
    resultado = "Insuficiente"
elif nota < 6:
    resultado = "Suficiente"
elif nota < 7:
    resultado = "Bien"
elif nota < 9:
    resultado = "Notable"
else:
    resultado = "Sobresaliente"

# Mostrar el resultado
print(f"El resultado en el nuevo sistema de evaluación es: {resultado}")


# 7.	Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A está formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

# Preguntar al usuario su nombre y sexo
nombre = input("Introduce tu nombre: ")
sexo = input("Introduce tu sexo (M para masculino, F para femenino): ").upper()

# Determinar el grupo correspondiente
if (sexo == 'F' and nombre[0].upper() < 'M') or (sexo == 'M' and nombre[0].upper() > 'N'):
    grupo = 'A'
else:
    grupo = 'B'

# Mostrar el grupo correspondiente
print(f"Tu grupo es: {grupo}")



