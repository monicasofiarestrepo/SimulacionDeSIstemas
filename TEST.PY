
import random
import math

distancias_promedios = []
for a in range(20): #los 20 promedios
  distancias = []
  for i in range(50): #los 50 puntos
    #se generan las coordenadas aleatorias:
    x1 = random.random()
    y1 = random.random()
    z1 = random.random()

    x2 = random.random()
    y2 = random.random()
    z2 = random.random()
    #se calcula la distancia entre ambos puntos
    distancia = math.sqrt( ((x1-x2)**2) + ((y1-y2)**2) + ((z1-z2)**2))
    distancias.append(distancia)

  promedio = sum(distancias)/len(distancias) #para 50 datos se calcula el promedio
  distancias_promedios.append(promedio) #ese promedio se guarda

X_muestral = sum(distancias_promedios)/len(distancias_promedios) #media muestral

#procedimiento para calcular la desviación estandar:
aux = 0
for x in distancias_promedios:
  aux += ((x - X_muestral)**2)
DS_muestral = math.sqrt(aux/(len(distancias_promedios)-1))

#el valor de la de la distribucion T
#para alpha medios es decir 0.025 es aproximadamente 2.093
masomenos = 2.93 * DS_muestral / math.sqrt(len(distancias_promedios))
print(f"{X_muestral} ± {masomenos}")