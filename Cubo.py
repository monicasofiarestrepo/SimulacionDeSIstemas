
import random
import math
distancias_promedios=[]
distancias = []

for i in range(50):
    
    x1 = random.random()
    y1 = random.random()
    z1 = random.random()

    x2 = random.random()
    y2 = random.random()
    z2 = random.random()

    #distancia entre ambos puntos
    distancia = math.sqrt( ((x1-x2)**2) + ((y1-y2)**2) + ((z1-z2)**2))
    distancias.append(distancia)
    
    for j in range(20):
        promedio = sum(distancias)/len(distancias) 
        distancias_promedios.append(promedio) 

media_muestral = sum(distancias_promedios)/len(distancias_promedios)

#calcular la desviación estandar:
numero_aux = 0
for x in distancias_promedios:
  numero_aux += ((x - media_muestral)**2)
SD_muestral = math.sqrt(numero_aux/(len(distancias_promedios)-1))

#el valor de la de la distribucion T
#para alpha medios (0.025) es aproximadamente 2.093
holgura = 2.093 * SD_muestral / math.sqrt(len(distancias_promedios))
print(f"{media_muestral} ± {holgura}")