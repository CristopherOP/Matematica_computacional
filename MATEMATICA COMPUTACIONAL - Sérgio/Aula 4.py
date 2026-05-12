import random
import time

# Bubble Sort
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Quick Sort
def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivo = lista[0]
        menores = [x for x in lista[1:] if x <= pivo]
        maiores = [x for x in lista[1:] if x > pivo]
        return quick_sort(menores) + [pivo] + quick_sort(maiores)

# Gerar lista
lista = [random.randint(1, 10000) for _ in range(10000)]

# Copiar listas
lista1 = lista.copy()
lista2 = lista.copy()

# Teste Bubble Sort
inicio = time.time()
bubble_sort(lista1)
fim = time.time()
print("Tempo Bubble Sort:", fim - inicio)

# Teste Quick Sort
inicio = time.time()
quick_sort(lista2)
fim = time.time()
print("Tempo Quick Sort:", fim - inicio)