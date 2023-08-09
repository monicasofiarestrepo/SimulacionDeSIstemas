import random
import math
import numpy as np
from scipy.stats import t

def calcular_distancia(punto1, punto2):
    return math.sqrt(sum((x1 - x2)**2 for x1, x2 in zip(punto1, punto2)))

def generar_puntos(n):
    puntos = []
    for _ in range(n):
        punto = [random.uniform(0, 1) for _ in range(3)]  # Coordenadas aleatorias entre 0 y 1
        puntos.append(punto)
    return puntos

def main():
    num_ejecuciones = 20
    resultados = []

    for _ in range(num_ejecuciones):
        n = random.randint(51, 100)  # Generar un valor aleatorio de N entre 51 y 100
        puntos = generar_puntos(n)

        distancias = []
        for i in range(n):
            for j in range(i + 1, n):
                distancia = calcular_distancia(puntos[i], puntos[j])
                distancias.append(distancia)

        promedio_distancias = np.mean(distancias)
        resultados.append(promedio_distancias)

    media_muestral = np.mean(resultados)
    desviacion_estandar_muestral = np.std(resultados, ddof=1)  # Usar ddof=1 para calcular la desviación estándar muestral

    alpha = 0.05  # Nivel de confianza (95%)
    t_critical = t.ppf(1 - alpha / 2, num_ejecuciones - 1)
    intervalo_confianza_inferior = media_muestral - (t_critical * desviacion_estandar_muestral / math.sqrt(num_ejecuciones))
    intervalo_confianza_superior = media_muestral + (t_critical * desviacion_estandar_muestral / math.sqrt(num_ejecuciones))

    print(f"Media muestral: {media_muestral}")
    print(f"Desviación estándar muestral: {desviacion_estandar_muestral}")
    print(f"Intervalo de confianza: ({intervalo_confianza_inferior}, {intervalo_confianza_superior})")

if __name__ == "__main__":
    main()

