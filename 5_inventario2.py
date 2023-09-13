import random

#Funciones para las fuentes de incertidumbre

def leadTime():
  acumulada = [0.6,0.9,1]
  lt = [1,2,3]
  randomLeadTime = random.random()

  for i in range(len(acumulada)):
    if randomLeadTime<=acumulada[i]:
      return lt[i]

def demanda():
  acumulada = [0.1,0.35,0.70,0.91,1]
  demanda = [0,1,2,3,4]
  randomDemanda = random.random()

  for i in range(len(acumulada)):
    if randomDemanda<=acumulada[i]:
      return demanda[i]
    
    
#Funcion simulación para un año

def simulacion(N):
  #Inicializamos valores
  M = 11
  inv = 3
  deficit = 0
  pedido = 8
  ltime = 2
  tiempo = ltime + 1 #Porque comenzamos desde 1
  costo = 0

  #Listas con valores iniciales
  listaInventario = [inv]
  listaDeficit = [deficit]
  listaDemanda = [0]

  for i in range(1,361):
    #Pedidos cada 5 días
    if i % N == 0:
      pedido = M - inv + deficit
      costo += 2000
      ltime = leadTime()
      tiempo = i + ltime

    #Cuando llega el pedido
    if i == tiempo:
      inv += pedido

    #Demanda diaria
    demandaDia = demanda()
    inv -= demandaDia

    #Operaciones del inventario y deficit
    inv -= deficit
    deficit = 0
    if inv < 0:
      deficit += abs(inv)
      inv = 0

    #Sumamos costos de inventario y déficit
    costo += inv*0.4
    costo += deficit*0.6

    #Añadimos valores a las listas
    listaInventario.append(inv)
    listaDeficit.append(deficit)
    listaDemanda.append(demandaDia)

  return listaInventario,listaDemanda,listaDeficit,costo

# import matplotlib.pyplot as plt

# #Probando el programa con la gráfica
# tupla =  simulacion(5)

# lInvertario = tupla[0]
# lDemanda = tupla[1]
# lDeficit = tupla[2]

# print(f"Lista inventa: {lInvertario}")
# print(f"Lista demanda: {lDemanda}")
# print(f"Lista deficit: {lDeficit}\n")

# #Luego de completar la simulación, graficamos el inventario y el déficit en una sola gráfica
# plt.figure(figsize=(12, 6))

# #Graficar inventario
# plt.plot(range(361), lInvertario, label='Inventario', linewidth=2, color='blue')

# #Graficar déficit
# plt.plot(range(361), lDeficit, label='Déficit', linewidth=2, color='red')

# plt.xlabel('Día')
# plt.ylabel('Inventario / Déficit')
# plt.title('Gráfico de Inventario y Déficit')
# plt.grid()
# plt.legend()

# plt.show()


#Costo medio anual de la política actual de reposición

def costoMedioAnual(N):
  suma = 0
  for i in range(1000):
    suma += simulacion(N)[3]
  return suma/1000

print(f"El costo medio anual de la política actual de reposición es ${costoMedioAnual(5)}")


import pandas as pd
#¿Cómo se comportan los costos medios anuales si se aumenta el número de días que se espera para hacer un pedido?
dias = [10,15,20,25,40,45,50,51,52,53,54,55,56,57,60,70,75,80,100,150,200,300,350]
costos = []
for dia in dias:
  costo = costoMedioAnual(dia)
  costos.append(costo)

df = pd.DataFrame({"DIAS": dias, "COSTO MEDIO ANUAL": costos})

texto = """Respecto al comportamiento, los costos comienzan a bajar hasta cierto punto,
para comenzar a subir de nuevo, y así sucesivamente; por ejemplo comienza a bajar hasta un N alrededor de los
52 días y de ahí vuelve a subir, para luego bajar a partir de los 60, etc. De los datos obtenidos se observa
que hacer pedidos cada N=52 generaría menos costos medios anuales\n"""

print(texto)
df