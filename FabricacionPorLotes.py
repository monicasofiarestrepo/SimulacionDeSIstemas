import random
import math
import statistics

def SimulacionDias():
    r = random.random()
    if r <= 0.05:
        dias = 5
    elif r <= 0.15:
        dias = 6
    elif r <= 0.35:
        dias = 7
    elif r <= 0.65:
        dias = 8
    elif r <= 0.85:
        dias = 9
    elif r <= 0.95:
        dias = 10
    else:
        dias = 11
    return dias
        
def rendimiento(a, b, c):
    #distri triangular
    #a,b,c son mínimo, máximo y moda en ese orden
    r = random.random()
    if r <= (c-a)/(b-a):
        return( a + math.sqrt(r * (b-a) * (c-a)) )
    else:
        return ( b - math.sqrt((1-r) * (b-a) * (b - c)))
    
    
def inspeccion():
    randomito = random.random()
    if randomito <= 0.8:
        x = "Pasa Inspección"
    else: 
        x = "No pasa Inspección"
    return x

def simulacion():
    #simulación de cantidad de días que nos demoramos para hacer un lote 
    onzas = 0
    dias = 0
    lotes = 0
    while onzas < 8000:
        lotes += 1
        dias += SimulacionDias()
        if inspeccion() == "Pasa Inspección":
            onzas += rendimiento(600, 1000, 1100)
    return dias, lotes, onzas

observaciones = []
lotes = []
onzas = []
dias = []
for i in range(1000):
    sim_resultados = simulacion()
    dias.append(sim_resultados[0])
    lotes.append(sim_resultados[1])
    onzas.append(sim_resultados[2])

    

promedioDias = sum(dias)/len(dias)
promedioLotes = sum(lotes)/len(lotes)
promedioOnzas = sum(onzas)/len(onzas)

desviacionEstandarDias = statistics.stdev(dias)

print("***************************************************************************************")
print("Primer Punto: \n")
print(f"El valor esperado de los días que se demoran para completar el pedido es: {promedioDias}")
print(f"Esto significa que deben prepararse para completar el pedido {promedioDias} dias antes\n")
print(f"El valor esperado de los lotes que se toma para completar el pedido de 8000 onzas es: {promedioLotes}")
print(f"El valor esperado de las onzas que se producen es : {promedioOnzas}")
print("***************************************************************************************")
print("Segundo Punto: \n")
print(f"Primero calculamos la desviación estandar de los días: {desviacionEstandarDias}\n la precisión D será un porcentaje de 100*(1- alfa). alfa = 0.1, ya que tendremos 1 grado de libertad")
print(f"El numero de simulaciones necesarias para callcularlo sale de la formula n = (Z**2 * D.S.**2)/D**2, Z =  1.96 que sale de la tabla de T-Student en una distribución normal, y la desviación estandar la hemos calculado de sde la lista de días")
n = ((1.96**2 * desviacionEstandarDias**2)/1**2)
print(n)
print("***************************************************************************************")
print("Tercer Punto:\n")
print(f"Con base a la simulación, le recomiendo a Wozac empezar la fabricación del pedido {promedioDias + desviacionEstandarDias} antes de su fecha de eentrega.")
print("esta es la cantidad de días (contando una demora de desviación estándar) con los que la empresa históricamente ha logrado completas pedidos de esta magnitud.")
print("***************************************************************************************")
