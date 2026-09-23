from datetime import date
novo="S"
contador= 0
nomes = []

while (novo=="S"):
  nome=input("Digite seu nome\n") #variavel tipo string, ou cadeia de caracteres
  sobrenome=input("Digite seu sobrenome\n")
  nomecompleto=nome.strip()+" "+sobrenome.strip()
  
  if (len(nome.strip())==0) and (len(sobrenome.strip())==0):
    print("Voce deve digitar todas as informações pedidas.")
  else:
    print("Nome completo:", nomecompleto) #concatenação, juntar as variaveis
    nomes.append(nomecompleto) #guarda o nome na lista
    contador += 1
  novo=input("Deseja cadastrar nova pessoa? S/N ").upper()

  if (novo!="S") and (novo!="N"):
    print("Opção invalida")

print("Quantidade de nomes cadastrados:", contador)

for pessoa in nomes:
  print("-", pessoa)

print("\n Nomes cadastrados:", contador)  
print("\n Data de hoje", date.today)
print("------------------------\n")
print("Nome         Sobrenome")
print("------------------------\n")
matriz_nome=list(nome)
matriz_sobrenome=list(sobrenome)
for i in range(contador):
   print(matriz_nome[i],"         ", matriz_sobrenome[i])


