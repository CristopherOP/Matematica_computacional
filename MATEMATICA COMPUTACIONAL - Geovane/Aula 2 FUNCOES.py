import matplotlib.pyplot as plt #importar biblioteca grafica para plotagem
import numpy as np #biblioteca para efetuar operações matematicas

def graficolinear():
    x=np.linspace(-1,1,100)
    f_x=3*x-1 #definindo a função a ser calculada
    plt.plot(x,f_x,color="red", label="Sem variacao")
    plt.title("Grafico funcao linear")
    plt.axvline(0, color="black", label="(Y)") #linha vertical
    plt.axhline(0, color="purple", label="(X)") #linha horizontal
    plt.scatter(-1, -4, color="green")
    plt.scatter(0, -1, color="yellow")
    plt.scatter(1, 2, color="blue")
    plt.legend()

    plt.savefig("funcaolinear.png")
    plt.grid(True, linestyle='--', alpha=0.8)
    plt.show()

def graficoquadrantico(): 
    x=np.linspace(0, 5, 100)
    y= x**2 - 6*x + 5
    f_x=3*x-1 #definindo a função a ser calculada
    plt.plot(x,f_x,color="red", label="Sem variacao")
    plt.title("Grafico funcao linear")
    plt.axvline(0, color="black", label="(Y)") #linha vertical
    plt.axhline(0, color="purple", label="(X)") #linha horizontal

    plt.scatter(-1, -4, color="green") #destacar pontos
    plt.scatter(0, -1, color="yellow")
    plt.scatter(1, 2, color="blue")

    plt.legend()

    plt.savefig("funcaolinear.png")
    plt.grid(True, linestyle='--', alpha=0.8)
    plt.show()