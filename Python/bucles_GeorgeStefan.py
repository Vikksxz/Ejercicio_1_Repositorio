# 1)	Escriba un programa que pregunte cuántos números se van a introducir, pida esos números, y muestre un mensaje cada vez que un número no sea mayor que el primero.

# Preguntar cuantos numeros se van a utilizar
cantidad_numeros = int(input("¿Cuántos números vas a introducir? "))

# Pedir el primer número
primer_numero = float(input("Introduce el primer número: "))

# Pedir el resto de los números y verificar si son mayores que el primero
for i in range(1, cantidad_numeros):
    numero = float(input(f"Introduce el número {i+1}: "))
    if numero <= primer_numero:
        print(f"El número {numero} no es mayor que el primer número ({primer_numero}).")

print("Fin del programa.")



# 2)	Escriba un programa que pregunte cuántos números se van a introducir, pida esos números, y escriba el mayor, el menor y la media aritmética. Se recuerda que la media aritmética de un conjunto de valores es la suma de esos valores dividida por la cantidad de valores.

# Preguntar cuántos números se van a introducir
cantidad_numeros = int(input("¿Cuántos números vas a introducir? "))

# Inicializar variables para el mayor, el menor y la suma
mayor = None
menor = None
suma = 0

# Pedir los números y calcular el mayor, el menor y la suma
for i in range(cantidad_numeros):
    numero = float(input(f"Introduce el número {i+1}: "))
    
    if mayor is None or numero > mayor:
        mayor = numero
    
    if menor is None or numero < menor:
        menor = numero
    
    suma += numero

# Calcular la media aritmética
media = suma / cantidad_numeros

# Mostrar los resultados
print(f"El mayor número es: {mayor}")
print(f"El menor número es: {menor}")
print(f"La media aritmética es: {media}")


# 3)	Escriba un programa que pregunte cuantos números se van a introducir, pida esos números (que puedan ser decimales) y calcule su suma.

# Preguntar cuántos números se van a introducir
cantidad_numeros = int(input("¿Cuántos números vas a introducir? "))

# Inicializar la variable para la suma
suma = 0

# Pedir los números y calcular su suma
for i in range(cantidad_numeros):
    numero = float(input(f"Introduce el número {i+1}: "))
    suma += numero

# Mostrar la suma total
print(f"La suma de los números es: {suma}")


#  4)	Escriba un programa que pida dos números enteros y escriba la suma de todos los enteros desde el primer número hasta el segundo. 
#         Mejore el programa anterior haciendo que el programa escriba la suma realizada

# Pedir dos números enteros
inicio = int(input("Introduce el primer número entero: "))
fin = int(input("Introduce el segundo número entero: "))

# Asegurarse de que inicio sea menor o igual que fin
if inicio > fin:
    inicio, fin = fin, inicio

# Inicializar la variable para la suma
suma = 0

# Calcular la suma de todos los enteros desde inicio hasta fin
for numero in range(inicio, fin + 1):
    suma += numero
    print(f"Sumando {numero}, suma actual: {suma}")

# Mostrar la suma total
print(f"La suma de todos los enteros desde {inicio} hasta {fin} es: {suma}")
