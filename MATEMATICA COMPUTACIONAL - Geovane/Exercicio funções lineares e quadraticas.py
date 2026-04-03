import numpy as np
import matplotlib.pyplot as plt

def exercicio1():
    x = np.linspace(-10, 10, 100)
    y = 5*x + 10
    plt.plot(x, y)
    plt.title("f(x) = 5x + 10")
    plt.grid()
    plt.show()

def exercicio2():
    print("Coeficiente angular: -2")
    print("Coeficiente linear: 5")

def exercicio3():
    x = np.linspace(0, 6, 100)
    y = 4*x - 12
    plt.plot(x, y)
    plt.scatter(3, 0)
    plt.title("Raiz em x = 3")
    plt.grid()
    plt.show()

def exercicio4():
    x = np.linspace(-10, 10, 100)
    plt.plot(x, x, label="f(x)=x")
    plt.plot(x, 2*x, label="g(x)=2x")
    plt.legend()
    plt.grid()
    plt.show()

def exercicio5():
    a = float(input("Digite a: "))
    b = float(input("Digite b: "))
    x = np.linspace(-10, 10, 100)
    y = a*x + b
    plt.plot(x, y)
    plt.title(f"f(x) = {a}x + {b}")
    plt.grid()
    plt.show()

def exercicio6():
    x = np.linspace(0, 20, 100)
    y = 2.5*x + 5
    plt.plot(x, y)
    plt.title("Custo do táxi")
    plt.grid()
    plt.show()

def exercicio7():
    a, b, c = 1, -5, 6
    delta = b**2 - 4*a*c
    x1 = (-b + np.sqrt(delta)) / (2*a)
    x2 = (-b - np.sqrt(delta)) / (2*a)
    print("Raízes:", x1, x2)

def exercicio8():
    x = np.linspace(-5, 5, 100)
    plt.plot(x, x**2, label="x^2")
    plt.plot(x, -x**2, label="-x^2")
    plt.legend()
    plt.grid()
    plt.show()

def exercicio9():
    a, b, c = 2, -4, 8
    xv = -b / (2*a)
    yv = a*xv**2 + b*xv + c
    print("Vértice:", xv, yv)

    x = np.linspace(-2, 4, 100)
    y = a*x**2 + b*x + c
    plt.plot(x, y)
    plt.scatter(xv, yv)
    plt.grid()
    plt.show()

def exercicio10():
    x = np.linspace(-5, 5, 100)
    y = x**2 - 4
    plt.plot(x, y)
    plt.scatter([-2, 2], [0, 0])
    plt.grid()
    plt.show()

def exercicio11():
    x = np.linspace(-5, 5, 100)
    for c in [-2, 0, 2]:
        y = x**2 + c
        plt.plot(x, y, label=f'c={c}')
    plt.legend()
    plt.grid()
    plt.show()

def exercicio12():
    a, b, c = -5, 20, 0
    t_v = -b / (2*a)
    h_max = a*t_v**2 + b*t_v + c
    print("Altura máxima:", h_max)

def exercicio13():
    a, b, c = 1, -5, 6
    delta = b**2 - 4*a*c

    if delta > 0:
        print("Duas raízes reais")
    elif delta == 0:
        print("Uma raiz real")
    else:
        print("Nenhuma raiz real")

def exercicio14():
    x = np.linspace(-1, 3, 100)
    y1 = x**2
    y2 = 2*x

    plt.plot(x, y1, label="x^2")
    plt.plot(x, y2, label="2x")
    plt.scatter([0, 2], [0, 4])

    plt.legend()
    plt.grid()
    plt.show()

def exercicio15():
    x = np.linspace(-2, 2, 100)
    y = x**2

    plt.plot(x, y)
    plt.fill_between(x, y, 0, alpha=0.3)
    plt.grid()
    plt.show()


def menu():
    while True:
        print("\n===== MENU DE EXERCÍCIOS =====")
        print("1 - Exercício 1")
        print("2 - Exercício 2")
        print("3 - Exercício 3")
        print("4 - Exercício 4")
        print("5 - Exercício 5")
        print("6 - Exercício 6")
        print("7 - Exercício 7")
        print("8 - Exercício 8")
        print("9 - Exercício 9")
        print("10 - Exercício 10")
        print("11 - Exercício 11")
        print("12 - Exercício 12")
        print("13 - Exercício 13")
        print("14 - Exercício 14")
        print("15 - Exercício 15")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            exercicio1()
        elif opcao == "2":
            exercicio2()
        elif opcao == "3":
            exercicio3()
        elif opcao == "4":
            exercicio4()
        elif opcao == "5":
            exercicio5()
        elif opcao == "6":
            exercicio6()
        elif opcao == "7":
            exercicio7()
        elif opcao == "8":
            exercicio8()
        elif opcao == "9":
            exercicio9()
        elif opcao == "10":
            exercicio10()
        elif opcao == "11":
            exercicio11()
        elif opcao == "12":
            exercicio12()
        elif opcao == "13":
            exercicio13()
        elif opcao == "14":
            exercicio14()
        elif opcao == "15":
            exercicio15()
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida!")

menu()