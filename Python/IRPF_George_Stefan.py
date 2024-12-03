# Desarrolla un programa en python que pida al usuario sus ingresos anuales y le devuelva cuanto tiene que pagar de irpf teniendo en cuenta cada uno de los tramos.
importe = int(input("Especifique sus ingresos: "))

if importe <= 12450:
    irpf = importe * 0.19
    print(f"Tiene que pagar {irpf:.2f}€ de IRPF")
elif 12450 < importe <= 20200:
    irpf = importe * 0.24
    print(f"Tiene que pagar {irpf:.2f}€ de IRPF")
elif 20200 < importe <= 35200:
    irpf = importe * 0.30
    print(f"Tiene que pagar {irpf:.2f}€ de IRPF")
elif 35200 < importe <= 60000:
    irpf = importe * 0.37
    print(f"Tiene que pagar {irpf:.2f}€ de IRPF")
elif 60000 < importe <= 300000:
    irpf = importe * 0.45
    print(f"Tiene que pagar {irpf:.2f}€ de IRPF")
elif importe > 300000:
    irpf = importe * 0.47
    print(f"Tiene que pagar {irpf:.2f}€ de IRPF")

