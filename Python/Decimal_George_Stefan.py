def decimal_a_binario(numero):
    # Verifica si el número es 0
    if numero == 0:
        return "0"
    
    # Establecemos una cadena vacía para almacenar el resultado binario
    binario = ""
    
    # Mientras el número sea mayor que 0
    while numero > 0:
        # Obtiene el resto de la división por 2 (0 o 1)
        residuo = numero % 2
        # Añade el resto al inicio de la cadena binaria
        binario = str(residuo) + binario
        # Divide el número por 2 (parte entera)
        numero = numero // 2
    
    return binario

# Pide al usuario que ingrese un número entero
numero_decimal = int(input("Ingrese un número entero en formato decimal: "))

# Convierte el número decimal a binario
numero_binario = decimal_a_binario(numero_decimal)

# Muestra el resultado
print(f"El número {numero_decimal} en binario es: {numero_binario}")
