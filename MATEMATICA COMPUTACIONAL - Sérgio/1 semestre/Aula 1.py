def exercicio1():
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))

    subtracao = num1 - num2

    print("Resultado da subtracao: ", subtracao)

def exercicio2():
    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero: "))

    resultado = num1 * num2
    print("Resultado do produto: ", resultado)

def exercicio3():
    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero: "))
    num3 = float(input("Digite o terceiro numero: "))
    num4 = float(input("Digite o quarto numero: "))

    media = (num1 + num2 + num3 + num4) / 4

    print("A media e: ", media)

def exercicio4():
    num1 = float(input("Digite um numero: "))

    dobro = num1 * 2
    triplo = num1 * 3

    print("O dobro e: ", dobro)
    print("O triplo e: ", triplo)

def exercicio5():
    num1 = float(input("Digite um numero: "))

    antecesssor = num1 - 1
    sucessor = num1 + 1

    print("O antecessor e: ", antecesssor)
    print("O sucessor e: ", sucessor)

def exercicio6():
    num = float(input("Digite um numero: "))

    if num > 0:
        print("O valor e positivo.")
    elif num < 0:
        print("O valor e negativo.")
    else:
        print("O valor e Zero.")

def exercicio7():
    num = int(input("Digite um numero: "))

    if num % 5 == 0:
        print("O numero e multiplo de 5.")

    else:
        print("O numero NAO e multiplo de 5.")

def exercicio8():
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))

    if num2 == 0:
        print("Nao e possivel dividir por zero")

    else:
        quociente = num1 // num2
        resto = num1 % num2

        print("Quociente: ", quociente)
        print("Resto: ", resto)

def exercicio9():
    horas = float(input("Digite o valor em horas: "))

    minutos = horas * 60

    print("O equivalente em minutos e: ", minutos)

def exercicio10():
    dias = float(input("Digite o valor em dias: "))

    horas = dias * 24

    print("Equivalente em horas: ", horas)

def exercicio11():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    media = (nota1 + nota2) / 2

    print("Media: ", media)

    if media >= 60:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")

def exercicio12():
    num = int(input("Digite um numero: "))

    if num > 0 and num % 2 == 0:
        print("O numero e positivo e par.")
    else:
        print("O numero NAO e positivo e par.")

def exercicio13():
    n1 = float(input("Digite o primeiro numero: "))
    n2 = float(input("Diite o segundo numero: "))
    n3 = float(input("Digite o terceiro numero: "))

    maior = n1

    if n2 > maior:
        maior = n2
    if n3 > maior:
        maior = n3

    print("O maior numero e: ", maior)

def exercicio14():
    n1 = float(input("Digite o primeiro numero"))
    n2 = float(input("Digite o segundo numero: "))
    n3 = float(input("Digite o terceiro numero: "))

    menor = n1

    if n2 > menor:
        menor = n2
    if n3 > menor:
        menor = n3

    print("O menor numero e: ", menor)

def exercicio15():
    num = float(input("Digite um numero: "))

    if num >= 10 and num <= 50:
        print("O numero esta entre 10 e 50.")
    else:
        print("O numero nao esta entre 10 e 50.")

def exercicio16():
    idade = int(input("Digite a idade:" ))

    if idade >= 18:
        print("Maior de idade.")

    else:
        print("Menor de idade.")

def exercicio17():
    salario = float(input("Digite o salário: "))

    if salario < 2000:
        aumento = salario * 0.10
        novo_salario = salario + aumento
        print("Novo salario com aumento: ", novo_salario)
        
    else:
        print("Salario sem aumento.")

def exercicio18():
    num = int(input("Digite um numero: "))

    if num % 3 == 0 and num % 5 == 0:
        print("O numero e divisivel por 3 e por 5.")

    else:
        print("O numero nao e divisivel por 3 e por 5.")

def exercicio19():
    nota = float(input("Digite a nota final: "))

    if nota >= 90:
        print("Conceito: A")
    elif nota >= 70:
        print("Conceito: B")
    elif nota >= 60:
        print("Conceito: C")
    else:
        print("Conceito: D")

