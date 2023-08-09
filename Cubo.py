#Distancia entre dos puntos de un cubo
#Monica Restrepo Leon, C.c. 1000181289
import random
import math
distancias_promedios=[]

y1 = [random.random() for i in range(50)]
z1 = [random.random() for i in range(50)]
x1 = [random.random() for i in range(50)]

x2 = [random.random() for i in range(50)]
y2 = [random.random() for i in range(50)]
z2 = [random.random() for i in range(50)]

distancias = []
for i in range(50):
    Euclidiana = math.sqrt( ((x1[i]-x2[i])**2) + ((y1[i]-y2[i])**2) + ((z1[i]-z2[i])**2))
    distancias.append(Euclidiana)

promedio = sum(distancias)/len(distancias)
print(f"distancia promedio: {promedio}")