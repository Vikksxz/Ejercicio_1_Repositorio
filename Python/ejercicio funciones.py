# un programa que le demmos dos numeros y que haga el minimo comun multiplo y el maximo comun divisor 
def mcd(a, b):#establecemos la funcion de maximo comun divisor
    while b:
        a, b = b, a % b
    return a

def mcm(a, b):#Establecemos la funcion de minimo comun multiplo
    return abs(a * b) // mcd(a, b)

# Solicitar al usuario que ingrese dos números
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Calcular el MCD y el MCM
maximo_comun_divisor = mcd(num1, num2)
minimo_comun_multiplo = mcm(num1, num2)

# Mostrar los resultados
print(f"El Máximo Común Divisor (MCD) de {num1} y {num2} es: {maximo_comun_divisor}")
print(f"El Mínimo Común Múltiplo (MCM) de {num1} y {num2} es: {minimo_comun_multiplo}")
