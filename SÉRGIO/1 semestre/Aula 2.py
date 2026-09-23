A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7}
C = {2, 4, 6, 8}
U = {1, 2, 3, 4, 5, 6, 7, 8}
#exercicio 1
resultado = (A and B) or C
print(resultado)
#exercicio 2
resultado = (A or C) and (B - A)
print(resultado)
#exercicio 3
complemento = U - A
print(complemento)
#exercicio 4
esquerda = A & (B | C)
direita = (A & B) | (A & C)
print(esquerda == direita)
#exercicio 5
resultado = C.issubset (A | B)
print(resultado)
#exercicio 6
resultado = A.isdisjoint(C)
print(resultado)
#exercicio 7    
p = True
q = False
r = True

resultado = (p and q) or r
print(resultado)
#exercicio 8
resultado = not (p or q) and r
print(resultado)
#exercicio 9
resultado = (p or q) and (not r)
print(resultado)
#exercicio 10
valores = [True, False]

for q in valores:
    resultado = (p and q) or (not q)
    print(p, q, resultado)

#exercicio 11
x = 3
y = 8

resultado = (x in A) and (y not in B)
print(resultado)

#exercicio 12
resultado = len(A & B) != 0
print(resultado)

#exercicio 13
p = True
q = False

resultado = not (p and q) == (not p or not q)
print(resultado)