def exercicio20():
    ladoA = float(input("Digite o primeiro lado: "))
    ladoB = float(input("Digite o segundo lado: "))
    ladoC = float(input("Digite o terceiro lado: "))

    if ladoA + ladoB > ladoC and ladoA + ladoC > ladoB and ladoB + ladoC > ladoA:
        print("Formam um triangulo.")

    else:
        print("Nao formam um triangulo.")

def exercicio21():
    for i in range(1,21):
        print(i)

def exercicio22():
    for i in range(2, 51, 2):
        print(i)

def exercicio23():
    soma = 0
    for i in range(1, 6):
        num = float(input("Digite o {i}° numero: "))
        soma += num

    print("Soma total: ", soma)

def exercicio24():
    soma  = 0
    for i in range(1, 6):
        num = float(input("Digite o {i}° numero: "))
        soma += num

    media = soma / 5
    print("Media: ", media)

def exercicio25():
    soma = 0
    while True:
        num  = float(input("Digite um numero (0 para parar): "))

        if num == 0:
            break

        soma += num

    print("Soma total: ", soma)

def exercicio26():
    while True:
        num = float(input("Digite um numero (negativo para encerrar): "))

        if num < 0:
            print("Programa encerrado.")
            break

        print("Numero digitado: ", num)

def exercicio27():
    n = int(input("Digite um numero: "))

    for i in range(3, n + 1, 3):
        print(i)

def exercicio28():
    num = int(input("Digite um numero: "))

    for i in range(1,11):
        print(f"{num} x {i} = {num * i}")

def exercicio29():
    n = int(input("Digite um numero: "))

    if n < 0:
        print("Fatorial nao existe para numero negativo.")
        return

    fatorial = 1 
    for i in range(1, n + 1):
        fatorial *= i
        print("Fatorial: ", fatorial)

def exercicio30():
    contador = 0 
    for i in range(1,11):
        num = float(input(f"Digite o {i}° numero: "))

        if num > 0:
            contador += 0
        
    print("Quantidade de números positivos: ", contador)

def exercicio31():
    lista = []

    for i in range(1,6):
        num = float(input(f"Digite o {i}° numero: "))
        lista.append(num)

    print("Lista: ", lista)

def exercicio32():
    lista = []

    for i in range(1,6):
        num = float(input(f"Digite o {i}° numero: "))
        lista.append(num)

    print("Numeros pares da lista: ")

    for num in lista:
        if num % 2 == 0:
            print(num)

def exercicio33():
    lista = []

    for i in range(1,6):
        num = float(input(f"Digite o {i}° numero: "))
        lista.append(num)

    maior = lista[0]

    for num in lista:
        if num > maior:
            maior = num

    print("Maior valor da lista: ", maior)

def exercicio34():
    lista = []

    for i in range(1,6):
        num = float(input(f"Digite o {i}° numero: "))
        lista.append(num)

    menor = lista[0]

    for num in lista:
        if num < menor:
            menor = num

    print("Menor valor da lista: ", menor)

def exercicio35():
    lista = []

    for i in range(1,6):
        num = float(input(f"Digite o {i}° numero: "))
        lista.append(num)

    soma = sum(lista)
    media = soma/len(lista)

    print("Media da lista: ", media)

def exercicio36():
    nomes = []

    for i in range(1,6):
        nome = input(f"Digite o {i}° nome: ")
        nomes.append(nome)

    print("Nomes digitados:")

    for nome in nomes:
        print(nome)

def exercicio37():
    contador = 0

    for i in range(1,6):
        num = float(input(f"Digite o {i}° numero: "))

        if num > 10:
            contador += 1

    print("Quantidade de numeros maiores que 10: ", contador)

def exercicio38():
    lista = []

    for i in range(1,6):
        num = float(input(f"Digite o {i}° numero: "))

        if num < 0:
            num = 0

        lista.append(num)

    print("Lista com negativos substituidos por zero: ")
    print(lista)

