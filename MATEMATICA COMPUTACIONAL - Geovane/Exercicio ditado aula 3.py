import numpy as np
import matplotlib.pyplot as plt

#ENTRADA
nome = input("Digite seu nome: ")

inicio = float(input("Digite o valor inicial de X: "))
fim = float(input("Digite o valor final de X: "))

base = float(input("Digite o valor da base (a): "))

#PROCESSAMENTO
x= np.linspace(inicio, fim, 100)
y= np.power(base,x)

media_y= np.mean(y)

#SAIDA
print(f"\nNome: {nome}")
print(f"Valor medio de Y: {media_y:.2f}")

#GRAFICO
plt.figure(figsize=(10,5))

plt.plot(x, y, label=f'f(x)={base}^x')
plt.title(f"Função exponencial - {nome}")
plt.xlabel("X")
plt.ylabel("Y")

plt.grid()
plt.legend()

#TEXTO ABAIXO DO GRAFICO
plt.figtext(0.5, -0.05, f"Valor medio de Y = {media_y:.2f}",
            ha="center", fontsize=12)

plt.show()  