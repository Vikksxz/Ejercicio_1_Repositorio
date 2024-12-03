#El ayuntamiento de Guadalajara acaba de contruir un nuevo parkin público
#y necesita un programa que calcule el importe a pagar por el usuario.
#Entre corruptelas y mariscadas varias se han quedado sin presupuesto para el programador, así que te han encargado a ti esta tarea.
#Escribe un programa en python que tenga como entrada la hora de entrada y la hora de salida, calcule el importe total sabiendo que la hora sale a
# 3.40€ y a partir de la segunda a 1.80€ la hora.

#El formato de hora tiene que estar en "hh:mm:ss" evidentemente hay que tener en cuenta
#los minutos y los segundos
#CONDICIÓN: La diferencia entre la hora de entrada y salida tiene que ser calculada
#con una función.

from datetime import datetime

def calcular_diferencia_horas(hora_entrada, hora_salida):
    formato = "%H:%M:%S"
    entrada = datetime.strptime(hora_entrada, formato)
    salida = datetime.strptime(hora_salida, formato)
    diferencia = salida - entrada
    return diferencia.total_seconds() / 3600

def calcular_importe(hora_entrada, hora_salida):
    diferencia_horas = calcular_diferencia_horas(hora_entrada, hora_salida)
    
    if diferencia_horas <= 1:
        importe = 3.40
    else:
        importe = 3.40 + (diferencia_horas - 1) * 1.80
    
    return importe

hora_entrada = input("Ingrese la hora de entrada (hh:mm:ss): ")
hora_salida = input("Ingrese la hora de salida (hh:mm:ss): ")

importe_total = calcular_importe(hora_entrada, hora_salida)

print(f"El importe total a pagar es: {importe_total:.2f}€")
