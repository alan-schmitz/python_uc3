frase = ["olá", "mundo", "olá", "python", "mundo"]
contagem = {}

for palavra in frase:
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1

print(contagem)