# El equipo Aston Martin de F1 te acaba de fichar para que ayudes con la estrategía de la próxima carrera.
#El tiempo medio por vuelta es de 1 min y 30 segundos por cada vuelta que demos
#desgastamos un 1.15% la vida de los neumáticos y el tiempo por vuelta aumenta en 2 decimas por cada vuelta.
#Cuando hacemos una parada volvemos a tener las ruedas al 100% y a dar la vuelta
#en 1'30''. Escribe una función que devuelva cuanto tiempo tardará el piloto en dar n vueltas
#parando cuando los neumáticos lleguen a un porcentaje x de desgaste.
#siendo las vueltas y el porcentaje de desgaste parámetros iniciales de la función

def tiempo_total_vueltas(n, x):
    tiempo_inicial = 90 
    desgaste_por_vuelta = 1.15
    aumento_tiempo_por_vuelta = 0.2
    tiempo_total = 0
    neumaticos_actuales = 100
    tiempo_vuelta_actual = tiempo_inicial

    for vuelta in range(1, n + 1):
        tiempo_total += tiempo_vuelta_actual
        neumaticos_actuales -= desgaste_por_vuelta
        if neumaticos_actuales <= x:
            neumaticos_actuales = 100
            tiempo_vuelta_actual = tiempo_inicial
        else:
            tiempo_vuelta_actual += aumento_tiempo_por_vuelta
    return tiempo_total

n = 50 
x = int(input('Introduce el desgaste de los neumaticos'))
tiempo_total = tiempo_total_vueltas(n, x)
print(f"El tiempo total para dar {n} vueltas con una parada cuando los neumáticos lleguen al {x}% de desgaste es: {tiempo_total} segundos")
