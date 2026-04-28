import matplotlib.pyplot as plt
import numpy as np
import math

# calcular as raízes

def calcular_raizes(a, b, c):
    delta = b**2 - 4*a*c

    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return x1, x2
    elif delta == 0:
        x1 = x2 = -b / (2*a)
        return x1, x2
    else:
        return None, None

# retornar as coordenadas do vértice

def calcular_vertice(a, b, c):
    delta = b**2 - 4*a*c
    xv = -b / (2*a)
    yv = -delta / (4*a)
    return xv, yv

# plotar o gráfico com matplotlib e numpy

def plotar_grafico(a, b, c):
    x = np.linspace(-10, 10, 100)
    y = a*x**2 + b*x + c

    plt.plot(x, y)
    plt.axhline(0, color='black', lw=1)  # Eixo X
    plt.axvline(0, color='black', lw=1)  # Eixo Y
    plt.title(f"Gráfico da Função: {a}x² + {b}x + {c}")
    plt.show()

# letra a)

a, b, c = 1, -5, 6

x1, x2 = calcular_raizes(a, b, c)
print(f"Raízes: x1 = {x1}, x2 = {x2}")

xv, yv = calcular_vertice(a, b, c)
print(f"Vértice: ({xv}, {yv})")

plotar_grafico(a, b, c)

# letra b)

a, b, c = -5, 20, 0

x1, x2 = calcular_raizes(a, b, c)
print(f"Raízes: x1 = {x1}, x2 = {x2}")

xv, yv = calcular_vertice(a, b, c)
print(f"Vértice: ({xv}, {yv})")

plotar_grafico(a, b, c)

# CHAMANDO AS FUNÇÕES - letra c)

a, b, c = 1, -2, 5

x1, x2 = calcular_raizes(a, b, c)
print(f"Raízes: {x1} (sem raízes reais)")

xv, yv = calcular_vertice(a, b, c)
print(f"Vértice: ({xv}, {yv})")

plotar_grafico(a, b, c)