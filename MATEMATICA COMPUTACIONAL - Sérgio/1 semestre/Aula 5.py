def exercicio_01():
    numeros = []
    for i in range(10):
        n = int(input(f"Digite o {i+1}º número: "))
        numeros.append(n)
    print("\nLista original:", numeros)
    print("Maior valor:", max(numeros))
    print("Menor valor:", min(numeros))


def exercicio_02():
    qtd = int(input("Quantos números você vai digitar? "))
    numeros = []
    for i in range(qtd):
        n = int(input(f"Digite o {i+1}º número: "))
        numeros.append(n)
    pares = [x for x in numeros if x % 2 == 0]
    print("\nLista original:", numeros)
    print("Lista de pares:", pares)


def exercicio_03():
    qtd = int(input("Quantos números você vai digitar? "))
    numeros = []
    for i in range(qtd):
        n = float(input(f"Digite o {i+1}º número: "))
        numeros.append(n)
    soma = sum(numeros)
    media = soma / len(numeros)
    print("\nLista:", numeros)
    print(f"Soma: {soma}")
    print(f"Média: {media:.2f}")


def bubble_sort_crescente(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def exercicio_04():
    qtd = int(input("Quantos números você vai digitar? "))
    numeros = []
    for i in range(qtd):
        n = int(input(f"Digite o {i+1}º número: "))
        numeros.append(n)
    print("\nAntes da ordenação:", numeros)
    print("Após Bubble Sort (crescente):", bubble_sort_crescente(numeros[:]))


def bubble_sort_decrescente(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j] < lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def exercicio_05():
    qtd = int(input("Quantos números você vai digitar? "))
    numeros = []
    for i in range(qtd):
        n = int(input(f"Digite o {i+1}º número: "))
        numeros.append(n)
    print("\nAntes da ordenação:", numeros)
    print("Após Bubble Sort (decrescente):", bubble_sort_decrescente(numeros[:]))


def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivo = lista[-1]
    menores = [x for x in lista[:-1] if x <= pivo]
    maiores = [x for x in lista[:-1] if x > pivo]
    return quick_sort(menores) + [pivo] + quick_sort(maiores)

def exercicio_06():
    qtd = int(input("Quantos números você vai digitar? "))
    numeros = []
    for i in range(qtd):
        n = int(input(f"Digite o {i+1}º número: "))
        numeros.append(n)
    print("\nAntes da ordenação:", numeros)
    print("Após Quick Sort (crescente):", quick_sort(numeros))


# ─────────────────────────────────────────
#  MENU 
# ─────────────────────────────────────────

exercicios = {
    1: exercicio_01,
    2: exercicio_02,
    3: exercicio_03,
    4: exercicio_04,
    5: exercicio_05,
    6: exercicio_06,
}

print("=" * 40)
print(" Exercícios de Lista")
print("=" * 40)
print(" 1 → Lista básica")
print(" 2 → Filtragem de pares")
print(" 3 → Soma e média")
print(" 4 → Bubble Sort crescente")
print(" 5 → Bubble Sort decrescente")
print(" 6 → Quick Sort")
print("=" * 40)

escolha = int(input("Digite o número do exercício: "))

if escolha in exercicios:
    print(f"\n── Exercício {escolha:02d} ──────────────────────\n")
    exercicios[escolha]()
else:
    print("Opção inválida. Escolha um número entre 1 e 6.")