def exercicio39():
    lista = []

    for i in range(1,6):
        num = float(input(f"Digite o {i}° numero: "))
        lista.append(num)

    lista.sort()

    print("Lista em ordem crescente:")
    print(lista)

def exercicio40():
    lista = []

    for i in range(1,6):
        num = float(input(f"Digite o {i}° numero: "))
        lista.append(num)

    busca = float(input("Digite o numero que deseja procurar: "))

    if busca in lista:
        print("O numero esta presente na lista.")
    else:
        print("O numero nao esta presente na lista.")


print("\n====== MENU ======")
print("01 - Subtracao")
print("02 - Produto")
print("03 - Media")
print("04 - Dobro e triplo")
print("05 - Antecessor e sucessor")
print("06 - Positivo, negativo ou zero")
print("07 - Multiplo de 5")
print("08 - Quociente e resto")
print("09 - Horas em minutos")
print("10 - Dias para horas")
print("11 - Media para aprovacao")
print("12 - Positivo e par ou nao")
print("13 - Qual o maior")
print("14 - Qual o menor")
print("15 - Intervalo entre 10 e 50")
print("16 - Maior de idade")
print("17 - Aumento no salario")
print("18 - Divisivel por 3 e 5")
print("19 - Conceito")
print("20 - Triangulo")
print("21 - Numeros de 1 a 20")
print("22 - Numeros pares de 1 a 50")
print("23 - Soma de 5 numeros")
print("24 - Media de 5 numeros")
print("25 - Leitura de varios numeros ate 0")
print("26 - Letira de varios numeros ate negativo")
print("27 - Leia um numero e mostre os multiplos de 3")
print("28 - Tabuada de 1 a 10")
print("29 - Fatorial")
print("30 - Quantos sao positivos")
print("31 - Lista de numeros")
print("32 - Lista de numeros pares")
print("33 - Maior valor da lista")
print("34 - Menor valor da lista")
print("35 - Media dos valores da lista")
print("36 - Mostre todos os numeros armazenados")
print("37 - Leia os numeros e conte quais sao maiores que 10")
print("38 - Leia os numeros e substitua os valores negativos por 0")
print("39 - Leia os numeros e monte a lista em ordem crescente")
print("40 - Leia os numeros e informe se um numero especifico esta presente na lista")

opcao = input("Escolha: ")

if opcao == "01":
    exercicio1()
elif opcao == "02":
    exercicio2()
elif opcao == "03":
    exercicio3()
elif opcao == "04":
    exercicio4()
elif opcao == "05":
    exercicio5()
elif opcao == "06":
    exercicio6()
elif opcao == "07":
    exercicio7()
elif opcao == "08":
    exercicio8()
elif opcao == "09":
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
elif opcao == "16":
    exercicio16()
elif opcao == "17":
    exercicio17()
elif opcao == "18":
    exercicio18()
elif opcao == "19":
    exercicio19()
elif opcao == "20":
    exercicio20()
elif opcao == "21":
    exercicio21()
elif opcao == "22":
    exercicio22()
elif opcao == "23":
    exercicio23()
elif opcao == "24":
    exercicio24()
elif opcao == "25":
    exercicio25()
elif opcao == "26":
    exercicio26()
elif opcao == "27":
    exercicio27()
elif opcao == "28":
    exercicio28()
elif opcao == "29":
    exercicio29()
elif opcao == "30":
    exercicio30()
elif opcao == "31":
    exercicio31()
elif opcao == "32":
    exercicio32()
elif opcao == "33":
    exercicio33()
elif opcao == "34":
    exercicio34()
elif opcao == "35":
    exercicio35()
elif opcao == "36":
    exercicio36()
elif opcao == "37":
    exercicio37()
elif opcao == "38":
    exercicio38()
elif opcao == "39":
    exercicio39()
elif opcao == "40":
    exercicio40()
elif opcao == "0":
    print("Encerrando...")
else:
    print("Opcao invalida.")