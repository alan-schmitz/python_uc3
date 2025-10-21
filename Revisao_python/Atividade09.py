vendas = [("A", 150), ("B", 200), ("C", 80)]
total = 0

for produto, valor in vendas:
    total += valor

print(f"a soma dos valores dos produtos e: {total}")