import hashlib #biblioteca para criptografia

# Definição da senha de acesso
SENHA_HASH = "03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4"
    #senha 1234 digitada previamente convertida em hash-sha256
    #conversao feita com o codigo:
    #python -c "import hashlib; print(hashlib.sha256('1234'.encode()).hexdigest())"
    #onde 1234 é a senha traduzida em hash

# Loop de verificação de segurança
while True:
    acesso = input("Digite a senha de 4 dígitos para acessar: ")
    
    if hashlib.sha256(acesso.encode()).hexdigest() == SENHA_HASH:
        #converte o texto digitado em byte, gera o hash,
        #converte o hash em texto legivel e compara com a senha_hash
        print("Acesso concedido!\n")
        break
    else:
        print("Senha incorreta. Tente novamente.")

# --- O restante do seu programa começa aqui ---
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2

print(f"A soma entre {num1} e {num2} é: {soma}")