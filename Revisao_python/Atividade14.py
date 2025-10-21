estoque = {"teclado": 5, "mouse": 10, "monitor": 3}
vendas_hoje = ["teclado", "mouse", "teclado"]

for item in vendas_hoje:
    if item in estoque and estoque[item] > 0:
        estoque[item] -= 1

print(estoque) 