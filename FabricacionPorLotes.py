import random

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
        
def rendimiento():
    pass

def inspeccion():
    randomito = random.random()
    if randomito <= 0.8:
        x = "Pasa Inspección"
    else: 
        x = "No pasa inspección"
    return x

def simulacion():
    #simulación de cantidad de días que nos demoramos para hacer un lote 
    onzas = 0
    dias = 0
    while onzas < 8000:
        dias += dias()
        if inspeccion() == "Pasa inspección":
            onzas += onzas
    return dias