import random
from scipy.integrate import quad 

repeticiones = 50000
a = 0
b = 4
c = 5
listaPuntos = []
listaAciertos = []

def evaluarFuncion(x):
    funcion = (x + (x + (x)**(1/2))**(1/2))**(1/2)
    return funcion


def CalcularXi(a, b):
    U = random.uniform(0, 1)
    Xi = a + U * (b - a)
    return Xi

for i in range(repeticiones):
    X = CalcularXi(a, b)
    Y = CalcularXi(0, c)
    listaPuntos.append([X, Y])
    x = listaPuntos[i][0]  
    y = listaPuntos[i][1]  
    listaAciertos.append(evaluarFuncion(x) >= y)

N_H = listaAciertos.count(True)
NXD = len(listaAciertos)

#Estimar el valor de I=∫40(x+(x+(x)1/2)1/2))1/2 con a = 0 y b = 4
#usando el método de acierto/falla y calcular un intervalo de confianza para esta estimación.

IntegAciertoFallo = c * (b - a) * (N_H / NXD)
pEstimado = N_H / NXD

Ireal, error = quad(evaluarFuncion, a, b)

print(f"Valor real de la integral I  = {Ireal}")
print(f"Valor de I con la integral de montecarlo metodo Acierto Fallo = {IntegAciertoFallo}")


#metodo de la media muestral
#Estimar el valor de I=∫40(x+(x+(x)1/2)1/2))1/2 con a = 0 y b = 4


PuntosMetodoMediaMuestral = []

for i in range(repeticiones):
    X = CalcularXi(a, b)
    Y = CalcularXi(0, c)
    PuntosMetodoMediaMuestral.append([X, Y])

GXi = []
for i in range(repeticiones):
    x = listaPuntos[i][0]  
    GXi.append(evaluarFuncion(x))

IntegMediaMuestral = ((b-a)*(1/NXD))*sum(GXi)

print(f"Valor encontrado de I con la integral de montecarlo metodo de media muestral = {IntegMediaMuestral}")

#Comparar ambos valores

DiferenciaIAleatoria = Ireal- IntegAciertoFallo
DiferenciaIMuestral = Ireal - IntegMediaMuestral

Menor = min(DiferenciaIAleatoria, DiferenciaIMuestral)

if Menor == DiferenciaIAleatoria:
  print("En esta prueba es mas cercana por el método de aleatoriedad.")
elif Menor == DiferenciaIMuestral:
  print("En esta prueba es mas cercana por el método de la media muestral.")

