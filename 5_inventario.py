import random

def LeadTime():
  dias = [1,2,3]
  probabilidad = [0.6, 0.9, 1]
  rand = random.random()
  for i in range(len(probabilidad)):
    if rand <= probabilidad[i]:
      return dias[i]+1

def Demanda():
  dia = [0,1,2,3,4]
  probi = [0.1, 0.36, 0.71, 0.91, 1]
  randi = random.random()
  for i in range(len(probi)):
    if randi <= probi[i]:
      return dia[i]


M = 11
Pedido= 8
N = 5
inventario = 3
tiempo= 2
defecit = 0

for i in range(360):
  
  if i %N == 0:
    Pedido = M - inventario + defecit
    lti= LeadTime()
    tiempo = i + LeadTime()
    print("******Punto 1: Simular 360 días********")
    print(f"tiempo en días: {tiempo}")
    print(f"Pedido: {Pedido}  Inventario: {inventario}")
    print("**************")
    
  if i == tiempo:
    demandaDia = Demanda()
    inventario += Pedido
    inventario -= demandaDia
  if inventario < 0:
    defecit += abs(inventario)


#   print(f"Pedido: {Pedido}  Inventario: {inventario} Defecit {defecit}")

