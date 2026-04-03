import matplotlib.pyplot as plt #biblioteca para geração do grafico
import numpy as np #biblioteca para geração de coleção de listas

x=np.arange(-2,3+1) #gerando listas de valores para x aleatorios

print("Valores de x:", x)
base=2.0
y= np.power(base,x)
plt.figure(figsize=(12,6))
plt.title("Grafico da função f(x)=a^x")
plt.xlabel("Valores de X")
plt.ylabel("Valores de Y")
plt.plot(x,y)
plt.show()

print("EXERCICIO 2")
#valores de y: [0,25 0,5 0 1. 2. 3.]
#valores de x: [-2 -1 0 1 2 3]

capital=1000
taxa=0.20
periodo=np.arange(1,12+1, dtype=float)
montante=np.power(capital*(1+taxa), periodo)
plt.plot(periodo,montante)
plt.show()
print(periodo)
print(montante[1])

